## Celery tests

#### Installation 

```pip install "celery[librabbitmq,redis]"```

#### Setting up message broker (RabbitMQ)

https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html

#### Setting up backend (Redis)

https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html

#### Setting up workers
Before running a workflow on Celery, one needs to switch on Celery
with workers in a separate terminal. 

In a terminal, proceed to project
folder. Then, activate respective conda environment. Then, execute:
```
celery -A tasks worker --loglevel=info
```
This will create workers based on tasks.

#### Setting up monitoring
Before running a workflow on Celery, it is advised to switch on monitoring
for fancy task visualizations (including statuses, results, time, etc)

In a terminal, proceed to project
folder. Then, activate respective conda environment. Then, execute: 
```
celery -A tasks flower
```

#### Running the project

To run the project execute 

```
run_tasks.py
```

