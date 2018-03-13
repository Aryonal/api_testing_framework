# Testing framework
for Ultrabear api testing

## 工程目录
```
.
├── api
│   ├── assets.py
│   ├── auth.py
│   └── __init__.py
├── cases.py
├── __init__.py
├── main.py
├── README.MD
└── testing.py

2 directories, 9 files

```

### api

```python
import api
```

用 `requests` 封装的 api 接口，目前只封装了 `domain/auth` 与 `domain/assets` 下的接口，包括
- auth
    - Register
    - Login
    - Signup
    - AddID
    - SetRole
- assets
    - project_detail_by_id
    - custom_detail_by_name
    - custumes_list
    - get_asset_with_md5_url
    - sounds_list
    - backdrops_list
    - sound_detail_by_name
    - user_projects_list
    - projects_list
    - backdrop_detail_by_name
    - upload_custume
    - upload_sound
    - upload_backdrops
    - duplicate_project
    - upload_project

### testing.py

测试项目，包括
- timing: 运行时间
- http_code_testing: http code 是否为200
- result_should_be: 结果是否符合预期
- api_testing: 判断是否通过测试

以 decorator 修饰用例函数。

### cases.py

测试用例。
