
### extract_partb

Annual Return Detail table. Row for each AR for each registered main charity. 
Contains a row for each year for each charity, with more detailed financial 
information. Charities only have to fill in this information if their income 
is greater than &pound;500,000 in that year.

Field name		| Data type		| Description                                         | Note
----------------|---------------|-----------------------------------------------------|--------------------------------
regno			| int			| registered number of a charity                      | 
artype			| char(4)		| annual return mailing cycle code                    | 
fystart			| datetime		| Charity's financial year start date                 | 
fyend			| datetime		| Charity's financial year end date                   | 
inc_leg			| numeric		| Legacies                                            | (included in `inv_vol`)
inc_end			| numeric		| Endowments                                          | (included in `inv_vol`)
inc_vol			| numeric		| Voluntary Income                                    | 
inc_fr			| numeric		| Activities generating funds                         | 
inc_char		| numeric		| Charitable activities                               | 
inc_invest		| numeric		| Investment income                                   | 
inc_other		| numeric		| Other Income                                        | 
inc_total		| numeric		| Total Incoming resources                            | 
invest_gain		| numeric		| Gains/loss on investments                           | 
asset_gain		| numeric		| Revaluations of fixed assets                        | 
pension_gain	| numeric		| Gains/loss on Pension Fund                          | 
exp_vol			| numeric		| Voluntary income costs                              | From financial year ending 2016 and later, this figure is not reported
exp_trade		| numeric		| Fundraising Trading costs                           | From financial year ending 2016 and later, this figure is not reported
exp_invest		| numeric		| Investment Management costs                         | 
exp_grant		| numeric		| Grants to institutions                              | 
exp_charble		| numeric		| Charitable Activities costs                       |  (includes `exp_grant`) 
exp_gov			| numeric		| Governance costs                                    | 
exp_other		| numeric		| Other resources expended                            | 
exp_total		| numeric		| Total Resources expended                            | 
exp_support		| numeric		| Support costs                                       | 
exp_dep			| numeric		| Depreciation                                        | 
reserves		| numeric		| Reserves                                            | 
asset_open		| numeric		| Total fixed assets (at start of year)               | 
asset_close		| numeric		| Total fixed assets                                  | 
fixed_assets	| numeric		| Fixed Investments Assets                            | 
open_assets		| numeric		| Fixed Investments Assets (start of year)            | 
invest_assets	| numeric		| Current Investment Assets                           | 
cash_assets		| numeric		| Cash                                                | 
current_assets	| numeric		| Total Current Assets                                | 
credit_1		| numeric		| Creditors - within one year                         | 
credit_long		| numeric		| Creditors - Long Term/Provision                     | 
pension_assets	| numeric		| Pension Assets/Liabilities                          | 
total_assets	| numeric		| Total Net Assets/Liabilities                        | 
funds_end		| numeric		| Endowment funds                                     | 
funds_restrict	| numeric		| Restricted funds                                    | 
funds_unrestrict	| numeric	| Unrestricted funds                                  | 
funds_total		| numeric		| Total funds                                         | 
employees		| numeric		| Employees                                           | 
volunteers		| numeric		| Volunteers                                          | 
cons_acc		| char(1)		| Consolidated accounts (True/False)                  | 
charity_acc		| char(1)		| Charity only accounts (True/False)                  | 

#### Part B structure

The Part B table is structured in not the most intuitive way - some categories
are actually subcategories of others. The table below shows the structure of the table:
the categories in higher levels add up to their parents (sometimes with a residual field 
that isn't in the dataset).

\* For records with a financial year ending in 2016 or later, the `exp_trade` (fundraising
trading costs) and `exp_vol` (voluntary income costs) figures are not provided. It's not
possible to derive the individual figures from the rest of the data, but you can work out
the sum of both of them using `exp_total - (exp_other + exp_charble + exp_gov + exp_invest)`.

<table class="docutils">
<thead>
<tr>
<th>level 1</th>
<th>level 2</th>
<th>level 3</th></tr>
</thead>
<tbody>
<tr><td rowspan="7">inc_total</td><td rowspan="3">inc_vol</td><td>inc_leg</td></tr>
<tr><td>inc_end</td></tr>
<tr><td>(residual [inc_vol - inc_leg - inc_end])</td></tr>
<tr><td colspan="2">inc_fr</td></tr>
<tr><td colspan="2">inc_char</td></tr>
<tr><td colspan="2">inc_invest</td></tr>
<tr><td colspan="2">inc_other</td></tr>
<tr><td colspan="3">invest_gain</td></tr>
<tr><td colspan="3">asset_gain</td></tr>
<tr><td colspan="3">pension_gain</td></tr>
<tr><td rowspan="7">exp_total</td><td rowspan="3">(Cost of generating funds)</td><td colspan="1">exp_vol*</td></tr>
<tr><td colspan="1">exp_trade*</td></tr>
<tr><td colspan="1">exp_invest</td></tr>
<tr><td rowspan="2">exp_charble</td><td>exp_grant</td></tr>
<tr><td>(residual [exp_charble - exp_grant])</td></tr>
<tr><td colspan="2">exp_gov</td></tr>
<tr><td colspan="2">exp_other</td></tr>
<tr><td rowspan="8">total_assets</td><td rowspan="2">asset_close</td><td>fixed_assets [Fixed Investment Assets]</td></tr>
<tr><td>(residual [Tangible Fixed Assets])</td></tr>
<tr><td rowspan="3">current_assets</td><td>invest_assets</td></tr>
<tr><td>cash_assets</td></tr>
<tr><td>(possible residual [current_assets - (invest_assets + cash_assets)])</td></tr>
<tr><td colspan="2">credit_1</td></tr>
<tr><td colspan="2">credit_long</td></tr>
<tr><td colspan="2">pension_assets</td></tr>
<tr><td rowspan="3">funds_total</td><td colspan="2">funds_end</td></tr>
<tr><td rowspan="2">(Income funds)</td><td colspan="1">funds_restrict</td></tr>
<tr><td colspan="1">funds_unrestrict</td></tr>
<tr><td colspan="3">asset_open</td></tr>
<tr><td colspan="3">open_assets</td></tr>
<tr><td colspan="3">exp_support</td></tr>
<tr><td colspan="3">exp_dep</td></tr>
<tr><td colspan="3">reserves</td></tr>
<tr><td colspan="3">employees</td></tr>
<tr><td colspan="3">volunteers</td></tr>
</tbody>
</table>
