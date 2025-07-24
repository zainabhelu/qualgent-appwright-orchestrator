import sys
import json
import os
import time
import requests
from qgjob.config import *

def FGetServerURL():
    str_env = os.environ.get(STR_ENV_SERVER)
    if str_env:
        return str_env
    return f"http://localhost:{STR_SERVER_PORT}"

def FSubmitJob(dct_args):
    try:
        resp = requests.post(FGetServerURL() + "/submit", json=dct_args)
        resp.raise_for_status()
        print(resp.json()["msg"])
        return resp.json()["job_id"]
    except Exception as e:
        print(STR_APPWRIGHT_LOG_PREFIX + str(e))
        sys.exit(1)

def FGetJobStatus(str_job_id):
    try:
        resp = requests.get(FGetServerURL() + f"/status/{str_job_id}")
        resp.raise_for_status()
        print(resp.json()["msg"])
        return resp.json()["job"]["status"]
    except Exception as e:
        print(STR_APPWRIGHT_LOG_PREFIX + str(e))
        sys.exit(1)

def FMain():
    argv = sys.argv
    if len(argv) < 2:
        print(STR_CLI_USAGE)
        sys.exit(1)
    if argv[1] == "submit":
        dct = {}
        for i, arg in enumerate(argv):
            if arg.startswith("--"):
                dct[arg[2:].replace("-", "_")] = argv[i+1]
        required = ["org_id", "app_version_id", "test", "priority", "target"]
        if not all(k in dct for k in required):
            print(STR_MSG_INVALID_ARGS)
            sys.exit(1)
        dct["test_path"] = dct.pop("test")
        FSubmitJob(dct)
    elif argv[1] == "status":
        if len(argv) < 3:
            print(STR_MSG_INVALID_ARGS)
            sys.exit(1)
        FGetJobStatus(argv[2])
    else:
        print(STR_CLI_USAGE)
        sys.exit(1)

if __name__ == "__main__":
    FMain()
