import time
from celeryapp import app
import random
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)


@app.task
def sleeping(secs_before, secs=1):
    time.sleep(secs)
    secs_and_before = secs + secs_before
    r.set('flat', 0)
    r.set('time', secs_and_before)
    return secs_and_before


@app.task
def wait_for_candle(secs=1):
    # r_int = random.randint(0, 10)
    time.sleep(secs)
    return secs


@app.task
def flatten_paper(secs_before, secs=2):
    time.sleep(secs)
    secs_and_before = refresh_syms_lots(secs_before + secs)
    return secs_and_before


@app.task
def flatten_prod(secs_before):
    secs = random.randint(1, 5)
    time.sleep(secs)
    secs_and_before = refresh_syms_lots(secs_before + secs)
    return secs_and_before


@app.task
def flatten_paper_unchained(secs=2):
    secs_before = int(r.get('time'))
    time.sleep(secs)
    secs_and_before = secs + secs_before
    return secs_and_before


@app.task
def flatten_prod_unchained():
    secs_before = int(r.get('time'))
    secs = random.randint(1, 5)
    time.sleep(secs)
    secs_and_before = secs + secs_before
    return secs_and_before


@app.task
def refresh_syms_lots_unchained(secs_before, secs=3):
    counter = int(r.get('flat'))
    print(f'Counter is: {counter}')
    if counter == 0:
        r.set('flat', 1)
        time.sleep(secs)
        print(f'Sleeping for {secs} seconds')
    elif counter == 1:
        r.set('flat', 0)
        secs = 0
    return secs_before + secs


def refresh_syms_lots(secs_before, secs=3):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    counter = int(r.get('flat'))
    print(f'Counter is: {counter}')
    if counter == 0:
        r.set('flat', 1)
        time.sleep(secs)
        print(f'Sleeping for {secs} seconds')
    elif counter == 1:
        r.set('flat', 0)
        secs = 0
    return secs_before + secs


@app.task
def reducer(list_secs):
    max_time = max(list_secs)
    r.set('time', max_time)
    return max_time


@app.task
def make_step_paper(secs=2):
    secs_before = int(r.get('time'))
    time.sleep(secs)
    secs_and_before = secs + secs_before
    return secs_and_before


@app.task
def make_step_prod():
    secs_before = int(r.get('time'))
    secs = random.randint(1, 5)
    time.sleep(secs)
    secs_and_before = secs + secs_before
    return secs_and_before


@app.task
def refresh_model(secs_before, secs=3):
    counter = int(r.get('flat'))
    print(f'Counter is: {counter}')
    if counter == 0:
        r.set('flat', 1)
        time.sleep(secs)
        print(f'Sleeping for {secs} seconds')
    elif counter == 1:
        r.set('flat', 0)
        secs = 0
    return secs_before + secs

#####################################################

@app.task
def add(*args):
    print('task one begins')
    # sleep 5 seconds
    time.sleep(2)
    print('task one finished')
    return sum(args)


@app.task
def mply(x, y):
    print('task two begins')
    time.sleep(2)
    print('task two finishes')
    return x * y


@app.task
def reduce(numbers):
    print('task three begins')
    time.sleep(2)
    print('task three finishes')
    return sum(numbers)
