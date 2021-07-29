from rq import Queue
from redis import Redis
from config import RQ_HOST, RQ_PORT

class JobQueue:
    def __init__(self, queue_name='default'):
        self.queue_name = queue_name
        job_backend = Redis(host=RQ_HOST, port=RQ_PORT, db=0)

        self.q = Queue(self.queue_name, connection=job_backend)

    def queue(self):
        return self.q
