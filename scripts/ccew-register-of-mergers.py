import re
import argparse
import csv
import os

import pandas as pd
from requests_html import HTMLSession

# updated version of https://gist.github.com/drkane/0faa257e447452661a4d

# default location of the register of mergers
ROM_PAGE = "https://www.gov.uk/government/publications/register-of-merged-charities"

# function for spliting dataframe rows based on separating a column
# from https://gist.github.com/jlln/338b4b0b55bd6984f883#gistcomment-2359013
def splitDataFrameList(df, target_column, separator):
    """df = dataframe to split,
    target_column = the column containing the values to split
    separator = the symbol used to perform the split
    returns: a dataframe with each entry for the target column separated, with each element moved into a new row.
    The values in the other columns are duplicated across the newly divided rows.
    """

    row_accumulator = []

    def splitListToRows(row, separator):
        split_row = re.split(separator, row[target_column])
        for s in split_row:
            new_row = row.to_dict()
            new_row[target_column] = s
            row_accumulator.append(new_row)

    df.apply(splitListToRows, axis=1, args=(separator,))
    new_df = pd.DataFrame(row_accumulator)
    return new_df


def find_rom(rom_page):
    """
    Find the latest register of mergers on a page
    """
    session = HTMLSession()
    r = session.get(rom_page)
    return next(l for l in r.html.absolute_links if l.endswith(".csv"))


def parse_rom(rom):
    """
    Takes a link to the register of mergers and returns a formatted dataset
    """

    print("Loading data from {}".format(rom))

    # load the file into pandas
    if rom.endswith("csv"):
        rom_df = pd.read_csv(rom, skip_blank_lines=True, encoding="latin_1")
    elif rom.endswith("xls") or rom.endswith("xlsx"):
        rom_df = pd.read_excel(rom, skip_blank_lines=True, encoding="latin_1")

    # remove any blank rows
    rom_df = rom_df.dropna(how="all")

    original_rows = len(rom_df)
    print("{:,.0f} rows loaded".format(len(rom_df)))

    # drop any empty columns
    non_null_columns = [
        col for col in rom_df.columns if rom_df.loc[:, col].notna().any()
    ]
    rom_df = rom_df[non_null_columns]

    # rename the columns for ease of use
    print("Existing columns:")
    for c in rom_df.columns:
        print(" - {}".format(c))
    new_columns = {
        "Name of transferring charity (transferor) and charity number (if any)": "transferor_name",
        "Name of receiving charity (transferee) and charity number (if any)": "transferee_name",
        "Date Vesting Declaration made": "date_vesting_declaration",
        "Date property transferred": "date_property_transferred",
        "Date merger registered": "date_merger_registered",
    }
    rom_df = rom_df.rename(columns=lambda c: new_columns.get(c.strip(), c))
    print("renamed columns")
    for c in new_columns.values():
        print(c)
        assert c in rom_df.columns

    # look for rows split by lots of spaces
    rom_df = splitDataFrameList(rom_df, "transferor_name", r"\s\s\s\s+")
    print("{:,.0f} rows added by splitting rows".format(len(rom_df) - original_rows))

    # look for charity numbers in the data
    # charity number extraction includes looking for subsidiary numbers
    regno_regex = r"\(([0-9]{6,7})([\-\/]([0-9]+))?\)"

    for f in ["transferor", "transferee"]:
        regno = rom_df[f + "_name"].str.extract(regno_regex, expand=True)
        rom_df.loc[:, f + "_regno"] = regno[0]
        rom_df.loc[:, f + "_subno"] = regno[2].fillna(0)
        rom_df.loc[:, f + "_name"] = rom_df[f + "_name"].str.replace(regno_regex, "")
        rom_df.loc[rom_df[f + "_regno"].isnull(), f + "_subno"] = None
    print("Charity numbers extracted")
    print(
        "{:,.0f} transferees don't have charity numbers".format(
            len(rom_df[rom_df.transferee_regno.isnull()])
        )
    )
    print(
        "{:,.0f} transferors don't have charity numbers".format(
            len(rom_df[rom_df.transferor_regno.isnull()])
        )
    )

    # trim fields
    for f in ["transferor_name", "transferee_name"]:
        rom_df.loc[:, f] = rom_df[f].str.strip()
        rom_df.loc[:, f] = rom_df[f].str.strip(",")

    # force dates into format
    date_fields = [
        "date_vesting_declaration",
        "date_property_transferred",
        "date_merger_registered",
    ]
    for f in date_fields:

        rows_with_str = rom_df[f].apply(type).eq(str)

        if not rows_with_str.any():
            continue

        # fix date typos
        date_replace = [
            ("`", ""),
            ("I ", "01 "),
            ("Janaury", "January"),
            ("Janurary", "January"),
            ("Marhc", "March"),
            ("Ju;u", "June"),
            ("Octboer", "October"),
            ("Deceber", "December"),
            ("Decimber", "December"),
            ("Augiust", "August"),
        ]
        for d in date_replace:
            rom_df.loc[rows_with_str, f] = rom_df.loc[rows_with_str, f].str.replace(
                d[0], d[1]
            )

        rom_df.loc[:, f] = pd.to_datetime(rom_df[f])

    without_date_field = len(rom_df[date_fields].dropna(how="all"))

    print(
        "{:,.0f} rows don't have a valid date".format(len(rom_df) - without_date_field)
    )

    # fix typo in a charity number
    # 1115638 => 1112538
    charity_number_typos = [
        # (From, To),
        ("1115638", "1112538", "transferor_regno"),
        ("1076829", "1076289", "transferor_regno"),
    ]
    for number_from, number_to, field in charity_number_typos:
        rom_df.loc[rom_df[field] == number_from, field] = number_to

    # reorder the columns
    rom_df = rom_df[
        [
            "transferor_name",
            "transferor_regno",
            "transferor_subno",
            "transferee_name",
            "transferee_regno",
            "transferee_subno",
            "date_vesting_declaration",
            "date_property_transferred",
            "date_merger_registered",
        ]
    ].sort_values(
        [
            "date_merger_registered",
            "transferee_regno",
            "transferor_regno",
        ]
    )

    return rom_df.sort_values("date_merger_registered")


def main():

    parser = argparse.ArgumentParser(
        description="Import the Charity Commission register of mergers"
    )
    parser.add_argument(
        "--input", default=ROM_PAGE, help="The register of mergers file"
    )
    parser.add_argument(
        "--output",
        default=os.path.join(
            os.path.dirname(__file__), "..", "ccew-register-of-mergers.csv"
        ),
        help="CSV file to output data in",
    )
    args = parser.parse_args()

    rom_link = find_rom(args.input)

    rom_df = parse_rom(rom_link)
    rom_df.to_csv(
        args.output, index=False, date_format="%Y-%m-%d", quoting=csv.QUOTE_NONNUMERIC
    )
    print("{:,.0f} rows saved to {}".format(len(rom_df), args.output))


if __name__ == "__main__":
    main()
