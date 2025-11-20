# /// script
# dependencies = [
#   "pandas",
#   "python-dotenv",
# ]
# ///
import csv
import os
import time

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

DB_URI = os.environ.get("FTC_DB_URL")
DUAL_REGISTERED_FILE = os.path.join("relationships", "dual-registered-uk-charities.csv")

QUERY = """
WITH crossborder_existing AS (
        SELECT org_id,
                linked_orgs
        FROM ftc_organisation
        WHERE org_id ILIKE 'GB-SC-%'
                AND jsonb_array_length(jsonb_path_query_array(array_to_json(linked_orgs)::jsonb, '$[*] ? (@ starts with "GB-CHC-")')) > 0
        ORDER BY "latestIncome" DESC NULLS LAST
), crossborder AS (
        SELECT r.org_id,
                r."data"->>'Parent charity name' AS parent_name,
                r."data"->>'Parent charity number' AS parent_charity_number,
                r."data"->>'Parent charity country of registration' AS parent_reg_country
        FROM charity_charityraw r
        WHERE spider = 'oscr'
                AND r."data"->>'Regulatory Type' = 'Cross Border'
)
SELECT c.id,
        c."name",
        c.constitution,
        cb.org_id,
        c.income,
        cb.parent_name,
        cb.parent_charity_number,
        cb.parent_reg_country,
        cbe.org_id,
        cbe.linked_orgs
FROM charity_charity c
        INNER JOIN crossborder cb
                ON c.id = cb.org_id
        LEFT OUTER JOIN crossborder_existing cbe
                ON c.id = cbe.org_id
WHERE c.id ILIKE 'GB-SC-%'
        AND cbe.org_id IS NULL
ORDER BY c.income DESC NULLS LAST
"""

df = pd.read_sql(QUERY, DB_URI)
print(df)
