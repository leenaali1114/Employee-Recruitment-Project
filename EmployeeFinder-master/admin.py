from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route('/adminhome',methods=['get','post'])
def adminhome():
	return render_template("adminhome.html")

@admin.route('/adview_users',methods=['get','post'])
def adview_users():
	data={}
	q="select *,concat(first_name,' ',last_name)as NAME from user"
	res=select(q)
	data['us']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		id1=request.args['id1']
	else:
		action=None
	if action=="delete":
		q="delete from login where login_id='%s'"%(id1)
		delete(q)
		q="delete from user where user_id='%s'"%(id)
		delete(q)
		flash("Data Removed...")
		return redirect(url_for('admin.adview_users'))
	return render_template("adminview_users.html",data=data)

@admin.route('/adview_employees',methods=['get','post'])
def adview_employees():
	data={}
	q="select * from employee"
	res=select(q)
	data['emp']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		id1=request.args['id1']
	else:
		action=None
	if action=="delete":
		q="delete from login where login_id='%s'"%(id1)
		delete(q)
		q="delete from employee where employee_id='%s'"%(id)
		delete(q)
		flash("Data Removed...")
		return redirect(url_for('admin.adview_employees'))
	return render_template("adminview_employees.html",data=data)

@admin.route('/viewfeedback',methods=['get','post'])
def viewfeedback():
	data={}
	q="select *,concat(first_name,' ',last_name)as NAME from feedback inner join user using(user_id)"
	res=select(q)
	data['feed']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from feedback where feedback_id='%s'"%(id)
		delete(q)
		flash("Review Removed...")
		return redirect(url_for('admin.viewfeedback'))
	j = 0
	for i in range(1, len(res) + 1):
		if 'submit' + str(i) in request.form:
			reply = request.form['reply' + str(i)]
			q = "UPDATE feedback SET reply='%s' WHERE feedback_id='%s'" % (reply, res[j]['feedback_id'])
			update(q)
			flash("Send Message...")
			return redirect(url_for('admin.viewfeedback'))
		j = j + 1
	return render_template("adminview_feedback.html",data=data)