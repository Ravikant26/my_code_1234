pytest -v -s -p no:warnings -n=8 --html=Reports/My_report.html  --alluredir="AllureReports" -m "CredKart or sanity"

allure serve "AllureReports"
