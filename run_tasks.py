from celery import group, chain

from tasks import *
import time


def run_loop_map_reduce():
    while True:
        t1 = time.time()
        result = (add.s(1, 2) | group(add.s(4), mply.s(5)) | reduce.s()).apply_async()
        sleeeping = result.get()
        print(sleeeping)
        time.sleep(sleeeping)
        print(f'Task finished in {time.time()-t1} seconds')


def run_helloworld():
    result = add.delay(1, 2)
    # at this time, our task is not finished, so it will return False
    print('Task finished? ', result.ready())
    print('Task result: ', result.result)
    # sleep 10 seconds to ensure the task has been finished
    time.sleep(10)
    # now the task should be finished and ready method will return True
    print('Task finished? ', result.ready())
    print('Task result: ', result.result)


def run_mock_trading():
    while True:
        t1 = time.time()
        # result = (wait_for_candle.s() | sleeping.s() | group(flatten_paper.s(), flatten_prod.s()) | reducer.s()).apply_async()
        flatten_refresh_gp = group((flatten_prod_unchained.s() | refresh_syms_lots_unchained.s()),
                                   (flatten_paper_unchained.s() | refresh_syms_lots_unchained.s()))
        make_step_refresh_model_gp = group((make_step_paper.s() | refresh_model.s()), (make_step_prod.s() | refresh_model.s()))
        result = (wait_for_candle.s() |
                  sleeping.s() | flatten_refresh_gp | reducer.s() | make_step_refresh_model_gp | reducer.s()).apply_async()
        print(result.get())
        print(f'Task finished in {time.time()-t1} seconds')


def explore_redis():
    results = (redis_write.si() | redis_read.si()).apply_async()
    print(results.get())


if __name__ == '__main__':
    # run_loop_map_reduce()
    run_mock_trading()
    # explore_redis()
