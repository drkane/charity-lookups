# /// script
# dependencies = [
#   "pandas",
#   "sqlalchemy",
#   "psycopg2-binary",
# ]
# ///
import os

import pandas as pd

DB_URL = os.environ.get("FTC_DB_URL")

df = (
    pd.read_sql(
        """
with mutuals as (
select *
    from ftc_organisation fo
    where source_id = 'mutuals'
), companies as (
    select *
    from companies_company cc
    where "CompanyCategory" != 'ltd'
)
select m.org_id,
    m."orgIDs",
    m.name,
    m."postalCode",
    m."dateRegistered",
    m."dateRemoved",
    m.active,
    m."organisationType",
    c."CompanyNumber",
    c."CompanyName",
    c."CompanyCategory",
    c."IncorporationDate",
    ltrim(regexp_replace(m.org_id, '[^0-9]+', '', 'g'), '0') as mutual_digits,
    ltrim(regexp_replace(c."CompanyNumber", '[^0-9]+', '', 'g'), '0') as company_digits
from mutuals m
left outer join companies c
    on trim(
            replace(
                upper(
                    regexp_replace(m.name, '[^[:alnum:]]+', ' ', 'g')
                ),
                ' LTD',
                'LIMITED'
            )
        ) =
       trim(
            replace(
                upper(
                    regexp_replace(c."CompanyName", '[^[:alnum:]]+', ' ', 'g')
                ),
                ' LTD',
                'LIMITED'
            )
        )
order by m."organisationType", mutual_digits;
""",
        con=DB_URL,
    )
    .assign(
        organisationType=lambda x: x["organisationType"].apply(lambda y: y[1]),
        company_id=lambda x: x["CompanyNumber"].apply("GB-COH-{}".format),
        mutual_digits=lambda x: x["mutual_digits"].replace("", pd.NA).astype("Int64"),
        company_digits=lambda x: x["company_digits"].replace("", pd.NA).astype("Int64"),
    )
    .sort_values(
        by=["organisationType", "mutual_digits", "org_id", "company_id"],
    )
)
print(f"Found {len(df)} mutual companies in original query")


df = (
    df.loc[
        df["mutual_digits"] == df["company_digits"],
        [
            "org_id",
            "company_id",
            "name",
        ],
    ]
    .rename(
        columns={
            "org_id": "org_id_a",
            "company_id": "org_id_b",
            "name": "org_name",
        }
    )
    .assign(
        relationship="sameas",
        source="Mutual companies",
    )
    .sort_values(
        by=["org_id_a", "org_id_b"],
    )
)
print(f"Found {len(df)} mutual companies after deduplication")

filename = os.path.join("relationships", "mutual-companies.csv")
original_df = pd.read_csv(filename)

df = pd.concat([original_df, df], ignore_index=True).drop_duplicates(
    ["org_id_a", "org_id_b"], keep="last"
)
print(f"Found {len(df)} mutual companies to save")

df.to_csv(filename, index=False)
print(f"Saved to {filename}")
