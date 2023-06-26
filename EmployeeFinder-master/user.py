from flask import *
from database import *

user=Blueprint('user',__name__)

@user.route('/userhome',methods=['get','post'])
def userhome():
	data={}
	ids=session['login_id']
	q="select *,concat(first_name,' ',last_name)as NAME from user where login_id='%s'"%(ids)
	res=select(q)
	data['us']=res
	return render_template("userhome.html",data=data)

@user.route('/sendfeedback',methods=['get','post'])
def sendfeedback():
	ids=session['login_id']
	if 'submit' in request.form:
		feed=request.form['feed']
		q="insert into feedback values(null,(select user_id from user where login_id='%s'),'%s','Pending',Curdate())"%(ids,feed)
		insert(q)
		flash("Feedback Added..")
		return redirect(url_for('user.userhome'))
	return render_template('usersend_feedback.html')

@user.route('/viewfeedback',methods=['get','post'])
def viewfeedback():
	data={}
	ids=session['login_id']
	q="select *,concat(first_name,' ',last_name)as NAME from feedback inner join user using(user_id) where login_id='%s'"%(ids)
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
		flash("Feedback Deleted..")
		return redirect(url_for('user.viewfeedback'))
	return render_template('userview_feedback.html',data=data)

@user.route('/my_profile',methods=['get','post'])
def my_profile():
	data={}
	ids=session['login_id']
	q="select *,concat(first_name,' ',last_name)as NAME from user where login_id='%s'"%(ids)
	res=select(q)
	data['us']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		id1=request.args['id1']
	else:
		action=None
	if action=="delete":
		q = "delete from user where user_id='%s'" % (id)
		delete(q)
		q = "delete from login where login_id='%s'"%(id1)
		delete(q)
		flash("Account Removed...")
		return redirect(url_for('public.user_register'))
	if action=="update":
		q="select * from user where user_id='%s'"%(id)
		res=select(q)
		data['updateprt']=res
	if 'update' in request.form:
		fname = request.form['fname']
		lname = request.form['lname']
		gender = request.form['gender']
		address = request.form['address']
		phone = request.form['phone']
		email = request.form['email']
		place = request.form['place']
		q="update user set first_name='%s',last_name='%s',gender='%s',address='%s',phone='%s',email='%s',place='%s' where user_id='%s'"%(fname,lname,gender,address,phone,email,place,id)
		update(q)
		return redirect(url_for('user.my_profile'))
	return render_template('userview_profile.html',data=data)

@user.route('/change_password',methods=['get','post'])
def change_password():
		if 'submit' in request.form:
			username = request.form['username']
			password = request.form['password']
			q = "update login set password='%s' where username='%s'" % (password, username)
			update(q)
			flash("Your password changed..")
			return redirect(url_for('user.my_profile'))
		return render_template('userchange_password.html')

@user.route('/view_employee',methods=['get','post'])
def view_employee():
	data={}
	q="select * from employee"
	res=select(q)
	data['emp']=res
	return  render_template('userview_emplyees.html',data=data)

@user.route('/view_skill',methods=['get','post'])
def view_skill():
	data={}
	id=request.args['id']
	q = "select * from skill inner join employee using(employee_id)where employee_id='%s'" % (id)
	res = select(q)
	data['skil'] = res
	return render_template('userview_skill.html',data=data)

@user.route('/view_reference',methods=['get','post'])
def view_reference():
	data={}
	q="select * from reference inner join employee using(employee_id)"
	res=select(q)
	data['ref']=res
	return render_template('userview_reference.html',data=data)

# @user.route('/usersearch',methods=['get','post'])
# def usersearch():
# 	data={}
# 	if 'submit' in request.form:
# 		name = request.form['name']
# 		q = "select * from skill inner join employee using(employee_id) WHERE  skill.skill_name LIKE '%s'" % (name)
# 		res = select(q)
# 		data['viewsearch'] = res
# 	return render_template('usersearch.html',data=data)

@user.route('/usersearch', methods=['GET', 'POST'])
def usersearch():
    data = {}
    q = "SELECT * FROM skill"
    res = select(q)
    data['pl'] = res
    if request.method == 'POST':
        name = request.form['name']
        q = "SELECT * FROM skill inner join employee using(employee_id) WHERE skill_name LIKE '%{}%'".format(name)
        res = select(q)
        data['viewsearch'] = res
        return redirect(url_for('user.usserach', id=name))
    return render_template("usersearch.html", data=data)


@user.route('/usserach', methods=['GET', 'POST'])
def usserach():
    data = {}
    id = request.args.get('id')
    q = "SELECT * FROM skill inner join employee using(employee_id) WHERE skill_id LIKE '%{}%'".format(id)
    res = select(q)
    data['viewsearch'] = res
    return render_template("serach.html", data=data)


@user.route('/send_jobproposal',methods=['get','post'])
def send_jobproposal():
	id=request.args['id']
	ids=session['login_id']
	if 'submit' in request.form:
		job_title=request.form['job_title']
		job_des=request.form['job_des']
		job_type=request.form['job_type']
		q="insert into job_offer values(null,(select user_id from user where login_id='%s'),'%s','%s','%s','%s','Pending')"%(ids,id,job_title,job_des,job_type)
		insert(q)
		flash("Job Requirement Sended..")
	return render_template('usersend_joboffer.html')

@user.route('/viewjob_status',methods=['get','post'])
def viewjob_status():
	data={}
	ids=session['login_id']
	q="select *,concat(first_name,' ',last_name)as NAME from job_offer inner join user using(user_id) inner join skill using(skill_id) inner join employee using(employee_id) where user.login_id='%s'"%(ids)
	res=select(q)
	data['jo']=res
	return render_template('userview_jobstatus.html',data=data)

@user.route('/work_duration',methods=['get','post'])
def work_duration():
	ids=session['login_id']
	id=request.args['id']
	if 'submit' in request.form:
		work_des=request.form['work_des']
		start_date=request.form['start_date']
		end_date=request.form['end_date']
		work_loc=request.form['work_loc']
		q="insert into work_duration values(null,'%s',(select user_id from user where login_id='%s'),'%s','%s','%s','%s','Pending')"%(id,ids,work_des,start_date,end_date,work_loc)
		insert(q)
		flash("Work Added..")
	return render_template("useraddwork_duration.html")

@user.route('/work_status',methods=['get','post'])
def work_status():
	data={}
	ids=session['login_id']
	id=request.args['id']
	q="select * from work_duration inner join job_offer using(job_id) inner join user on work_duration.user_id=user.user_id inner join skill using(skill_id) inner join employee using(employee_id) where user.login_id='%s' and job_id='%s'"%(ids,id)
	res=select(q)
	data['wo']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=="delete":
		q = "delete from work_duration where work_id='%s'" % (id)
		delete(q)
		flash("Work Canceled...")
		# return redirect(url_for('user.work_status'))
	return render_template("userwork_status.html",data=data)

@user.route('/add_payment',methods=['get','post'])
def add_payment():
	id=request.args['id']
	ids=session['login_id']
	if 'submit' in request.form:
		no_days=request.form['no_days']
		amount=request.form['amount']
		total_amount=int(no_days)*int(amount)
		q="insert into payment values(null,'%s',(select user_id from user where login_id='%s'),'%s','%s','%s','Paid',Curdate())"%(id,ids,no_days,amount,total_amount)
		insert(q)
		flash("Payment Added")
	return render_template("useradd_payment.html")

@user.route('/view_payment',methods=['get','post'])
def view_payment():
	data={}
	id=request.args['id']
	ids=session['login_id']
	q="SELECT *,concat(first_name,' ',last_name)as NAME FROM payment INNER JOIN `user` on payment.user_id=user.user_id INNER JOIN job_offer USING(job_id)INNER JOIN skill USING(skill_id)INNER JOIN employee USING(employee_id)WHERE user.login_id='%s' AND job_id='%s'"%(ids,id)
	res=select(q)
	data['pay']=res
	return render_template("userview_payment.html",data=data)

@user.route('/add_rating',methods=['get','post'])
def add_rating():
	id=request.args['id']
	ids=session['login_id']
	if 'submit' in request.form:
		rate = request.form['rate']
		review = request.form['des']
		q = "insert into rating values(null,(select user_id from user where login_id='%s'),'%s','%s','%s',Curdate(),'pending')"%(ids,id,rate,review)
		insert(q)
		flash("Your Rating Added..")
	return render_template('useradd_rating.html')

@user.route('/view_rating',methods=['get','post'])
def view_rating():
	data={}
	ids=session['login_id']
	id=request.args['id']
	q="select *,concat(first_name,' ',last_name)as NAME from rating inner join user using(user_id) inner join employee using(employee_id) where user.login_id='%s' and employee_id='%s'"%(ids,id)
	res=select(q)
	data['re']=res
	return render_template("userview_rating.html",data=data)