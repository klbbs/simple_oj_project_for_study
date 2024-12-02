from flask import Flask, render_template, request
from oj import oj

from oj import db
from oj.models import Problem

@oj.route('/', methods=['POST','GET'])
def index():

    page = request.args.get('page',1,type=int)

    problems = Problem.query.paginate(page=page,per_page=10,error_out=False)

    return render_template('index.html',problems=problems)

@oj.route('/problem/<int:id>')
def detail(id):
    problem = Problem.query.get(id)
    if problem is None:
        return "没有找到此id题目"
    return render_template('problem.html',problem=problem)