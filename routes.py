from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from sklearn.externals import joblib
from models import db, User
from forms import UsersForm
from flask import request


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://localhost/student'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/usersdb'
db.init_app(app)

app.secret_key = "e14a-key"

# db= SQLAlchemy()
# class User(db.Model):
# 	__tablename__='student'
# 	user_id = db.Column(db.Integer, nullable=False, autoincrement=True)
# 	first_name =  db.Column(db.String(100), nullable=False)
# 	last_name =  db.Column(db.String(100), nullable=False)
# 	email =  db.Column(db.String(100), primary_key=True, nullable=False)

@app.route("/")
def indef():
	return render_template("index.html")

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
	form = UsersForm()
	if request.method == 'GET':
		return render_template('add_user.html', form=form)
	else:
		if form.validate_on_submit():
			first_name = request.form['first_name']
			age = request.form['age']
			new_user = User(first_name=first_name, age=age)
			db.session.add(new_user)
			db.session.commit()
			return redirect(url_for('index'))

if __name__ == "__main__":
	app.run(debug=True)
