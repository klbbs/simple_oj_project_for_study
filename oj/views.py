from flask import Flask, render_template
from oj import oj

from oj import db
from oj.models import Problem

@oj.route('/')
def index():
    problems = Problem.query.all()
    return render_template('index.html',problems=problems)

@oj.route('/problem/<int:id>')
def detail(id):
    problem = Problem.query.get(id)
    if problem is None:
        return "没有找到此id题目"
    return render_template('problem.html',problem=problem)