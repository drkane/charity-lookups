# Fields from the Charity Commission for England and Wales register extract.

An outline of the fields available in the Charity Commission for England and Wales's register download, available from [the full register download files](https://register-of-charities.charitycommission.gov.uk/register/full-register-download).

Tables:

- [Charity](#Charity)
- [CharityAnnualReturnHistory](#CharityAnnualReturnHistory)
- [CharityAreaOfOperation](#CharityAreaOfOperation)
- [CharityARPartA](#CharityARPartA)
- [CharityARPartB](#CharityARPartB)
- [CharityClassification](#CharityClassification)
- [CharityEventHistory](#CharityEventHistory)
- [CharityGoverningDocument](#CharityGoverningDocument)
- [CharityOtherNames](#CharityOtherNames)
- [CharityOtherRegulators](#CharityOtherRegulators)
- [CharityPolicy](#CharityPolicy)
- [CharityPublishedReport](#CharityPublishedReport)
- [CharityTrustee](#CharityTrustee)

## Charity

Main table. Note that "linked" charities are included in this table, the number of actual operating charities is better determined by removing any charities with `linked_charity_number` not equal to 0 (zero).

The `organisation_number` field is used as a foreign key for other tables in the extract.

| Field | Description | 
|-------|-------------|
| organisation_number | The organisation number for the charity. This is the index value for the charity. | 
| registered_charity_number | The registration number of the registered organisation allocated by the Commission. Note that a main charity and all its linked charities will share the same registered_charity_number. | 
| linked_charity_number | A number that uniquely identifies the subsidiary or group member associated with a registered charity. Used for user identification purposes where the subsidiary is known by the parent registration number and the subsidiary number. The main parent charity has a linked_charity_number of 0. | 
| charity_name | The Main Name of the Charity | 
| charity_type | The type of the charity displayed on the public register of charities. Only the main parent charity will have a value for this field (i.e. linked_charity_number=0). | 
| charity_registration_status | The charity registration status indicates whether a charity is registered or removed | 
| date_of_registration | The date the charity was registered with the Charity Commission. | 
| date_of_removal | This is the date the charity was removed from the Register of Charities. This will not necessarily be the same date that the charity ceased to exist or ceased to operate. For non-removed charities the field is NULL. | 
| charity_reporting_status | The current reporting status of the charity | 
| latest_acc_fin_period_start_date | The start date of the latest financial period for which the charity has made a submission. | 
| latest_acc_fin_period_end_date | The end date of the latest financial period for which the charity has made a submission. | 
| latest_income | The latest income submitted by the charity. This is the total gross income submitted on part A of the annual return submission. | 
| latest_expenditure | The latest expenditure submitted by a charity. This is the expenditure submitted on part A of the annual return submission. | 
| charity_contact_address1 | Charity Address Line 1 | 
| charity_contact_address2 | Charity Address Line 2 | 
| charity_contact_address3 | Charity Address Line 3 | 
| charity_contact_address4 | Charity Address Line 4 | 
| charity_contact_address5 | Charity Address Line 5 | 
| charity_contact_postcode | Charity Postcode | 
| charity_contact_phone | Charity Public Telephone Number | 
| charity_contact_email | Charity Public email address | 
| charity_contact_web | Charity Website Address | 
| charity_company_registration_number | Registered Company Number of the Charity as assigned by Companies House. Integer returned as string | 
| charity_insolvent | Indicates if the charity is insolvent. | 
| charity_in_administration | Indicates if the charity is in administration. | 
| charity_previously_excepted | Indicates the charity was previously an excepted charity. | 
| charity_is_cdf_or_cif | Indicates whether the charity is a Common Investment Fund or Common Deposit Fund. | 
| charity_is_cio | Indicates whether the charity is a Charitable Incorporated Organisation. | 
| cio_is_dissolved | Indicates the CIO is to be dissolved. | 
| date_cio_dissolution_notice | Date the CIO dissolution notice expires | 
| charity_activities | The charity activities, the trustees' description of what they do and who they help. | 
| charity_gift_aid | Indicates whether the charity is registered for gift aid with HMRC. True, False, NULL (not known) | 
| charity_has_land | Indicates whether the charity owns or leases any land or buildings. True, False, NULL (not known) | 

## CharityAnnualReturnHistory

| Field | Description | 
|-------|-------------|
| organisation_number | The organisation number for the charity. This is the index value for the charity. | 
| registered_charity_number | The registration number of the registered organisation allocated by the Commission. Note that a main charity and all its linked charities will share the same registered_charity_number. | 
| fin_period_start_date | The start date of the financial period which is detailed for the charity. | 
| fin_period_end_date | The end date of the financial period which is detailed for the charity. | 
| ar_cycle_reference | The annual return cycle to which the submission details relate. | 
| reporting_due_date | The due date of the financial period which is detailed for the charity. | 
| date_annual_return_received | The date the annual return was received for the financial period which is detailed for the charity. | 
| date_accounts_received | The date the charity accounts were received for the financial period which is detailed for the charity. | 
| total_gross_income | The total gross income reported on Part A of the annual return for the financial period detailed. | 
| total_gross_expenditure | The total gross expenditure reported on Part A of the annual return for the financial period detailed. | 
| accounts_qualified | Indicates whether the accounts have a qualified opinion. (True or NULL) | 
| suppression_ind | An indicator of whether the finances for this year are currently suppressed. 1 = Supressed, 0 = not supressed. | 
| suppression_type |  | 

## CharityAreaOfOperation

| Field | Description | 
|-------|-------------|
| organisation_number | The organisation number for the charity. This is the index value for the charity. | 
| registered_charity_number | The registration number of the registered organisation allocated by the Commission. Note that a main charity and all its linked charities will share the same registered_charity_number. | 
| linked_charity_number | A number that uniquely identifies the subsidiary or group member associated with a registered charity. Used for user identification purposes where the subsidiary is known by the parent registration number and the subsidiary number. The main parent charity has a linked_charity_number of 0. | 
| geographic_area_type | The area type for this row | 
| geographic_area_description | The area descriptor for this row | 
| parent_geographic_area_type | The parent area type. For example, if the area type is a country this indicator will be continent | 
| parent_geographic_area_description | The descriptor for the parent area type | 
| welsh_ind |  | 

## CharityARPartA

| Field | Description | 
|-------|-------------|
| organisation_number | The organisation number for the charity. This is the index value for the charity. | 
| registered_charity_number | The registration number of the registered organisation allocated by the Commission. Note that a main charity and all its linked charities will share the same registered_charity_number. | 
| latest_fin_period_submitted_ind | Indicates whether the financial data on this line relates to the latest financial data submitted by the charity. (True or False) | 
| fin_period_order_number | A field to aid ordering of the financial data for each charity. (1=Most recent data in the table, 5=Least recent data in the table) | 
| ar_cycle_reference | The annual return cycle to which the submission details relate. | 
| fin_period_start_date | The start date of the financial period which is detailed for the charity. | 
| fin_period_end_date | The end date of the financial period which is detailed for the charity. | 
| ar_due_date | The due date of the annual return which is detailed for the charity. | 
| ar_received_date | The date the annual return was received for the financial period which is detailed for the charity. | 
| total_gross_income | The total gross income reported on Part A of the annual return for the financial period detailed. | 
| total_gross_expenditure | The total gross expenditure reported on Part A of the annual return for the financial period detailed. | 
| charity_raises_funds_from_public | Indicates if the charity raised funds from the public for the financial period which is detailed for the charity. (True, False or NULL) | 
| charity_professional_fundraiser | Indicates if the charity worked with professional fundraisers for the financial period which is detailed for the charity. (True, False or NULL) | 
| charity_agreement_professional_fundraiser | Indicates if the charity had an agreement with its professional fundraisers for the financial period which is detailed. (True, False or NULL) | 
| charity_commercial_participator | Indicates if the charity worked with commercial participators for the financial period detailed. (True, False or NULL) | 
| charity_agreement_commerical_participator | Indicates if the charity had an agreement with its commercial participators for the financial period detailed. (True, False or NULL) | 
| grant_making_is_main_activity | Indicates if grant making was the main way the charity carried out its purposes for the financial period detailed. (True, False or NULL) | 
| charity_receives_govt_funding_contracts | Indicates if the charity received any income from government contracts for the financial period detailed. (True, False or NULL) | 
| count_govt_contracts | The number of government contracts the charity had for the financial period detailed. | 
| charity_receives_govt_funding_grants | Indicates if the charity received any income from government grants for the financial period detailed. (True, False or NULL) | 
| count_govt_grants | The number of government grants the charity received for the financial period detailed. | 
| income_from_government_contracts | The income the charity received from government contracts for the financial period detailed. | 
| income_from_government_grants | The income the charity received from government grants for the financial period detailed. | 
| charity_has_trading_subsidiary | Indicates if the charity had a trading subsidiary for the financial period detailed. (True, False or NULL) | 
| trustee_also_director_of_subsidiary | Indicates if a trustee was also a director of a trading subsidiary for the financial period detailed. (True, False or NULL) | 
| does_trustee_receive_any_benefit | Indicates if any of the trustees received any remuneration, payments or benefits from the charity other than refunds of legitimate trustee expenses for the financial period detailed. (True, False or NULL) | 
| trustee_payments_acting_as_trustee | Indicates if any trustees received payments for acting as a trustee for the financial period detailed. (True, False or NULL) | 
| trustee_receives_payments_services | Indicates if any trustees received payments for providing services to the charity for the financial period detailed. (True, False or NULL) | 
| trustee_receives_other_benefit | Indicates if any trustees received any other benefit from the charity for the financial period detailed. (True, False or NULL) | 
| trustee_resigned_employment | Indicates if any of the trustees resigned and took up employment with the charity during the financial period detailed. (True, False or NULL) | 
| employees_salary_over_60k | Indicates if any of the charity's staff received total employee benefits of £60,000 or more. (True, False or NULL) | 
| count_salary_band_60001_70000 | Number of staff whose total employment benefits were in this band for the financial period detailed. | 
| count_salary_band_70001_80000 | Number of staff whose total employment benefits were in this band for the financial period detailed. | 
| count_salary_band_80001_90000 | Number of staff whose total employment benefits were in this band for the financial period detailed. | 
| count_salary_band_90001_100000 | Number of staff whose total employment benefits were in this band for the financial period detailed. | 
| count_salary_band_100001_110000 | Number of staff whose total employment benefits were in this band for the financial period detailed. | 
| count_salary_band_110001_120000 | Number of staff whose total employment benefits were in this band for the financial period detailed. | 
| count_salary_band_120001_130000 | Number of staff whose total employment benefits were in this band for the financial period detailed. | 
| count_salary_band_130001_140000 | Number of staff whose total employment benefits were in this band for the financial period detailed. | 
| count_salary_band_140001_150000 | Number of staff whose total employment benefits were in this band for the financial period detailed. | 
| count_salary_band_150001_200000 | Number of staff whose total employment benefits were in this band for the financial period detailed. | 
| count_salary_band_200001_250000 | Number of staff whose total employment benefits were in this band for the financial period detailed. | 
| count_salary_band_250001_300000 | Number of staff whose total employment benefits were in this band for the financial period detailed. | 
| count_salary_band_300001_350000 | Number of staff whose total employment benefits were in this band for the financial period detailed. | 
| count_salary_band_350001_400000 | Number of staff whose total employment benefits were in this band for the financial period detailed. | 
| count_salary_band_400001_450000 | Number of staff whose total employment benefits were in this band for the financial period detailed. | 
| count_salary_band_450001_500000 | Number of staff whose total employment benefits were in this band for the financial period detailed. | 
| count_salary_band_over_500000 | Number of staff whose total employment benefits were in this band for the financial period detailed. | 
| count_volunteers | Number of Volunteers. The trustees' estimate of the number of people who undertook voluntary work in the UK for the charity during the year. The number shown is a head count and not expressed as full-time equivalents. Charities are invited to provide an estimate of volunteer numbers in their Annual Return but are not obliged to do so. Where a number is provided by the charity, including zero, that number is displayed. | 


## CharityARPartB

| Field | Description | 
|-------|-------------|
| organisation_number | The organisation number for the charity. This is the index value for the charity. | 
| registered_charity_number | The registration number of the registered organisation allocated by the Commission. Note that a main charity and all its linked charities will share the same registered_charity_number. | 
| latest_fin_period_submitted_ind | Indicates whether the financial data on this line relates to the latest financial data submitted by the charity. (True or False) | 
| fin_period_order_number | A field to aid ordering of the financial data for each charity. (1=Most recent data in the table, 5=Least recent data in the table) | 
| ar_cycle_reference | The annual return cycle to which the submission details relate. | 
| fin_period_start_date | The start date of the financial period which is detailed for the charity. | 
| fin_period_end_date | The end date of the financial period which is detailed for the charity. | 
| ar_due_date | The due date of the annual return which is detailed for the charity. | 
| ar_received_date | The date the annual return was received for the financial period which is detailed for the charity. | 
| income_donations_and_legacies | Income from donations and legacies as entered on the Annual Return form for the financial period detailed. | 
| income_charitable_activities | Income received as fees or grants specifically for goods and services supplied by the charity to meet the needs of its beneficiaries for the financial period detailed. | 
| income_other_trading_activities | Income from other trading activity as entered on the Annual Return form for the financial period detailed. | 
| income_investments | Income from investments including dividends, interest and rents but excluding changes (realised and unrealised gains) in the capital value of the investment portfolio for the financial period detailed. | 
| income_other | Other income. This category includes gains on the disposal of own use assets (i.e. fixed assets not held as investments), but otherwise is only used exceptionally for very unusual transactions that cannot be accounted for in the categories above for the financial period detailed. | 
| income_total_income_and_endowments | Total income including endowments for the financial period detailed. | 
| income_legacies | Income from legacies as entered on the Annual Return form for the financial period detailed. | 
| income_endowments | Income from endowments as entered on the Annual Return form for the financial period detailed. | 
| expenditure_raising_funds | Costs associated with providing goods and services to the public, where the main motive is to raise funds for the charity rather than providing goods or services to meet the needs of its beneficiaries for the financial period detailed. (eg charity shops, fundraising dinners etc.). | 
| expenditure_charitable_expenditure | Costs incurred by the charity in supplying goods or services to meet the needs of its beneficiaries. Grants made to meet the needs of the charity's beneficiaries for the financial period detailed. | 
| expenditure_other | Other expenditure for the financial period detailed. This category is only used very exceptionally for items that don't fit within one of the categories above. | 
| expenditure_total | Total expenditure for the financial period detailed on the Part B of the annual return. | 
| expenditure_investment_management | Expenditure managing investments for the financial period detailed. | 
| expenditure_grants_institution | Any grants that the charity has awarded to other institutions to further their charitable work. | 
| expenditure_governance | Costs associated with running the charity itself for the financial period. (e.g. costs of trustee meetings, internal and external audit costs and legal advice relating to governance matters). | 
| expenditure_support_costs | Support costs should be allocated across activities and are those costs which, while necessary to deliver an activity, do not themselves produce the activity.  They include the central office functions of the charity and are often apportioned to activities.  The amount shown here is the total amount of support costs (for charitable, fundraising and governance activities) included in resources expended. | 
| expenditure_depreciation | Depreciation charge for the year can be found in the fixed asset analysis notes to the accounts.  This is the amount of depreciation on tangible fixed assets (including impairment charges, if any), which will be shown as the charge for the year in the tangible fixed asset note to the accounts. | 
| gain_loss_investment | The gain or loss associated with the charity's investments | 
| gain_loss_pension_fund | The gain or loss associated with the charity's pension fund | 
| gain_loss_revaluation_fixed_investment | The gain or loss associated with any revaluation of fixed assets | 
| gain_loss_other | The gain or loss associated with any other assets | 
| reserves | The level of reserves is those unrestricted funds which are freely available for the charity to spend and can be found in the Financial Review in the Trustees Annual Report and will exclude endowments. | 
| assets_total_fixed | Total fixed assets. Fixed assets are those held for continuing use and include tangible fixed assets such as land, buildings, equipment and vehicles, and any investments held on a long-term basis to generate income or gains. | 
| assets_own_use | Total own use assets. This is a calculated field. assets_own_use = assets_total_fixed - assets_long_term_investment | 
| assets_long_term_investment | Fixed Asset Investment are held for the long term to generate income or gains and may include quoted and unquoted shares, bonds, gilts, common investment funds, investment property and term deposits held as part of an investment portfolio. | 
| defined_benefit_pension_scheme | This is surplus or deficit in any defined benefit pension scheme operated and represents a potential long-term asset or liability. | 
| assets_other_assets | The value of any other assets | 
| assets_total_liabilities | The value of the total liabilities for the charity. This is a calculated field. assets_total_liabilities = creditors_one_year_total_current + creditors_falling_due_after_one_year | 
| assets_current_investment | Total Current Assets are a separate class of Total Current Asset and they are held with intention of disposing of them within 12 months. | 
| assets_total_assets_and_liabilities | Total Net assets or liabilities can be found on the Balance Sheet. This is the total of all assets shown less all liabilities. This should be the same as the Total funds of the charity. | 
| creditors_one_year_total_current | Creditors due within one year are the amounts owed to creditors and include loans and overdrafts, trade creditors, accruals and deferred income and they are payable within one year. | 
| creditors_falling_due_after_one_year | These are the amounts owed to creditors payable after more than one year, with provisions for liabilities and charges. | 
| assets_cash | Cash at bank and in hand are a separate class of Total Current Assets.  This amount includes deposits with banks and other financial institutions, which are repayable on demand, but excludes bank overdrafts. | 
| funds_endowment | Endowment funds include the amount of all permanent and expendable endowment funds. | 
| funds_unrestricted | Unrestricted funds include the amount of all funds held for the general purposes of the charity.  This will include unrestricted income funds, designated funds, revaluation reserves and any pension reserve. | 
| funds_restricted | Restricted funds include the amount of all funds held that must be spent on the purposes of the charity. | 
| funds_total | Total funds can be found on the Balance Sheet and should be the same as Total net assets/(liabilities). | 
| count_employees | The number of people that the charity employs | 
| charity_only_accounts | Indicates if the accounts represent only the charity accounts | 
| consolidated_accounts | Consolidated accounts bring together the resources of the charity and the subsidiaries under its control in one statement. These subsidiaries may be non-charitable and to exist for purposes that benefit the parent charity e.g. fund-raising. If set to 1 the accounts are consolidated. | 

## CharityClassification

| Field | Description | 
|-------|-------------|
| organisation_number | The organisation number for the charity. This is the index value for the charity. | 
| registered_charity_number | The registration number of the registered organisation allocated by the Commission. Note that a main charity and all its linked charities will share the same registered_charity_number. | 
| linked_charity_number | A number that uniquely identifies the subsidiary or group member associated with a registered charity. Used for user identification purposes where the subsidiary is known by the parent registration number and the subsidiary number. The main parent charity has a linked_charity_number of 0. | 
| classification_code | The code of the classification described in the row | 
| classification_type | The type of the classification. What - What the charity does. How - How the charity helps. Who - Who the charity helps | 
| classification_description | The descriptor of the classification code. | 

## CharityEventHistory

| Field | Description | 
|-------|-------------|
| organisation_number | The organisation number for the charity. This is the index value for the charity. | 
| registered_charity_number | The registration number of the registered organisation allocated by the Commission. Note that a main charity and all its linked charities will share the same registered_charity_number. | 
| linked_charity_number | A number that uniquely identifies the subsidiary or group member associated with a registered charity. Used for user identification purposes where the subsidiary is known by the parent registration number and the subsidiary number. The main parent charity has a linked_charity_number of 0. | 
| charity_name | The Main Name of the Charity | 
| charity_event_order | The order of the event in the charity history. 1 is the earliest event. | 
| event_type | The type of charity event that has occurred. | 
| date_of_event | The date that the event occurred. | 
| reason | The reason that the event occurred. A registration event will not have a reason available. | 
| assoc_organisation_number | The charity id for the charity associated with the charity event. For example, in the case of asset transfer in this is the charity that has transferred the funds into the charity. | 
| assoc_registered_charity_number | The registered charity number for the charity associated with the charity event. For example, in the case of asset transfer in this is the charity that has transferred the funds into the charity. | 
| assoc_charity_name | The charity name of the charity associated with the charity event. For example, in the case of asset transfer in this is the charity that has transferred the funds into the charity. | 

## CharityGoverningDocument

| Field | Description | 
|-------|-------------|
| organisation_number | The organisation number for the charity. This is the index value for the charity. | 
| registered_charity_number | The registration number of the registered organisation allocated by the Commission. Note that a main charity and all its linked charities will share the same registered_charity_number. | 
| linked_charity_number | A number that uniquely identifies the subsidiary or group member associated with a registered charity. Used for user identification purposes where the subsidiary is known by the parent registration number and the subsidiary number. The main parent charity has a linked_charity_number of 0. | 
| governing_document_description | The description of the governing document. Note that this is not the governing document itself but the details of the original document and any subsequent amendments. | 
| charitable_objects | The charitable objects of the charity. | 
| area_of_benefit | The area of benefit of the charity as defined in the governing document. This field can be blank as a charity does not have to define an area of benefit in the governing document. | 

## CharityOtherNames

| Field | Description | 
|-------|-------------|
| organisation_number | The organisation number for the charity. This is the index value for the charity. | 
| registered_charity_number | The registration number of the registered organisation allocated by the Commission. Note that a main charity and all its linked charities will share the same registered_charity_number. | 
| linked_charity_number | A number that uniquely identifies the subsidiary or group member associated with a registered charity. Used for user identification purposes where the subsidiary is known by the parent registration number and the subsidiary number. The main parent charity has a linked_charity_number of 0. | 
| charity_name_id | An id for the other charity name | 
| charity_name_type | The type of other charity name. This can be working name or previous name. | 
| charity_name | The Main Name of the Charity | 

## CharityOtherRegulators

| Field | Description | 
|-------|-------------|
| organisation_number | The organisation number for the charity. This is the index value for the charity. | 
| registered_charity_number | The registration number of the registered organisation allocated by the Commission. Note that a main charity and all its linked charities will share the same registered_charity_number. | 
| regulator_order | A field to aid the ordering of the regulators for the charity. | 
| regulator_name | The name of the regulator. | 
| regulator_web_url | The web URL for the regulator. | 

## CharityPolicy

| Field | Description | 
|-------|-------------|
| organisation_number | The organisation number for the charity. This is the index value for the charity. | 
| registered_charity_number | The registration number of the registered organisation allocated by the Commission. Note that a main charity and all its linked charities will share the same registered_charity_number. | 
| linked_charity_number | A number that uniquely identifies the subsidiary or group member associated with a registered charity. Used for user identification purposes where the subsidiary is known by the parent registration number and the subsidiary number. The main parent charity has a linked_charity_number of 0. | 
| policy_name | The name of the policy that the charity has in place. | 

## CharityPublishedReport

| Field | Description | 
|-------|-------------|
| organisation_number | The organisation number for the charity. This is the index value for the charity. | 
| registered_charity_number | The registration number of the registered organisation allocated by the Commission. Note that a main charity and all its linked charities will share the same registered_charity_number. | 
| linked_charity_number | A number that uniquely identifies the subsidiary or group member associated with a registered charity. Used for user identification purposes where the subsidiary is known by the parent registration number and the subsidiary number. The main parent charity has a linked_charity_number of 0. | 
| report_name | The type of report that has been published in relation to the charity. | 
| report_location | The web URL for the location on the charity commission .gov site where the published report can be located. | 
| date_published | The date that the message on the public register of charities to the report was published. | 

## CharityTrustee

| Field | Description | 
|-------|-------------|
| organisation_number | The organisation number for the charity. This is the index value for the charity. | 
| registered_charity_number | The registration number of the registered organisation allocated by the Commission. Note that a main charity and all its linked charities will share the same registered_charity_number. | 
| linked_charity_number | A number that uniquely identifies the subsidiary or group member associated with a registered charity. Used for user identification purposes where the subsidiary is known by the parent registration number and the subsidiary number. The main parent charity has a linked_charity_number of 0. | 
| trustee_id | The id number of the trustee. | 
| trustee_name | The name of the trustee. | 
| trustee_is_chair | TRUE if the trustee is the Chair. FALSE otherwise. | 
| individual_or_organisation | A flag to denote whether the trustee is an individual or an organisation. O for organisation or P for an individual. | 
| trustee_date_of_appointment | The date of appointment of the trustee for that charity. | 
