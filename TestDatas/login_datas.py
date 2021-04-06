from TestDatas.common_datas import home_url

# 登录成功
success = {"user":"18684720553","passwd":"python",'check':home_url}

# 手机号为空/密码为空/手机号格式不正确/非数字。。。。
invalid_datas = [
        {"user":"18684720553","passwd":"","check":"请输入密码"},
        {"user": "", "passwd": "python", "check": "请输入手机号"},
        {"user": "1868472055", "passwd": "python", "check": "请输入正确的手机号"}
    ]

# 密码错误 /手机号未注册
invalid_2_datas = [{"user":"18684720559","passwd":"python","check":"此账号没有经过授权，请联系管理员!"},
                   {"user":"18684720553","passwd":"1234567","check":"帐号或密码错误!"}]