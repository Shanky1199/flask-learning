#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=no-member
from flask import Flask
from flask_restful import Resource , Api,reqparse,abort,fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api= Api(app)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///sqlite.db"
db= SQLAlchemy(app)

class TodoModel(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    task= db.Column(db.String(200))
    summary= db.Column(db.String(500))


#db.create_all()

resource_fields ={
    "id" : fields.Integer,
    "task" : fields.String,
    "summary" : fields.String

}


task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str,help="task is required", required=True)
task_post_args.add_argument("summary", type=str,help="Summary is required", required=True)

task_put_args = reqparse.RequestParser()
task_put_args.add_argument("task", type=str)
task_put_args.add_argument("summary", type=str)


class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self,todo_id):
        #return tasks[todo_id]
        task= TodoModel.query.filter_by(id=todo_id).first()
        if not task:
            abort(409, message="sorry")
        return task
    
    @marshal_with(resource_fields)
    def post(self,todo_id):
        args= task_post_args.parse_args()
        task= TodoModel.query.filter_by(id=todo_id).first()
        if task:
            abort(409, message="sorry")
        todo= TodoModel(id=todo_id,task=args["task"],summary=args["summary"])
        db.session.add(todo)
        db.session.commit()
        return todo, 201
        
       # if todo_id in tasks:
            #abort(409, message="not acccepted")
        #tasks[todo_id]= { "task":args["task"], "summary": args["summary"]}
        #return tasks[todo_id]
    @marshal_with(resource_fields)
    def delete(self,todo_id):
        task= TodoModel.query.filter_by(id=todo_id).first()
        db.session.delete(task)
        db.session.commit()
        return task

    @marshal_with(resource_fields)   
    def put(self,todo_id):
        args = task_put_args.parse_args()
        task= TodoModel.query.filter_by(id=todo_id).first()
        if not task:
            abort(409, message="sorry")
        if args["task"]:
            task.task=args["task"]
        if args["summary"]:
            task.summary= args["summary"]
        db.session.commit()
        return task    
       
       


class Todolist(Resource):
    def get(self):
        todos={}
        tasks=TodoModel.query.all()
        for task in tasks:
            todos[task.id]= {"task":task.task,"summary":task.summary}
        return todos
    
    

        
    
    

api.add_resource(Todo,'/task/<int:todo_id>')
api.add_resource(Todolist,'/task')


if __name__=="__main__":
    app.run(debug=True)