from flask import Flask
from public import public
from admin import admin
from employee import employee
from user import user
app=Flask(__name__)
app.secret_key="Hai"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(user,url_prefix='/user')
app.register_blueprint(employee,url_prefix='/employee')
app.run(debug=True,port=5023)