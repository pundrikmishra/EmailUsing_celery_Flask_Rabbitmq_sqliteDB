from flask import Flask
from flask_mail import Mail, Message
# from flask_restful import Resource, Api
import config
# from celery_connect import celery
from celery_connect import make_celery


app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://guest:@localhost:5672//'
# app.config['CELERY_RESULT_BACKEND'] = 'rpc://'    # rabbitmq as backend
app.config['CELERY_RESULT_BACKEND'] = 'db+sqlite:///db.sqlite3' ## If you use sqlite database then uncomment this
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True  # also if you write 465 instead of True then also work
# app.config['MAIL_USE_TLS'] =
app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
# app.config['MAIL_DEFAULT_SENDER'] = 'xyz@gmail.com'
# app.config['MAIL_DEBUG'] = app.debug
# app.config['MAIL_MAX_EMAILS'] =
# app.config['MAIL_SUPPRESS_SEND'] =
# app.config['MAIL_ASCII_ATTACHMENTS'] =
celery = make_celery(app)
mail = Mail(app)
# api = Api(app)

# class send_email(Resource):
#     def get(self):
#         try:
#             email.delay()
#             return "Email Send"
#         except:
#             return "Email Failed"


# @app.route('/to_email')
# def send_mail(to_email):
#     email.delay(to_email)
#     return "Email Send"


@app.route('/')
def send_mail():
    # email.delay()
    # return "Email Send"
    try:
        email.delay()
        return "Email Send"
    except:
        return "Email Failed"


@celery.task(name='send_email.email')
def email():
    msg = Message("Hello", sender='xyz@gmail.com', recipients=['xyz@gmail.com'])
    mail.send(msg)
    return "message sent"


# @celery.task(name='send_email.email')
# def email(to_email):
#     msg = Message("Hello", sender='xyz@gmail.com', recipients=[to_email])
#     mail.send(msg)
#     return "message sent"


# api.add_resource(send_email, '/')


if __name__ == '__main__':
    app.run(debug=True)
