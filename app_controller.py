import os
import time
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, current_user, logout_user
from flask_socketio import SocketIO, join_room, leave_room, send

from wtform_fields import *
from models import *

app = Flask(__name__)
app.secret_key=os.environ.get('SECRET_KEY')

@app.route("/", methods=['GET', 'POST'])
def index():
	return 'I am alive'

if __name__ == "__main__":
	app.run(debug=True)