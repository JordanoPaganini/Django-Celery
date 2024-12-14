from celery import shared_task
from time import sleep

@shared_task
def task1():
    sleep(15)
    print('Hello, World!')