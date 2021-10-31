from celery import Celery
app = Celery('main', broker='pyamqp://guest@localhost//')
app.conf.result_backend = 'redis://localhost:6379/0'
@app.task
def add(x, y):
    return x + y