from celery import Celery

app = Celery('test_celery',
             broker='amqp://celery:celery@localhost/celery_vhost',
             backend='rpc://',
             include=['test_celery.tasks'])


