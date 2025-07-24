
from collections import defaultdict
from qgjob.config import STR_JOB_QUEUE, STR_JOB_HASH

def FGroupJobsByAppVersion(rds):
    lst_job_ids = rds.lrange(STR_JOB_QUEUE, 0, -1)
    dct_groups = defaultdict(list)
    for b_job_id in lst_job_ids:
        dct_job = eval(rds.hget(STR_JOB_HASH, b_job_id.decode()))
        dct_groups[dct_job["app_version_id"]].append(dct_job)
    return dct_groups

def FAssignJobsToAgents(rds, dct_groups):
    dct_agent_queues = defaultdict(list)
    for app_version, jobs in dct_groups.items():
        for job in jobs:
            dct_agent_queues[job["target"]].append(job)
    return dct_agent_queues
