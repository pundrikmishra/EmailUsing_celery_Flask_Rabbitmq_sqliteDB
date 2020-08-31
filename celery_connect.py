from celery import Celery


# celery = Celery('celery_connect', backend='rpc://', broker='amqp://guest:@localhost:5672//')
# You can also use above single line of code to run run celery worker OR use below code :- but in this it is not working

def make_celery(app):
    celery_app = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery_app.conf.update(app.config)

    class ContextTask(celery_app.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask
    return celery_app
