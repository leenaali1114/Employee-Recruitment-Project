from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def index():
	return render_template("index.html")

@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		username = request.form['username']
		password = request.form['password']
		q = "select * from login where username='%s' and password='%s'" % (username, password)
		res = select(q)
		if res:
			session['login_id'] = res[0]['login_id']
			if res[0]['usertype'] == "admin":
				flash("Login Successfully")
				return redirect(url_for('admin.adminhome'))
			if res[0]['usertype'] == "Employee":
				flash("Login Successfully")
				return redirect(url_for('employee.emphome'))
			if res[0]['usertype'] == "User":
				flash("Login Successfully")
				return redirect(url_for('user.userhome'))
		else:
			flash("invalid username and password")
	return  render_template("login.html")

@public.route('/user_register',methods=['get','post'])
def user_register():
	if 'submit' in request.form:
		fname = request.form['fname']
		lname = request.form['lname']
		gender=request.form['gender']
		address = request.form['address']
		phone = request.form['phone']
		email = request.form['email']
		place=request.form['place']
		username = request.form['username']
		password = request.form['password']
		q = "select * from login where username='%s' and password='%s'" % (username, password)
		print(q)
		result = select(q)
		if len(result) > 0:
			flash("That username and password is already exist")
		else:
			q = "insert into login values(null,'%s','%s','User')" % (username, password)
			res = insert(q)
			q = "insert into user values(null,'%s','%s','%s','%s','%s','%s','%s','%s')" % (res,fname,lname,gender,address,phone,email,place)
			insert(q)
			flash("Registered Successfully")
	return  render_template("user_register.html")

@public.route('/employee_register',methods=['get','post'])
def employee_register():
	if 'submit' in request.form:
		ename = request.form['ename']
		email = request.form['email']
		edetails=request.form['edetails']
		phone = request.form['phone']
		address=request.form['address']
		username = request.form['username']
		password = request.form['password']
		q = "select * from login where username='%s' and password='%s'" % (username, password)
		print(q)
		result = select(q)
		if len(result) > 0:
			flash("That username and password is already exist")
		else:
			q = "insert into login values(null,'%s','%s','Employee')" % (username, password)
			res = insert(q)
			q = "insert into employee values(null,'%s','%s','%s','%s','%s','%s')"%(res,ename,email,edetails,phone,address)
			insert(q)
			flash("Registered Successfully")
	return  render_template("employee_register.html")

