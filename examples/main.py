#!/usr/bin/python3

from fastapp import App

routes = [
    { 'path': '/',      'module': 'app.pages', 'class': 'Home',  'methods': [ 'GET'         ] },
    { 'path': '/login', 'module': 'app.login', 'class': 'Login', 'methods': [ 'GET', 'POST' ] }
]

app = App(routes=routes, host='0.0.0.0', config="config.yaml", port=5002)

app.run()
