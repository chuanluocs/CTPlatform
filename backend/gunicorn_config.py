# gunicorn_config.py
bind = "0.0.0.0:5000"
workers = 4
timeout = 5000
app_module = "hello:app"