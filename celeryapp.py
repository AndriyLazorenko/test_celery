from celery import Celery

app = Celery('test_celery',
             broker='amqp://celery:celery@localhost:5672/celery_vhost',
             backend='redis://localhost',
             include=['tasks'])
