select "CompanyNumber",
	"CompanyName",
	"CompanyCategory",
	"IncorporationDate"
from companies_main
where "CompanyCategory" in (
	'Charitable Incorporated Organisation', 
	'Scottish Charitable Incorporated Organisation'
);