# Relationships

This folder contains a series of files that demonstrate relationships between different organisations and their identifiers - principally showing that the identifiers are for the same organisation.

Each file should have the following format:

| Column heading | Required | Datatype | Description                                                                                                                                                                        |
| -------------- | :------: | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `org_id_a`     |    ✅    | String   | First Organisation Identifier in [Org-id format](http://org-id.guide/)                                                                                                             |
| `org_id_b`     |    ✅    | String   | Second Organisation Identifier in [Org-id format](http://org-id.guide/)                                                                                                            |
| `relationship` |    ✅    | String   | Relationship type. Normally "sameas". This describes the relationship between `org_id_a` and `org_id_b`, so a value of "parent" means that `org_id_a` is the parent of `org_id_b`. |
| `source`       |    ✅    | String   | Description of the source of the knowledge about the relationship. E.g. "Charity Commission Register of Mergers"                                                                   |
| `valid_from`   |    ❌    | Date     | Date from which this relationship starts. ISO Format.                                                                                                                              |
| `valid_to`     |    ❌    | Date     | Date from which this relationship ends. ISO Format.                                                                                                                                |
| `org_name`     |    ❌    | String   | Name of the organisation. Applies to both identifiers. If this is present then `org_name_a` and `org_name_b` should not be present.                                                |
| `org_name_a`   |    ❌    | String   | Name of the organisation. Applies to organisation identified by `org_id_a`. If this is present then `org_name` should not be present.                                              |
| `org_name_b`   |    ❌    | String   | Name of the organisation. Applies to organisation identified by `org_id_b`. If this is present then `org_name` should not be present.                                              |

Other columns can be present and will be ignored.

## Example

### Charities registered in England & Wales and Scotland

| org_id_a       | org_id_b      | org_name_b                                             |
| -------------- | ------------- | ------------------------------------------------------ |
| GB-SC-SC002327 | GB-CHC-263710 | Shelter, National Campaign for Homeless People Limited |
| GB-SC-SC004252 | GB-CHC-247556 | Sisters Trust                                          |
| GB-SC-SC005117 | GB-CHC-218186 | Leonard Cheshire Disability                            |
| ...            |               |                                                        |
