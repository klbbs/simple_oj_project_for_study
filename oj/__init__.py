from flask import Flask

from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

oj = Flask('oj')

oj.config.from_pyfile('settings.py')
oj.jinja_env.trim_blocks = True
oj.jinja_env.lstrip_blocks = True
oj.config.update(DEBUG=True)

db = SQLAlchemy(oj)
bootstrap = Bootstrap(oj)
moment = Moment(oj)


from oj import views, models, commands

