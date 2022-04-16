from flask import Blueprint, render_template, request, flash

from website import send_email

auth = Blueprint('auth', __name__)

@auth.route('/send')
def send():
    return render_template('sendbox.html')

@auth.route('/end', methods=['GET', 'POST'])
def about_us():
    name = request.form.get('name')
    msg = request.form.get('message')
    if msg:
        if name == '': name = 'anonymus'
        send_email(name, msg)
    return render_template('end.html')