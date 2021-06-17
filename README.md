# Celery Flask example

- Process long running tasks in the background

## Start flask
```
python3 -m venv vev
. venv/bin/activate
pip install -r requirementst.txt
export FLASK_APP=main
export FLASK_DEBUG=1
```

## Install redis:
https://redis.io/topics/quickstart

## Start Celery

```
celery -A main worker --loglevel=info -P threads
```

Visit http://127.0.0.1:5000



