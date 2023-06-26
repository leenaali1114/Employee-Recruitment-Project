from flask import *
from database import *

employee=Blueprint('employee',__name__)

@employee.route('/emphome',methods=['get','post'])
def emphome():
	data={}
	ids=session['login_id']
	q="select * from employee where login_id='%s'"%(ids)
	res=select(q)
	data['emp']=res
	return render_template("employeehome.html",data=data)

@employee.route('/add_skill',methods=['get','post'])
def add_skill():
	ids=session['login_id']
	if 'submit' in request.form:
		skill_name=request.form['skill_name']
		skill_des=request.form['skill_des']
		skill_exp=request.form['skill_exp']
		q="insert into skill values(null,(select employee_id from employee where login_id='%s'),'%s','%s','%s')"%(ids,skill_name,skill_des,skill_exp)
		insert(q)
		flash("Skill Added")
	return render_template("empadd_skill.html")

@employee.route('/view_skill',methods=['get','post'])
def view_skill():
	data={}
	ids=session['login_id']
	q="select * from skill inner join employee using(employee_id)where login_id='%s'"%(ids)
	res=select(q)
	data['skil']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from skill where skill_id='%s'"%(id)
		delete(q)
		flash("Skill Removed...")
		return redirect(url_for('employee.view_skill'))
	return render_template('empview_skill.html',data=data)

@employee.route('/my_profile',methods=['get','post'])
def my_profile():
	data={}
	ids=session['login_id']
	q="select * from employee where login_id='%s'"%(ids)
	res=select(q)
	data['emp']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		id1=request.args['id1']
	else:
		action=None
	if action=="delete":
		q = "delete from employee where employee_id='%s'" % (id)
		delete(q)
		q = "delete from login where login_id='%s'"%(id1)
		delete(q)
		flash("Account Removed...")
		return redirect(url_for('public.employee_register'))
	if action=="update":
		q="select * from employee where employee_id='%s'"%(id)
		res=select(q)
		data['updateprt']=res
	if 'update' in request.form:
		ename = request.form['ename']
		email = request.form['email']
		edetails = request.form['edetails']
		phone = request.form['phone']
		address = request.form['address']
		q="update employee set emp_name='%s',emp_email='%s',emp_details='%s',emp_phone='%s',emp_address='%s' where employee_id='%s'"%(ename,email,edetails,phone,address,id)
		update(q)
		return redirect(url_for('employee.my_profile'))
	return render_template('empview_myprofile.html',data=data)

@employee.route('/change_password',methods=['get','post'])
def change_password():
		if 'submit' in request.form:
			username = request.form['username']
			password = request.form['password']
			q = "update login set password='%s' where username='%s'" % (password, username)
			update(q)
			flash("Your password changed..")
			return redirect(url_for('employee.my_profile'))
		return render_template('empchange_password.html')

@employee.route('/add_reference',methods=['get','post'])
def add_reference():
	ids=session['login_id']
	if 'submit' in request.form:
		pre_comp=request.form['pre_comp']
		cur_exp=request.form['cur_exp']
		rele_pos=request.form['rele_pos']
		job_loc=request.form['job_loc']
		q="insert into reference values(null,(select employee_id from employee where login_id='%s'),'%s','%s','%s','%s')"%(ids,pre_comp,cur_exp,rele_pos,job_loc)
		insert(q)
		flash("Reference Added...")
	return render_template("empadd_reference.html")

@employee.route('/view_reference',methods=['get','post'])
def view_reference():
	data={}
	ids=session['login_id']
	q="select * from reference inner join employee using(employee_id) where login_id='%s'"%(ids)
	res=select(q)
	data['ref']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q="delete from reference where ref_id='%s'"%(id)
		delete(q)
		flash("Reference Removed...")
		return redirect(url_for('employee.add_reference'))
	return render_template('empview_reference.html',data=data)

@employee.route('/view_offers',methods=['get','post'])
def view_offers():
	data={}
	ids=session['login_id']
	q="select *,concat(first_name,' ',last_name)as NAME from job_offer inner join user using(user_id) inner join skill using(skill_id) inner join employee using(employee_id) where employee.login_id='%s'"%(ids)
	res=select(q)
	data['jo']=res
	if 'id' in request.args:
		id = request.args['id']
		q = "UPDATE job_offer SET job_status='Offer Accepted' WHERE job_id='%s' AND job_status='Pending'" % id
		update(q)
		return redirect(url_for('employee.view_offers'))
	elif 'id1' in request.args:
		id1 = request.args['id1']
		q = "UPDATE job_offer SET job_status='Request Reject' WHERE job_id='%s' AND job_status='Pending'" % id1
		update(q)
		return redirect(url_for('employee.view_offers'))
	return render_template('empview_jobstatus.html',data=data)

@employee.route('/work_status',methods=['get','post'])
def work_status():
	data={}
	ids=session['login_id']
	id=request.args['id']
	q="select *,concat(first_name,' ',last_name)as NAME from work_duration inner join job_offer using(job_id) inner join user on work_duration.user_id=user.user_id inner join skill using(skill_id) inner join employee using(employee_id) where employee.login_id='%s' and job_id='%s'"%(ids,id)
	res=select(q)
	data['wo']=res
	if 'id1' in request.args:
		id1 = request.args['id1']
		q = "UPDATE work_duration SET work_status='Work Accepted' WHERE work_id='%s' AND work_status='Pending'" % id1
		update(q)
		# return redirect(url_for('employee.work_status',id=id))
	elif 'id2' in request.args:
		id2 = request.args['id2']
		q = "UPDATE work_duration SET work_status='Request Reject' WHERE work_id='%s' AND work_status='Pending'" % id2
		update(q)
		# return redirect(url_for('employee.work_status',id=id))
	return render_template("empwork_status.html",data=data,id=id)

@employee.route('/view_payment',methods=['get','post'])
def view_payment():
	data={}
	id=request.args['id']
	ids=session['login_id']
	q="SELECT *,concat(first_name,' ',last_name)as NAME FROM payment INNER JOIN `user` on payment.user_id=user.user_id INNER JOIN job_offer USING(job_id)INNER JOIN skill USING(skill_id)INNER JOIN employee USING(employee_id)WHERE employee.login_id='%s' AND job_id='%s'"%(ids,id)
	res=select(q)
	data['pay']=res
	return render_template("empview_payment.html",data=data)

@employee.route('/view_rating',methods=['get','post'])
def view_rating():
	data={}
	ids=session['login_id']
	q="select *,concat(first_name,' ',last_name)as NAME from rating inner join user using(user_id) inner join employee using(employee_id) where employee.login_id='%s'"%(ids)
	res=select(q)
	data['re']=res
	j = 0
	for i in range(1, len(res) + 1):
		if 'submit' + str(i) in request.form:
			reply = request.form['reply' + str(i)]
			q = "UPDATE rating SET reply='%s' WHERE rating_id='%s'" % (reply, res[j]['rating_id'])
			update(q)
			flash("Send Message...")
			return redirect(url_for('employee.view_rating'))
		j = j + 1
	return render_template("empview_rating.html",data=data)