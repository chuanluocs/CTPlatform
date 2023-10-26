# CTPlatform后端部分
在开始工作之前，请按照以下步骤激活相应的虚拟环境：

使用以下命令激活虚拟环境：
```
$ . venv/bin/activate
```

接下来，设置必要的环境变量并运行后端服务：

导出 FLASK_APP 环境变量：
```
export FLASK_APP=hello.py
```

使用 Flask 命令运行后端：
```
flask run
```

如果您打算部署后端服务，您可以使用 gunicorn 命令进行部署：

使用 gunicorn 部署后端命令：
```
gunicorn -b 0.0.0.0:5000 hello:app
```

这些步骤将使您能够在本地开发和部署 CTPlatform 的后端部分。确保您已按照上述步骤正确设置和运行后端。