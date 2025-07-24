from flask import Flask, request, jsonify
from qgjob.config import *
from qgjob.queue_manager import FInitRedis, FEnqueueJob, FGetJob

app = Flask(__name__)
rds = FInitRedis(STR_REDIS_URL)

@app.route("/submit", methods=["POST"])
def SubmitJob():
    try:
        dct = request.get_json(force=True)
        required = ["org_id", "app_version_id", "test_path", "priority", "target"]
        if not all(k in dct for k in required):
            return jsonify({"error": STR_MSG_INVALID_ARGS}), 400
        str_job_id = FEnqueueJob(rds, dct)
        return jsonify({"msg": STR_MSG_SUBMIT_OK.format(job_id=str_job_id), "job_id": str_job_id}), 200
    except Exception:
        return jsonify({"error": STR_MSG_SERVER_ERROR}), 500

@app.route("/status/<job_id>", methods=["GET"])
def JobStatus(job_id):
    dct = FGetJob(rds, job_id)
    if not dct:
        return jsonify({"error": STR_MSG_JOB_NOT_FOUND}), 404
    return jsonify({"msg": STR_MSG_STATUS.format(job_id=job_id, status=dct['status']), "job": dct}), 200

if __name__ == "__main__":
    app.run(host=STR_SERVER_HOST, port=STR_SERVER_PORT)
