# Imp setting
# 1 configure local interpreter for project
# 2.  install required lib
# command pip install selenium pytest pytest-html pytest-xdist allure-pytest openpyxl
# 3. Check Default test runner in setting --> it should be pytest
# 4. Check terminal in setting --> it should be cmd.
import pytest


# Pytest Rules:
# 1.	Configure local interpreter
# 2.	Class Name should have prefix “Test_”
# 3.	Test cases name should start with “test_” or “_test”
# 4.	To run specific folder's test cases
# Command --> pytest
# 5.	To run specific file's test cases
# Command --> pytest "path of the file"
# 6.To show more details in console like test case status use verbose (-v)
# Command --> pytest -v
# 7.To show more details in console like test case status and output use standard output (-s)
# Command -->pytest -s
# 8.To run specific keyword’s test case use –k
# Command -- > pytest –k “keyword”
# 9.For grouping the test cases use –m
# Command 
# •	pytest –m “group_name”
# •	pytest –m “group_name1 and group_name2”
# •	pytest –m “group_name1 or group_name2"
#pytest -v -s -p no:warnings -m "web and regression"

# 10.	For grouping the test cases use –m
# Command 
# •	pytest –m “group_name”
# •	pytest –m “group_name1 and group_name2”
# •	pytest –m “group_name1 or group_name2
# 11.	To run test cases parallely use -n
# Command  pytest –n = number (number = no of worker processor)
# 12.	To generate html report
# Command  pytest --html=”file_name.html”

#-->pytest -v -s -p no:warnings -n=8 --html=Reports/My_report.html

# 13.	To generate  allure report
# •	Command to generate the reports files  pytest –alluredir=”Report_file_path”
# •	Command to generate the reports files  allure serve “Report_file_path”

# pytest -v -s -p no:warnings -n=8 --html=Reports/My_report.html  --alluredir="AllureReports"



class TestClass1:

    @pytest.mark.sanity
    @pytest.mark.math
    def test_sum001(self):
        a = 3
        b = 4
        sum = a + b
        print("sum of a +b is-->" + str(sum))
        if sum == 7:
            assert True
        else:
            assert False

    @pytest.mark.sanity
    @pytest.mark.math
    def test_sub002(self):
        a = 30
        b = 4
        sub = a - b
        print("sub of a - b is-->" + str(sub))
        if sub == 26:
            assert True
        else:
            assert False


