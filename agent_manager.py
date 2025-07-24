import time
from qgjob.queue_manager import FUpdateJobStatus

def FAgentWorkerLoop(rds, str_target, fn_run_test):
    while True:
        lst_job_ids = rds.lrange(str_target, 0, -1)
        for b_job_id in lst_job_ids:
            str_job_id = b_job_id.decode()
            FUpdateJobStatus(rds, str_job_id, "RUNNING")
            b_ok = fn_run_test()
            if b_ok:
                FUpdateJobStatus(rds, str_job_id, "DONE")
            else:
                FUpdateJobStatus(rds, str_job_id, "FAILED")
            rds.lrem(str_target, 0, b_job_id)
        time.sleep(1)
