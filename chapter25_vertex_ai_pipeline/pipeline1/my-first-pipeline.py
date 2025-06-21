# 앞에 !를 붙이면 명령어가 실행됨
# !pip install kfp --upgrade
# !pip install --upgrade kfp google-cloud-pipeline-components
# !pip install --upgrade google-cloud-aiplatform kfp google-cloud-pipeline-components

import kfp
from kfp import dsl
from kfp.v2 import compiler
from kfp.v2.dsl import component
# from kfp.v2.google.client import AIPlatformClient # ModuleNotFoundError: No module named 'kfp.v2.google'
# from google_cloud_pipeline_components.v1.client import AIPlatformClient # ModuleNotFoundError: No module named 'google_cloud_pipeline_components.v1.client'
from google.cloud import aiplatform  # 핵심: 여기서 모든 것을 관리합니다.

PROJECT_ID = 'khlee-demo'
REGION = 'us-central1'
BUCKET_NAME = 'gs://my-vertex-ai-pipeline'
PIPELINE_ROOT = '{}/pipeline_root1/'.format(BUCKET_NAME)

# 주석 해제하고 사용할 것
# PATH=%env PATH
# %env PATH={PATH}:/home/jupyter/.local/bin

# # deprecated
# @component(output_component_file='add.yaml', base_image='python:3.9')
# def add(a: float, b: float) -> float:
#     return a + b

# # deprecated
# @component(output_component_file='multiply.yaml', base_image='python:3.9')
# def multiply(a: float, b: float) -> float:
#     return a * b

# # deprecated
# @dsl.pipeline(name="my-first-pipeline1", pipeline_root=PIPELINE_ROOT)
# def add_mul_pipeline(a: float = 3, b: float = 5):
#     result = add(a, b)
#     multiply(result.output, b)



# import kfp
# from kfp import dsl
# from google.cloud import aiplatform

# --- 1. 기본 설정 (변경 없음) ---
# PROJECT_ID = "your-gcp-project-id"
# REGION = "us-central1"
# PIPELINE_ROOT = "gs://your-pipeline-root-bucket/add-mul-pipeline"

aiplatform.init(project=PROJECT_ID, location=REGION)


# --- 2. 컴포넌트 정의 (multiply 수정 및 log_result 추가) ---

@dsl.component(base_image="python:3.9")
def add(a: float, b: float) -> float:
    print(f"Adding {a} and {b}")
    result = a + b
    print(f"Result: {result}")
    return result

@dsl.component(base_image="python:3.9")
def multiply(x: float, y: float) -> float:  # ★ 수정: 반환 타입 힌트 추가
    """두 숫자를 곱하고 결과를 반환하는 컴포넌트"""
    print(f"Multiplying {x} and {y}")
    result = x * y
    print(f"Result: {result}")
    return result  # ★ 수정: return 구문 추가

@dsl.component(base_image="python:3.9")
def log_result(value_to_log: float): # ★ 추가: 결과를 확인하기 위한 컴포넌트
    """입력받은 값을 로그로 출력하는 간단한 컴포넌트"""
    print(f"Final calculated result is: {value_to_log}")


# --- 3. 파이프라인 정의 (수정된 부분) ★★★ ---

@dsl.pipeline(
    name="my-full-pipeline-with-outputs",
    pipeline_root=PIPELINE_ROOT
)
def add_mul_pipeline(a: float = 3, b: float = 5):
    add_task = add(a=a, b=b)

    # 이제 multiply_task 객체는 .output 속성을 가집니다.
    multiply_task = multiply(x=add_task.output, y=b)

    # multiply 컴포넌트의 출력을 log_result 컴포넌트의 입력으로 전달합니다.
    log_task = log_result(value_to_log=multiply_task.output) # ★ 추가


# --- 4. 파이프라인 컴파일 및 실행 (변경 없음) ---

compiler = kfp.compiler.Compiler()
compiler.compile(
    pipeline_func=add_mul_pipeline,
    package_path="add_mul_pipeline_final.json"
)

job = aiplatform.PipelineJob(
    display_name="add-mul-pipeline-final-run",
    template_path="add_mul_pipeline_final.json",
    parameter_values={
        'a': 10,
        'b': 20
    }
)

job.submit()

# print(f"Pipeline job submitted. View it in the console: {job.dashboard_uri}")