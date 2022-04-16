from flask import Flask
import smtplib
from transliterate import translit

EMAIL = 'email.email.sender@mail.ru'
PW = 'YqDrymDzGmQ1vKf5AGea'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1)!Ak!!!b&(?~t=aMK5-07'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

def send_email(name, msg):
    try:
        server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        server.ehlo()
        server.login(EMAIL, PW)
        message = translit('Subject: {} отправил поздравление\n\n{}'.format(name, msg), 'ru', reversed=1)
        server.sendmail(EMAIL, 's.kolovorotnyy@gmail.com', message)
        server.quit()
    except:
        print("Error")