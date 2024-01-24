import os

import pandas as pd


def strip_org_id(org_id: str):
    if not isinstance(org_id, str):
        return org_id
    return org_id.split("-", maxsplit=2)[-1]


RELATIONSHIP_DIR = os.path.join(os.path.dirname(__file__), "..", "relationships")


# filename: (assigns, columns)
RELATIONSHIP_FILES = {
    "ccew-register-of-mergers.csv": (
        {
            "date_merger_registered": lambda x: x["valid_from"],
            "transferor_name": lambda x: x["org_name_a"],
            "transferee_name": lambda x: x["org_name_b"],
        },
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
        ],
    ),
    "charity-company-numbers.csv": (
        {"name": lambda x: x["org_name"]},
        ["org_id_a", "org_id_b", "name"],
    ),
    "charity-reregistrations.csv": (
        {
            "Old charity number": lambda x: x["org_id_a"].apply(strip_org_id),
            "New charity number": lambda x: x["org_id_b"].apply(strip_org_id),
            "Name": lambda x: x["org_name"],
        },
        ["Old charity number", "New charity number", "Name"],
    ),
    "cio-company-numbers.csv": (
        {
            "company_number": lambda x: x["org_id_a"].apply(strip_org_id),
            "charity_number": lambda x: x["org_id_b"].apply(strip_org_id),
        },
        ["company_number", "charity_number"],
    ),
    "dual-registered-uk-charities.csv": (
        {
            "Scottish Charity Number": lambda x: x["org_id_a"].apply(strip_org_id),
            "E&W Charity Number": lambda x: x["org_id_b"].apply(strip_org_id),
            "Charity Name (E&W)": lambda x: x["org_name_b"],
        },
        ["Scottish Charity Number", "E&W Charity Number", "Charity Name (E&W)"],
    ),
    "federated-charities.csv": (
        {
            "type": lambda x: x["federation"],
            "reg_number": lambda x: (
                x["org_id_b"].str.replace("GB-NIC-", "GB-NIC-NI").apply(strip_org_id)
            ),
            "name": lambda x: x["org_name_a"],
        },
        ["type", "reg_number", "name"],
    ),
    "grid-lookup.csv": (
        {
            "grid_id": lambda x: x["org_id_a"].apply(strip_org_id),
            "org_id": lambda x: x["org_id_b"],
        },
        ["grid_id", "org_id"],
    ),
    "mutual-companies.csv": (
        {
            "mutual_id": lambda x: x["org_id_a"],
            "company_id": lambda x: x["org_id_b"],
            "name": lambda x: x["org_name"],
        },
        ["mutual_id", "company_id", "name"],
    ),
    "organisation-company-numbers.csv": (
        {
            "name": lambda x: x["org_name"],
        },
        ["org_id_a", "org_id_b", "name"],
    ),
    "oxbridge-charity-numbers.csv": (
        {
            "College": lambda x: x["college_name"],
            "University": lambda x: x["org_name_b"].str.replace("University of ", ""),
            "Charity Number": lambda x: x["org_id_b"].apply(strip_org_id),
            "Charity Name": lambda x: x["org_name_a"],
            "Note": lambda x: x["note"],
            "Parent Org ID": lambda x: x["org_id_a"],
        },
        [
            "College",
            "University",
            "Charity Number",
            "Charity Name",
            "Note",
            "Parent Org ID",
        ],
    ),
    "rsp-charity-number.csv": (
        {
            "RP Code": lambda x: x["org_id_a"].apply(strip_org_id),
            "Company Number": lambda x: x["company_number"],
            "Charity Number": lambda x: x["charity_number"],
            "Org ID": lambda x: x["org_id_b"],
        },
        ["RP Code", "Company Number", "Charity Number", "Org ID"],
    ),
    "university-charity-number.csv": (
        {
            "Name": lambda x: x["org_name"],
            "HESA ID": lambda x: x["org_id_a"].apply(strip_org_id),
            "OrgID": lambda x: x["org_id_b"],
        },
        ["Name", "HESA ID", "OrgID"],
    ),
    "university-royal-charters.csv": (
        {
            "Name": lambda x: x["org_name"],
            "URN": lambda x: x["org_id_a"].apply(strip_org_id),
            "CompanyNumber": lambda x: x["org_id_b"].apply(strip_org_id),
        },
        ["URN", "Name", "CompanyNumber"],
    ),
}


def main():
    output_df = pd.DataFrame(
        columns=[
            "org_id_a",
            "org_id_b",
            "relationship",
            "source",
            "valid_from",
            "valid_to",
            "org_name",
            "org_name_a",
            "org_name_b",
        ]
    )

    # go through the relationships directory
    for filename in os.listdir(RELATIONSHIP_DIR):
        if not filename.endswith(".csv") or filename.startswith("_"):
            print(f"{filename}: skipped")
            continue

        if filename == "cio-company-numbers.csv":
            output_filename = os.path.join(
                os.path.dirname(__file__), "..", "cio_company_numbers.csv"
            )
        else:
            output_filename = os.path.join(os.path.dirname(__file__), "..", filename)

        input_filename = os.path.join(RELATIONSHIP_DIR, filename)
        data = pd.read_csv(input_filename, dtype=str)

        if filename in RELATIONSHIP_FILES and os.path.exists(output_filename):
            assigns, columns = RELATIONSHIP_FILES[filename]
            data.assign(**assigns)[columns].to_csv(output_filename, index=False)
            print(f"{filename}: {len(data)} rows replicated in {output_filename}")

        print(f"{filename}: {len(data)} rows included")

        output_df = pd.concat(
            [output_df, data[[c for c in output_df.columns if c in data.columns]]],
            ignore_index=True,
        )

    for relationship in output_df["relationship"].unique():
        relationship_df = output_df[output_df["relationship"] == relationship]
        relationship_df = relationship_df[
            (relationship_df["org_id_a"] != relationship_df["org_id_b"])
            & relationship_df["org_id_a"].notnull()
            & relationship_df["org_id_b"].notnull()
        ]
        relationship_df.to_csv(
            os.path.join(RELATIONSHIP_DIR, f"_{relationship}.csv"),
            index=False,
        )
        print(
            f"{relationship}: {len(relationship_df)} rows saved as _{relationship}.csv"
        )


if __name__ == "__main__":
    main()
