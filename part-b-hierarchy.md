
## `extract_partb`

Annual Return Detail table. Row for each AR for each registered main charity. 
Contains a row for each year for each charity, with more detailed financial 
information. Charities only have to fill in this information if their income 
is greater than &pound;500,000 in that year.

Field name      | Old Field name		| Data type		| Description                                         | Note
----------------|----------------|---------------|-----------------------------------------------------|--------------------------------
`date_of_extract`			| 			| date | The date that the extract was taken from the main dataset	|  
`organisation_number`			| 			| int | The organisation number for the charity. This is the index value for the charity |
`registered_charity_number`			| `regno`			| int			| The registration number of the registered organisation allocated by the Commission. Note that a main charity and all its linked charities will share the same registered_charity_number    | 
`latest_fin_period_submitted_ind`			| 			| boolean |  Indicates whether the financial data on this line relates to the latest financial data submitted by the charity. (True or False)  | 
`fin_period_order_number`			| 			| int	| A field to aid ordering of the financial data for each charity. (1=Most recent data in the table, 5=Least recent data in the table) | 
`ar_cycle_reference`			| `artype`			| char(4)		| The annual return cycle to which the submission details relate. | 
`fin_period_start_date`			| `fystart`			| datetime		| The start date of the financial period which is detailed for the charity | 
`fin_period_end_date`			| `fyend`			| datetime		| The end date of the financial period which is detailed for the charity. | 
`ar_due_date`			| 			| datetime	| The due date of the annual return which is detailed for the charity | 
`ar_received_date`			| 			| datetime	| The date the annual return was received for the financial period which is detailed for the charity | 
`income_donations_and_legacies`			| `inc_vol`			| numeric		| Income from donations and legacies as entered on the Annual Return form for the financial period detailed | 
`income_charitable_activities`		| `inc_char`		| numeric		| Income received as fees or grants specifically for goods and services supplied by the charity to meet the needs of its beneficiaries for the financial period detailed | 
`income_other_trading_activities`			| `inc_fr`			| numeric		| Income from other trading activity as entered on the Annual Return form for the financial period detailed. | 
`income_investments`		| `inc_invest`		| numeric		| Income from investments including dividends, interest and rents but excluding changes (realised and unrealised gains) in the capital value of the investment portfolio for the financial period detailed. | 
`income_other`		| `inc_other`		| numeric		| Other income. This category includes gains on the disposal of own use assets (i.e. fixed assets not held as investments), but otherwise is only used exceptionally for very unusual transactions that cannot be accounted for in the categories above for the financial period detailed. | 
`income_total_income_and_endowments`		| `inc_total`		| numeric		| Total income including endowments for the financial period detailed.                            | 
`income_legacies`			| `inc_leg`			| numeric		| Income from legacies as entered on the Annual Return form for the financial period detailed | (included in `income_donations_and_legacies`)
`income_endowments`			| `inc_end`			| numeric		| Income from endowments as entered on the Annual Return form for the financial period detailed | (included in `income_donations_and_legacies`)
`expenditure_raising_funds`			| 			| numeric	| Costs associated with providing goods and services to the public, where the main motive is to raise funds for the charity rather than providing goods or services to meet the needs of its beneficiaries for the financial period detailed. (eg charity shops, fundraising dinners etc.). | Combines figures previously separated as `exp_vol` and `exp_trade`
`expenditure_charitable_expenditure`		| `exp_charble`		| numeric		| Costs incurred by the charity in supplying goods or services to meet the needs of its beneficiaries. Grants made to meet the needs of the charity’s beneficiaries for the financial period detailed. |  (includes `expenditure_grants_institution`) 
`expenditure_other`		| `exp_other`		| numeric		| Other expenditure for the financial period detailed. This category is only used very exceptionally for items that don’t fit within one of the categories above | 
`expenditure_total`		| `exp_total`		| numeric		| Total expenditure for the financial period detailed on the Part B of the annual return | 
(No longer reported)			| `exp_vol`			| numeric		| Voluntary income costs                              | From financial year ending 2016 and later, this figure is not reported
(No longer reported) | `exp_trade`		| numeric		| Fundraising Trading costs                           | From financial year ending 2016 and later, this figure is not reported
`expenditure_investment_management`		| `exp_invest`		| numeric		| Expenditure managing investments for the financial period detailed | 
`expenditure_grants_institution`		| `exp_grant`		| numeric		| Any grants that the charity has awarded to other institutions to further their charitable work | 
`expenditure_governance`			| `exp_gov`			| numeric		| Costs associated with running the charity itself for the financial period. (e.g. costs of trustee meetings, internal and external audit costs and legal advice relating to governance matters). | 
`expenditure_support_costs`		| `exp_support`		| numeric		| Support costs should be allocated across activities and are those costs which, while necessary to deliver an activity, do not themselves produce the activity.  They include the central office functions of the charity and are often apportioned to activities.  The amount shown here is the total amount of support costs (for charitable, fundraising and governance activities) included in resources expended. | 
`expenditure_depreciation`			| `exp_dep`			| numeric		| Depreciation charge for the year can be found in the fixed asset analysis notes to the accounts.  This is the amount of depreciation on tangible fixed assets (including impairment charges, if any), which will be shown as the charge for the year in the tangible fixed asset note to the accounts. | 
`gain_loss_investment`		| `invest_gain`		| numeric		| The gain or loss associated with the charity’s investments | 
`gain_loss_pension_fund`	| `pension_gain`	| numeric		| The gain or loss associated with the charity’s pension fund |  
`gain_loss_revaluation_fixed_investment`		| `asset_gain`		| numeric		| The gain or loss associated with any revaluation of fixed assets | 
`gain_loss_other`		| 		| numeric		| The gain or loss associated with any other assets | 
`reserves`		| `reserves`		| numeric		| The level of reserves is those unrestricted funds which are freely available for the charity to spend and can be found in the Financial Review in the Trustees Annual Report and will exclude endowments. | 
(No longer reported)		| `asset_open`		| numeric		| Total fixed assets (at start of year)               | Can be found in `assets_total_fixed` field for previous year
`assets_total_fixed`		| `asset_close`		| numeric		| Total fixed assets. Fixed assets are those held for continuing use and include tangible fixed assets such as land, buildings, equipment and vehicles, and any investments held on a long-term basis to generate income or gains. | 
`assets_own_use`	| 	| numeric		| Total own use assets. This is a calculated field. `assets_own_use` = `assets_total_fixed` – `assets_long_term_investment` | 
`assets_long_term_investment`	| `fixed_assets`	| numeric		| Fixed Asset Investment are held for the long term to generate income or gains and may include quoted and unquoted shares, bonds, gilts, common investment funds, investment property and term deposits held as part of an investment portfolio. | 
(No longer reported)		| `open_assets`		| numeric		| Fixed Investments Assets (start of year)            | Can be found in `assets_long_term_investment` field for previous year
`defined_benefit_pension_scheme`	| `pension_assets`	| numeric		| This is surplus or deficit in any defined benefit pension scheme operated and represents a potential long-term asset or liability. | 
`assets_other_assets`	| 	| numeric		| The value of gross current assets | 
`assets_total_liabilities`	| 	| numeric		| The value of the total liabilities for the charity. This is a calculated field. `assets_total_liabilities` = `creditors_one_year_total_current` + `creditors_falling_due_after_one_year` | 
`assets_current_investment`	| `invest_assets`	| numeric		| Total Current Investemnt Assets are a separate class of Total Current Asset and they are held with intention of disposing of them within 12 months. | 
`assets_total_assets_and_liabilities`	| `total_assets`	| numeric		| Total Net assets or liabilities can be found on the Balance Sheet. This is the total of all assets shown less all liabilities. This should be the same as the Total funds of the charity. | 
`creditors_one_year_total_current`		| `credit_1`		| numeric		| Creditors due within one year are the amounts owed to creditors and include loans and overdrafts, trade creditors, accruals and deferred income and they are payable within one year. | 
`creditors_falling_due_after_one_year`		| `credit_long`		| numeric		| These are the amounts owed to creditors payable after more than one year, with provisions for liabilities and charges.| 
`assets_cash`		| `cash_assets`		| numeric		| Cash at bank and in hand are a separate class of Total Current Assets.  This amount includes deposits with banks and other financial institutions, which are repayable on demand, but excludes bank overdrafts. | 
(No longer reported)	| `current_assets`	| numeric		| Total Current Assets                                | Can be calculated from other fields
`funds_endowment`		| `funds_end`		| numeric		| Endowment funds include the amount of all permanent and expendable endowment funds | 
`funds_unrestricted`	| `funds_unrestrict`	| numeric	| Unrestricted funds include the amount of all funds held for the general purposes of the charity.  This will include unrestricted income funds, designated funds, revaluation reserves and any pension reserve. | 
`funds_restricted`	| `funds_restrict`	| numeric		| Restricted funds include the amount of all funds held that must be spent on the purposes of the charity. | 
`funds_total`		| `funds_total`		| numeric		| Total funds can be found on the Balance Sheet and should be the same as Total net assets/(liabilities). | 
`count_employees`		| `employees`		| numeric		| The number of people that the charity employs | 
(No longer reported)	| `volunteers`		| numeric		| Volunteers                                          | Now in Part A return
`charity_only_accounts`		| `charity_acc`		| boolean		| Indicates if the accounts represent only the charity accounts | 
`consolidated_accounts`		| `cons_acc`		| boolean		| Consolidated accounts bring together the resources of the charity and the subsidiaries under its control in one statement. These subsidiaries may be non-charitable and to exist for purposes that benefit the parent charity e.g. fund-raising. If set to 1 the accounts are consolidated | 

### Part B structure

The Part B table is structured in not the most intuitive way - some categories
are actually subcategories of others. The table below shows the structure of the table:
the categories in higher levels add up to their parents (sometimes with a residual field 
that isn't in the dataset).

\* For records with a financial year ending in 2016 or later, the `exp_trade` (fundraising
trading costs) and `exp_vol` (voluntary income costs) figures are not provided. It's not
possible to derive the individual figures from the rest of the data, but you can work out
the sum of both of them using `exp_total - (exp_other + exp_charble + exp_gov + exp_invest)`.

#### Incoming resources

<table class="docutils">
<thead>
<tr>
<th>level 1</th>
<th>level 2</th>
<th>level 3</th></tr>
</thead>
<tbody>
<tr><td rowspan="7">income_total_income_and_endowments</td><td rowspan="3">income_donations_and_legacies</td><td>income_legacies</td></tr>
<tr><td>income_endowments</td></tr>
<tr><td>(residual [income_donations_and_legacies - (income_legacies + income_endowments)])</td></tr>
<tr><td colspan="2">income_other_trading_activities</td></tr>
<tr><td colspan="2">income_charitable_activities</td></tr>
<tr><td colspan="2">income_investments</td></tr>
<tr><td colspan="2">income_other</td></tr>
</tbody>
</table>

#### Spending

<table class="docutils">
<thead>
<tr>
<th>level 1</th>
<th>level 2</th>
<th>level 3</th></tr>
</thead>
<tbody>
<tr><td rowspan="6">expenditure_total</td><td colspan="2">expenditure_raising_funds</td></tr>
<tr><td colspan="2">expenditure_investment_management</td></tr>
<tr><td rowspan="2">expenditure_charitable_expenditure</td><td>expenditure_grants_institution</td></tr>
<tr><td>(residual [expenditure_charitable_expenditure - expenditure_grants_institution])</td></tr>
<tr><td colspan="2">expenditure_governance</td></tr>
<tr><td colspan="2">expenditure_other</td></tr>
</tbody>
</table>

Spending on support costs (`expenditure_support_costs`) and depreciation (`expenditure_depreciation`) is reported separately.

#### Assets

<table class="docutils">
<thead>
<tr>
<th>level 1</th>
<th>level 2</th>
<th>level 3</th></tr>
</thead>
<tbody>
<tr><td rowspan="8">assets_total_assets_and_liabilities</td><td rowspan="2">assets_total_fixed</td><td>assets_long_term_investment [Fixed Investment Assets]</td></tr>
<tr><td>assets_own_use [Tangible Fixed Assets]</td></tr>
<tr><td rowspan="3">assets_other_assets</td><td>assets_current_investment</td></tr>
<tr><td>assets_cash</td></tr>
<tr><td>(residual [assets_other_assets - (assets_current_investment + assets_cash)])</td></tr>
<tr><td rowspan="2">assets_total_liabilities</td><td colspan="1">creditors_one_year_total_current</td></tr>
<tr><td colspan="1">creditors_falling_due_after_one_year</td></tr>
<tr><td colspan="2">defined_benefit_pension_scheme</td></tr>
</tbody>
</table>

#### Funds

<table class="docutils">
<thead>
<tr>
<th>level 1</th>
<th>level 2</th>
<th>level 3</th></tr>
</thead>
<tbody>
<tr><td rowspan="3">funds_total</td><td colspan="2">funds_endowment</td></tr>
<tr><td rowspan="2">(Income funds)</td><td colspan="1">funds_restricted</td></tr>
<tr><td colspan="1">funds_unrestricted</td></tr>
</tbody>
</table>
