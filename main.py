from flask import Flask
from celery import Celery


def make_celery(flask_app):
    celery = Celery(
        flask_app.import_name,
        result_backend=flask_app.config["RESULT_BACKEND_CELERY"],
        broker=flask_app.config["CELERY_BROKER_URL"],
    )
    celery.conf.update(flask_app.config)

    return celery


flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL="redis://localhost:6379",
    RESULT_BACKEND_CELERY="redis://localhost:6379",
)

celery = make_celery(flask_app)


@celery.task()
def add_togeather(a, b):
    from time import sleep

    sleep(5)
    return a + b


@flask_app.route("/")
def hello_world():
    add_togeather.delay(5, 5)
    return "Hello world"
