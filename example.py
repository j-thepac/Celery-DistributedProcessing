
#Broker =  Queue Tasks (Distibuted Queue : Redis , RabbitMQ)
#Backend = Save Result ( Redis , Mongo ,SQlite ,RabbitMQ ....)
from celery import Celery
import time
app = Celery('tasks', broker='redis://localhost:6379/0',backend='redis://localhost:6379/1')


# app = Celery('tasks', broker='amqps://RabbitMQ_Cloud_@puffin.rmq2.cloudamqp.com/xcxlxzlg',
#              backend='mongodb://localhost:27017/from_celery')

@app.task
def add(x, y):
    time.sleep(3)
    return x + y
