# prompt:
# 아래 소스코드를 실행하면 ValueError: Missing key inputs argument! To use the Google AI API, provide (`api_key`) arguments. To use the Google Cloud API, provide (`vertexai`, `project` & `location`) arguments. 이라는 에러 메시지가 발생하는데 어떻게 해결해?
import time

from google import genai
from google.genai.types import CreateBatchJobConfig, JobState, HttpOptions

client = genai.Client(http_options=HttpOptions(api_version="v1"))
# TODO(developer): Update and un-comment below line
# output_uri = "gs://your-bucket/your-prefix"

# See the documentation: https://googleapis.github.io/python-genai/genai.html#genai.batches.Batches.create
job = client.batches.create(
    model="text-embedding-005",
    # Source link: https://storage.cloud.google.com/cloud-samples-data/generative-ai/embeddings/embeddings_input.jsonl
    src="gs://cloud-samples-data/generative-ai/embeddings/embeddings_input.jsonl",
    config=CreateBatchJobConfig(dest=output_uri),
)
print(f"Job name: {job.name}")
print(f"Job state: {job.state}")
# Example response:
# Job name: projects/%PROJECT_ID%/locations/us-central1/batchPredictionJobs/9876453210000000000
# Job state: JOB_STATE_PENDING

# See the documentation: https://googleapis.github.io/python-genai/genai.html#genai.types.BatchJob
completed_states = {
    JobState.JOB_STATE_SUCCEEDED,
    JobState.JOB_STATE_FAILED,
    JobState.JOB_STATE_CANCELLED,
    JobState.JOB_STATE_PAUSED,
}

while job.state not in completed_states:
    time.sleep(30)
    job = client.batches.get(name=job.name)
    print(f"Job state: {job.state}")
    if job.state == JobState.JOB_STATE_FAILED:
        print(f"Error: {job.error}")
        break

# Example response:
# Job state: JOB_STATE_PENDING
# Job state: JOB_STATE_RUNNING
# Job state: JOB_STATE_RUNNING
# ...
# Job state: JOB_STATE_SUCCEEDED