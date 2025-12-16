# /// script
# dependencies = [
#   "requests",
#   "sqlalchemy",
#   "tqdm",
#   "psycopg2-binary",
#   "python-dotenv",
# ]
# ///
import csv
import os
import time

import requests
import sqlalchemy
import tqdm
from dotenv import load_dotenv

load_dotenv()

DB_URI = os.environ.get("FTC_DB_URL")
CIOS_FILE = os.path.join("relationships", "cio-company-numbers.csv")
COMPANY_HOUSE_API_KEY = os.environ.get("COMPANY_HOUSE_API_KEY")
COMPANY_HOUSE_API_URL = "https://api.companieshouse.gov.uk/company/{}"
SOURCE = {
    "relationship": "sameas",
    "source": "CIO Company Numbers",
}


def strip_org_id(org_id: str):
    if not isinstance(org_id, str):
        return org_id
    return org_id.split("-", maxsplit=2)[-1]


def add_charity_org_id(regno: str):
    if regno.startswith("SC"):
        return "GB-SC-{}".format(regno)
    elif regno.startswith("N") or (regno.startswith("1") and len(regno) == 6):
        return "GB-NIC-{}".format(regno)
    else:
        return "GB-CHC-{}".format(regno)


existing_cios = {}
with open(CIOS_FILE) as a:
    reader = csv.DictReader(a)
    fields = reader.fieldnames
    for r in reader:
        r["company_number"] = strip_org_id(r["org_id_a"])
        r["charity_number"] = strip_org_id(r["org_id_b"])
        existing_cios[r["company_number"]] = r["charity_number"]


engine = sqlalchemy.create_engine(DB_URI, pool_pre_ping=True)
with engine.connect() as con:
    result = con.execute(
        sqlalchemy.text(
            """
    select "CompanyNumber", "CompanyName" 
    from companies_company
    where "CompanyNumber" like 'CS%%'
        or "CompanyNumber" like 'CE%%'
    """
        )
    )
    print("Companies in FTC:", result.rowcount)

    with open(CIOS_FILE, "w", newline="") as a:
        writer = csv.DictWriter(a, fieldnames=fields)
        writer.writeheader()

        print("Existing CIOS:", len(existing_cios))
        for coyno, regno in existing_cios.items():
            writer.writerow(
                {
                    "org_id_a": f"GB-COH-{coyno}",
                    "org_id_b": add_charity_org_id(regno),
                    **SOURCE,
                }
            )

        result = [r for r in result if r.CompanyNumber not in existing_cios]
        print("Companies to check:", len(result))
        for k, r in tqdm.tqdm(enumerate(result), total=len(result)):
            request = requests.get(
                COMPANY_HOUSE_API_URL.format(r.CompanyNumber),
                auth=(COMPANY_HOUSE_API_KEY, ""),
            )
            try:
                request.raise_for_status()
            except requests.exceptions.HTTPError:
                print(f"Error for {r.CompanyNumber}")
                continue
            co = request.json()
            if "external_registration_number" in co:
                writer.writerow(
                    {
                        "org_id_a": f"GB-COH-{r.CompanyNumber}",
                        "org_id_b": add_charity_org_id(
                            co["external_registration_number"]
                        ),
                        **SOURCE,
                    }
                )
            time.sleep(0.5)
