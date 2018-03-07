# Testing framework
for Ultrabear api testing

## 工程目录
```
.
├── __init__.py
├── api.py
├── cases.py
├── main.py
├── testing.py
└── README.MD
```

### api.py

用 `requests` 封装的 api 接口，目前只封装了 `domain/auth` 下的接口，包括
- Register
- Login
- Signup
- AddID
- SetRole

### testing.py

测试项目，包括
- timing: 运行时间
- http_code_testing: http code 是否为200
- result_should_be: 结果是否符合预期
- api_testing: 判断是否通过测试

以 decorator 修饰用例函数。

### cases.py

测试用例。
