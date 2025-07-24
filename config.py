
STR_REDIS_URL = "redis://localhost:6379/0"
STR_SERVER_HOST = "0.0.0.0"
STR_SERVER_PORT = 8080

STR_CLI_USAGE = "qgjob [submit|status] ..."
STR_APPWRIGHT_JOB_STATUS_PENDING = "PENDING"
STR_APPWRIGHT_JOB_STATUS_RUNNING = "RUNNING"
STR_APPWRIGHT_JOB_STATUS_DONE = "DONE"
STR_APPWRIGHT_JOB_STATUS_FAILED = "FAILED"

STR_MSG_SUBMIT_OK = "Job submitted successfully. Job ID: {job_id}"
STR_MSG_STATUS = "Status for Job {job_id}: {status}"
STR_MSG_SERVER_ERROR = "Internal server error"
STR_MSG_INVALID_ARGS = "Invalid arguments"
STR_MSG_JOB_NOT_FOUND = "Job not found"

STR_JOB_QUEUE = "job_queue"
STR_JOB_HASH = "job_hash"
STR_AGENT_STATUS = "agent_status"
STR_AGENT_QUEUE = "agent_queue"
STR_APPWRIGHT_LOG_PREFIX = "[QGJOB] "
STR_ENV_SERVER = "QGJOB_SERVER"
STR_POLL_INTERVAL = 3
STR_MAX_POLL_TRIES = 40
STR_GITHUB_OUTPUT = "##[group]QGJOB OUTPUT\n{msg}\n##[endgroup]"

DICT_TARGETS = {"emulator": "emulator", "device": "device", "browserstack": "browserstack"}
LIST_PRIORITIES = ["low", "medium", "high"]
