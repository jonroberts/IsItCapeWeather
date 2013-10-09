#!./venv/bin/python
# -*- coding: utf-8 -*-

'''
This script is used to launch capeweather.

Application initialization should go here.

'''

from flask import Flask

from capeweather import app # the app is created here
from capeweather.config import AppConfig
from capeweather.controllers import * # register the controllers with Flask
from capeweather.model import * # register any model (e.g. database) classes

config = AppConfig() # get access to configuration information

# register Flask modules (if any) here
#app.register_module(xxx)

app.run(debug=config.debugMode)
#app.run(host='0.0.0.0')

