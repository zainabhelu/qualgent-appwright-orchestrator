
import redis
import uuid
from qgjob.config import (
    STR_JOB_QUEUE, STR_JOB_HASH, STR_APPWRIGHT_JOB_STATUS_PENDING,
)

def FInitRedis(str_url):
    rds = redis.Redis.from_url(str_url)
    return rds

def FEnqueueJob(rds, dct_job):
    str_job_id = str(uuid.uuid4())
    dct_job["job_id"] = str_job_id
    dct_job["status"] = STR_APPWRIGHT_JOB_STATUS_PENDING
    rds.hset(STR_JOB_HASH, str_job_id, str(dct_job))
    rds.rpush(STR_JOB_QUEUE, str_job_id)
    return str_job_id

def FGetJob(rds, str_job_id):
    val = rds.hget(STR_JOB_HASH, str_job_id)
    return eval(val) if val else None

def FUpdateJobStatus(rds, str_job_id, str_status):
    dct_job = FGetJob(rds, str_job_id)
    if not dct_job:
        return False
    dct_job["status"] = str_status
    rds.hset(STR_JOB_HASH, str_job_id, str(dct_job))
    return True
