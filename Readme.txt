 Install all this:-
        pip install flask
        pip install flask_restful
        pip install celery
        pip install flask-mail
        pip install sqlalchemy   #### I you are using sqlite database then install this


         If using rabbitmq as a broker then first install it:-         #### if using celery then you need broker
                pip install rabbitmq       #if using pycharm then inside pycharm open Terminal and write this command
                sudo service rabbitmq-server start # from terminal
                sudo service rabbitmq-server status #from terminal check status
                sudo service rabbitmq-server stop
                if face any problem in installing then install it manually:- https://www.rabbitmq.com/download.html

 To start flask app:-
            python send_email.py

 To start worker run command:-
            celery -A send_email.celery worker --loglevel=info


 If you are using gmail to send email, then first you have to enable less secure apps,
 Go to below link to enable it.
          https://myaccount.google.com/lesssecureapps # Enable or Disable less secure app


 broker='amqp://guest:@localhost:5672//'   ### for rabbitmq
 backend='db+sqlite:///db.sqlite3'         ### Sqlite database as backend
 backend='rpc://'                          ### rabbitmq as backend
 backend='amqp'


For More:-
        https://www.youtube.com/watch?v=jsoC01eMHQA
        https://flask.palletsprojects.com/en/1.1.x/patterns/celery/
        https://pythonhosted.org/Flask-Mail/
        https://www.youtube.com/watch?v=etfECjhaP-g&list=PLXmMXHVSvS-CoYS177-UvMAQYRfL3fBtX&index=33
        https://www.lifewire.com/what-are-the-gmail-smtp-settings-1170854
        https://www.lifewire.com/what-are-the-outlook-com-smtp-server-settings-1170671
        https://www.youtube.com/watch?v=O-IM9wr0F6M
        https://www.youtube.com/watch?v=mP_Ln-Z9-XY
        https://github.com/vprusso/youtube_tutorials/tree/master/utility_scripts/send_email
        https://myaccount.google.com/lesssecureapps?pli=1
        https://docs.python.org/3/library/smtpd.html#
        https://www.youtube.com/watch?v=1Xvb2n17FqU





##########################################################################################################################
##########################################################################################################################
#               THIS MEANS,THE NAME WE ASSIGN TO CELERY,
#               THAT SAME NAME IS USED TO START CELERY WORKER
#               LIKE:-
#                       celery -A YourFileName.SameName worker --loglevel=info
#
#               YourFileName = name of that file in which your celery app is running
#               SameName  =  THE NAME WE ASSIGN TO CELERY
#
# For example in main.py file:-
#      1)       app = Celery('main', broker='amqp://guest:@localhost:5672//', backend='db+sqlite:///db.sqlite3')
#                       Then to start celery worker:-
#                               celery -A main.app worker --loglevel=info
#                                       OR
#                               celery -A main worker --loglevel=info
#      2)        celery = Celery('main', broker='amqp://guest:@localhost:5672//', backend='db+sqlite:///db.sqlite3')
#                       Then to start celery worker:-
#                               celery -A main.celery worker --loglevel=info
#                                       AND NOT use below command
#                               celery -A main worker --loglevel=info      ### do not use this command due to some reason
##########################################################################################################################
##########################################################################################################################
