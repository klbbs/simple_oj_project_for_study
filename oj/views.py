from flask import Flask, render_template
from oj import oj

from oj import db
from oj.models import Problem

@oj.route('/')
def index():
    problems = Problem.query.all()
    return render_template('index.html',problems=problems)