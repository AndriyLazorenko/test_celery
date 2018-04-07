from .celery import app
import time


@app.task
def longtime_add(x, y):
    print('long time task begins')
    # sleep 5 seconds
    time.sleep(15)
    print('long time task finished')
    return x + y
