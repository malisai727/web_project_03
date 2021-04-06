import pytest

if __name__ == '__main__':
    # pytest.main(['-s','-v','-m','smoke'])

    #运行并生成报告
    pytest.main(['-m','smoke','--html=Outputs/reports/pytest01.html','--alluredir=Outputs/allure'])