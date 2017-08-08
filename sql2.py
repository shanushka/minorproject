from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/dietician'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Example(db.Model):
	__tablename__ = 'userinput'
	user_id = db.Column('user_id', db.Integer, primary_key=True)
	username = db.Column('username', db.Unicode(30))
	email = db.Column('email', db.Unicode(30))
	weight=db.Column('weight',db.Integer)
	height=db.Column('height',db.Integer)
	age=db.Column('age',db.Integer)
	gender=db.Column('gender',db.String(10))
	activity=db.Column('activity',db.String(30))
	preference=db.Column('preference',db.String(20))

	#def __repr__(self):
		#return '<User %r>' % self.data



examples=Example.query.all()
ex = examples[-1]
# for ex in examples:
# 		print(ex.preference)