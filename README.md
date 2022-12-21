# Celery Flask example

- Process long running tasks in the background

## Clone
```
git clone https://github.com/chrisjsimpson/celery-flask-example-redis.git
```

## Start flask
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=main
export FLASK_DEBUG=1
flask run
```

## Install redis:
https://redis.io/topics/quickstart

## Start redis
Use docker or podman to start a quick redis container
```
podman run --rm --network=host redis
```
 or
```
docker run --rm --network=host redis
```

## Start Celery
In a new terminal
```
. venv/bin/activate

celery -A main worker --loglevel=info -P threads
```

Visit http://127.0.0.1:5000

### Observe task output
```
(venv) $ celery -A main worker --loglevel=info -P threads
 
 -------------- celery@
--- ***** ----- 
- *** --- * --- 
- ** ---------- [config]
- ** ---------- .> app:         main:0x7f18cf888a90
- ** ---------- .> transport:   redis://localhost:6379//
- ** ---------- .> results:     redis://localhost:6379/
- *** --- * --- .> concurrency: 8 (thread)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . main.add_togeather

[2021-06-17 17:45:03,384: INFO/MainProcess] Connected to redis://localhost:6379//
[2021-06-17 17:45:03,390: INFO/MainProcess] mingle: searching for neighbors
[2021-06-17 17:45:04,407: INFO/MainProcess] mingle: all alone
[2021-06-17 17:45:04,439: INFO/MainProcess] celery@ ready.
[2021-06-17 17:45:04,443: INFO/MainProcess] Task main.add_togeather[b8ba4a6e-717c-4fa7-8e75-11129b4414b8] received
[2021-06-17 17:45:07,694: INFO/MainProcess] Task main.add_togeather[4649295d-4373-4222-93e9-5829d64a6bb6] received
[2021-06-17 17:45:09,474: INFO/MainProcess] Task main.add_togeather[b8ba4a6e-717c-4fa7-8e75-11129b4414b8] succeeded in 5.029980767998495s: 10
[2021-06-17 17:45:10,448: INFO/MainProcess] Task main.add_togeather[b4e17a5a-4187-4446-9894-33197df734d2] received
[2021-06-17 17:45:12,699: INFO/MainProcess] Task main.add_togeather[4649295d-4373-4222-93e9-5829d64a6bb6] succeeded in 5.004405617000884s: 10
[2021-06-17 17:45:15,461: INFO/MainProcess] Task main.add_togeather[b4e17a5a-4187-4446-9894-33197df734d2] succeeded in 5.012906424992252s: 10
```



