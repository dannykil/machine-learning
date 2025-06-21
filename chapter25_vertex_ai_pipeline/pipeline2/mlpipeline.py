from kfp import dsl
from kfp.v2 import compiler
from google.cloud import aiplatform

# Vertex AI의 사전 빌드된 컴포넌트들을 임포트합니다.
# v1 경로의 Image 관련 컴포넌트를 사용합니다.
from google_cloud_pipeline_components.v1.dataset import ImageDatasetCreateOp
from google_cloud_pipeline_components.v1.automl.training_job import AutoMLImageTrainingJobRunOp
from google_cloud_pipeline_components.v1.endpoint import EndpointCreateOp, ModelDeployOp

# --- 1. 기본 설정 (사용자 환경에 맞게 수정) ---

# GCP 프로젝트 정보
PROJECT_ID = 'khlee-demo'
REGION = 'us-central1'
BUCKET_NAME = 'gs://my-vertex-ai-pipeline'

# 파이프라인 아티팩트를 저장할 GCS 버킷 경로 (미리 생성 필요)
PIPELINE_ROOT = '{}/pipeline_root2/'.format(BUCKET_NAME)

# 생성될 리소스들의 이름에 사용할 접두사
DISPLAY_NAME_PREFIX = "image"

# 사용할 데이터세트 (공개 Bank Marketing 데이터세트)
GCS_SOURCE_URI = 'gs://automl_images_dataset/datasets' # 이미지 데이터셋 GCS URI

# 이미지 데이터셋 스키마 URI (단일 라벨 이미지 분류용)
# 실제 데이터셋의 종류(단일/다중 라벨 분류, 객체 감지, 분할)에 따라 변경해야 합니다.
IMAGE_SCHEMA_URI = 'gs://google-cloud-aiplatform/schema/dataset/ioformat/image_classification_single_label_io_format_1.0.0.yaml'

# --- 2. 파이프라인 정의 ---
@dsl.pipeline(
    name=f"{DISPLAY_NAME_PREFIX}-e2e-workflow",
    description="A complete E2E ML pipeline using pre-built components.",
    pipeline_root=PIPELINE_ROOT,
)

def mlops_e2e_pipeline(
    project: str = PROJECT_ID,
    display_name: str = DISPLAY_NAME_PREFIX,
    gcs_source: str = GCS_SOURCE_URI,
    # 이미지 스키마 URI를 파이프라인 인자로도 받도록 추가
    import_schema_uri: str = IMAGE_SCHEMA_URI,
):
    """파이프라인의 각 단계를 정의합니다."""

    # Step 1: Creating Dataset
    # GCS의 이미지 데이터셋을 기반으로 Vertex AI Image 데이터세트를 생성합니다.
    dataset_create_task = ImageDatasetCreateOp(
        project=project,
        display_name=f"{display_name}-dataset",
        gcs_source=gcs_source,
        import_schema_uri=import_schema_uri, # 새로 추가된 부분
    )

    # Step 2: Training Model
    # 생성된 이미지 데이터세트를 사용하여 AutoML Image 모델을 학습시킵니다.
    training_task = AutoMLImageTrainingJobRunOp(
        project=project,
        display_name=f"{display_name}-train",
        # 이미지 분류 모델 학습 시 아래 인자들은 일반적으로 사용되지 않습니다.
        # optimization_prediction_type="classification", # 제거
        # optimization_objective="maximize-au-prc",      # 제거
        dataset=dataset_create_task.outputs["dataset"],
    )

    # Step 3: Creating Endpoint
    # 학습된 모델을 배포하기 위한 엔드포인트를 생성합니다.
    endpoint_create_task = EndpointCreateOp(
        project=project,
        display_name=f"{display_name}-endpoint",
    )

    # Step 4: Deployment
    # 학습이 완료된 모델을 생성된 엔드포인트에 배포합니다.
    model_deploy_task = ModelDeployOp(
        model=training_task.outputs["model"],
        endpoint=endpoint_create_task.outputs["endpoint"],
        dedicated_resources_min_replica_count=1,
        dedicated_resources_max_replica_count=1,
        dedicated_resources_machine_type="n1-standard-4",
    )

# --- 3. 파이프라인 컴파일 및 실행 ---
if __name__ == "__main__":
    # 파이프라인을 JSON 파일로 컴파일
    compiler.Compiler().compile(
        pipeline_func=mlops_e2e_pipeline, package_path="mlops_e2e_pipeline.json"
    )

    # Vertex AI 클라이언트 초기화
    aiplatform.init(project=PROJECT_ID, location=REGION)

    # 파이프라인 잡(Job) 생성
    job = aiplatform.PipelineJob(
        display_name=f"{DISPLAY_NAME_PREFIX}-run",
        template_path="mlops_e2e_pipeline.json",
        pipeline_root=PIPELINE_ROOT,
    )

    # 파이프라인 실행 제출
    print("Submitting the MLops pipeline job...")
    job.submit()
    # print(f"Pipeline job submitted. View it in the console: {job.dashboard_uri}")