1. 환경설정
1) 해당 가상 환경 활성화
conda activate your_environment_name

2) ipykernel 설치
conda install ipykernel
# 또는
# pip install ipykernel

3) Jupyter 커널로 등록
python -m ipykernel install --user --name=ml_env --display-name "Python (ml_env)"


2. Jupyter Lab 사용팁
1) 자동완성 - tab키

2) 


3. 실습이 없는 Chapter(이론)
Chapter08 - Explore Vertex AI Console


Chapter10 - About Model Garden 


Chapter11 - * Machine Learning Basic 
: Machine Learning Algorithm and Workflow
1) 


Chapter12 - GCP Service for Machine Learning 
: Machine Learning에 사용되는 GCP 제품/서비스(Compute Engine, IAM, Cloud Storage)


Chapter13 - * GCP Product for Machine Learning 
: 언제 어떤 제품/서비스를 사용해야하는가? ML에서 사용 가능한 4가지 제품(ML APIs, AutoML, BigQuery ML, Custom Model)이 각각 어떤 상황에서 사용되는지 확인
1) ML APIs : 모델에 학습시킬 데이터도 없는 상황
2) AutoML  : 모델에 학습시킬 데이터는 있으나 코딩은 할 수 없는 상황
3) Custom Model : 학습시킬 데이터도 있고 코딩도 할 수 있으나 모델 학습을 위한 SQL 작성은 불가한 상황
4) BigQuery ML  : 학습시킬 데이터도 있고 코딩도 할 수 있고 모델 학습을 위한 SQL 작성도 가능한 상황


Chapter14 - ML APIs(Pre Built APIs)
: Rest and RPC API 호출만으로 사용가능(* RPC API에 대해 알아보기)
1) Vision API
2) Natural Language API
3) Speech To Text API
4) Translation API
5) Video API

Chapter15 - Google Vision API
1) Try in browser
https://cloud.google.com/vision/docs/drag-and-drop?hl=ko

2) API Explorer
https://cloud.google.com/vision/docs/detect-labels-image-api?hl=ko

3) Raw Rest API(curl) 
: 영상에서 이슈(인증, API Enable)가 많아 영상이 길어짐
https://cloud.google.com/vision/docs/detect-labels-image-command-line?hl=ko

4) gcloud tool
gcloud ml vision detect-labels gs://cloud-samples-data/vision/using_curl/shanghai.jpeg
gcloud ml vision detect-labels gs://batch_data_embedding/demo-img.jpg
gcloud ml vision detect-faces gs://batch_data_embedding/demo-img.jpg

5) python code(for label detection)


