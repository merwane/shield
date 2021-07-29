#!/bin/sh

redis-server &
LC_ALL=C.UTF-8 LANG=C.UTF-8 rq worker &
gunicorn main:app -b :8000 --threads 2
