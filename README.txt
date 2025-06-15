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

* Let try more of Vision API! (in class)
1) Text from Image
gcloud ml vision detect-text demo-img.jpg
gcloud ml vision detect-text hand_written_text1.jpeg
gcloud ml vision detect-text hand_written_text1.jpeg | grep description
gcloud ml vision detect-text make-the-day-great.jpg
gcloud ml vision detect-text make-the-day-great.jpg | grep description

2) Text from PDF
gcloud ml vision detect-text-pdf gs://batch_data_embedding/detect_text/sample-local.pdf gs://batch_data_embedding/detect_text/sample-local-output.pdf
gcloud ml vision detect-text-pdf gs://batch_data_embedding/detect_text/세금계산서_2504_다스인포텍.pdf gs://batch_data_embedding/detect_text/세금계산서_2504_다스인포텍.pdf


3) Landmark, Logo, Label detection
gcloud ml vision detect-landmarks landmark.jpg
gcloud ml vision detect-landmarks landmark.webp
gcloud ml vision detect-landmarks tajimahal.jpg
gcloud ml vision detect-logos starburks.jpg
gcloud ml vision detect-logos instagram.webp

* 안됨 : logo와 landmark를 확실히 분류해야함
gcloud ml vision detect-logos landmark.jpg

* Label은 해당 이미지에 달린 label을 조회함(*score 확인 - 해당 label과 얼마나 일치하는지)
gcloud ml vision detect-labels landmark.webp
gcloud ml vision detect-labels instagram.webp
gcloud ml vision detect-image-properties honda.webp
gcloud ml vision detect-objects multiple_fruits2.jpg 


Chapter16 - Google Natural Language API
1) Try in browser
2) *gcloud tool
3) API Explorer - Raw Rest API
4) python code

gcloud ml language
gcloud ml language analyze-entities --content='Born in Scranton, Pennsylvania, Biden graduated from the University of Delaware in 1965 and the Syracuse University College of Law in 1968. He was elected to the New Castle County Council in 1970 and the U.S. Senate in 1972. As a senator, Biden chaired the Senate Judiciary Committee and Foreign Relations Committee. He drafted and led passage of the Violent Crime Control and Law Enforcement Act and the Violence Against Women Act. He also oversaw six U.S. Supreme Court confirmation hearings, including contentious hearings for Robert Bork and Clarence Thomas. He opposed the Gulf War in 1991 but voted in favor of the Iraq War Resolution in 2002. Biden ran unsuccessfully for the 1988 and 2008 Democratic presidential nominations. In 2008, Obama chose Biden as his running mate, and he was a close counselor to Obama as vice president. In the 2020 presidential election, Biden selected Kamala Harris as his running mate, and they defeated Republican incumbents Donald Trump and Mike Pence. He became the first president to serve with a female or African American vice president.' > a.out
gcloud ml language analyze-sentiment --content='Born in Scranton, Pennsylvania, Biden graduated from the University of Delaware in 1965 and the Syracuse University College of Law in 1968.' > b.out
gcloud ml language analyze-sentiment --content='You did it, you finally did it! I knew it. That is beautiful.'
gcloud ml language analyze-sentiment --content='How dare you.'
gcloud ml language analyze-sentiment --content='Are you cheating on me? I am going to kill you.'

gcloud ml language analyze-entity-sentiment --content='You have done it. Great job man.'

(구문 분석 - 문법에 대한 내용)
gcloud ml language analyze-syntax 
gcloud ml language analyze-syntax --content='Are you cheating on me? I am going to kill you.' > c.out

gcloud ml language classify-text 
gcloud ml language classify-text --content='Born in Scranton, Pennsylvania, Biden graduated from the University of Delaware in 1965 and the Syracuse University College of Law in 1968.'
gcloud ml language classify-text --content='Drone incidents near nuclear power plants are a nuclear safety hazard, and need to stop, Director General of the International Atomic Energy Agency (IAEA) Rafael Grossi said.'
gcloud ml language classify-text --content='대한민국 제21대 대통령 선거는 대한민국의 제21대 대통령을 선출하는 대한민국의 대통령 선거이다. 선거 결과 더불어민주당의 이재명 후보가 국민의힘 김문수 후보와 개혁신당 이준석 후보를 누르고 대통령에 당선되었다' --language=ko 


Chapter17 - Google Speech To Text, Text To Speech API
1) Try in browser


Chapter18 - Note Google AutoML


Chapter19 - AutoML Vision(콘솔 쉘에서 진행)
https://www.kaggle.com/datasets/hasibalmuzdadid/shoe-vs-sandal-vs-boot-dataset-15k-images
gsutil ls 
gsutil ls gs://automl_images_dataset/datasets
gsutil ls gs://automl_images_dataset/datasets/boot
gsutil ls gs://automl_images_dataset/datasets/shoe
gsutil ls gs://automl_images_dataset/datasets/sandal

* 대용량 푸시 (Large Push - 500MB 허용 및 초기화)
git config --global http.postBuffer 524288000
git config --global --unset http.postBuffer


Chapter20 - AutoML Natural Language


Chapter21 - AutoML with Tabular data


Chapter22 - Custom Training
You have your own dataset.
You want to train your own model.
You have a team of data scientists and they want to write their own algorithm based on
- Scikit Learn, XGBoost
- Tensorflow
- Pytorch Framework

* How to do?
- Spin notebook instance with Vertex AI workbench
- Two ways of Custom Trainig can be done : pre-built/custom container

Dataset for Custom Training 
- Iris Flower dataset
- 4 features : sepal length, sepal width, petal length, petal width
- prediction : 3 types of flowers(setosa, virginica, verci-color)
- 150 samples
- https://www.kaggle.com/datasets/arshid/iris-flower-dataset
- Training : custom container, pre-built container


Chapter23 - Custom Training with Custom Container
- Process of Building Custom container
1) Prepare Dataset - Explore
2) Setup Cloud Storage Bucket
3) Create Notebook instance
4) Upload Data to Bucket
5) Training Code in Scikit Learn/Tensorflow (or any other framework)
6) Make Docker Container from code
7) Push Docker Image to Artifact Registry(Copy Path)
8) Setup Custom Training with Custom Container <<< 이 부분은 정확히 뭘한다는건지 아직 잘 모르겠음
9) Import Model from Bucket to Model Registry <<< 이 부분이 이해가 잘 안됨. 이미지를 Artifact Registry에 업로드 했는데 왜 버킷에서 가져오지?
10) Deploy to Endpoint
11) Test
12) Prediction


1) Prepare Dataset - Explore
2) Setup Cloud Storage Bucket
3) Create Notebook instance
4) Upload Data to Bucket

5) Training Code in Scikit Learn/Tensorflow (or any other framework)
- 강의에서 모델을 export(model.pkl)해서 GCS에 저장했지만 도커 컨테이너를 사용할거라 삭제

6) Make Docker Container from code
- training.ipynb > training.py로 변환(terminal에서 가능 - notebook 생성 시 옵션에 지정함)
> jupyter nbconvert training.ipynb --to python
- Dockerfile, requirements.txt 파일 생성

7) Push Docker Image to Artifact Registry(Copy Path)
7.1) Artifact Registry 생성
7.2) 환경변수 내 이미지 경로 저장
- us-central1-docker.pkg.dev/khlee-demo/custom-training-af
- us-central1-docker.pkg.dev/khlee-demo/custom-training-af/${IMAGE_NAME}:${IMAGE_TAG}
- us-central1-docker.pkg.dev/khlee-demo/custom-training-af/iris_custom:v1
export IMAGE_URI=us-central1-docker.pkg.dev/khlee-demo/custom-training-af/iris_custom:v1 <<< terminal에 입력
7.3) 도커 이미지 생성
docker build -f Dockerfile -t ${IMAGE_URI} ./
7.4) Artifact Registry 업로드
- docker configuration update
gcloud auth configure-docker \
    us-central1-docker.pkg.dev
- docker push
docker push ${IMAGE_URI}

8) Setup Custom Training with Custom Container <<< 이 부분은 정확히 뭘한다는건지 아직 잘 모르겠음
9) Import Model from Bucket to Model Registry <<< 이 부분이 이해가 잘 안됨. 이미지를 Artifact Registry에 업로드 했는데 왜 버킷에서 가져오지?
10) Deploy to Endpoint
- Test your model
{
"instances": [
[5.0, 3.6, 1.4, 0.2], 
[10.0, 3.6, 1.4, 0.2], 
[10.0, 3.6, 1.4, 10.2]
]
}

- Sample Request
* Notebook에서 진행하며 INPUT-JSON 파일 생성하여 위 json 데이터 저장
ENDPOINT_ID="895421378939846656"
PROJECT_ID="842505830814"
INPUT_DATA_FILE="INPUT-JSON"

curl \
-X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://us-central1-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/us-central1/endpoints/${ENDPOINT_ID}:predict" \
-d "@${INPUT_DATA_FILE}"

11) Test

12) Prediction
12.1) Online Prediction(지금까지 한 것들 - endpoint가 Online Prediction에 생성되어 있음)
- 결과를 즉각적으로 확인해야하는 경우
- 모델이 배포되어야함
12.2) Batch Prediction
- 비동기로 진행
- 즉각적인 예측이 필요없는 경우(왜?)
- 모델을 배포할 필요 없음
- 한 번에 예측할 양이 많은 경우


Chapter24 - Custom Training with PreBuilt Container
1) Dataset - Explore
2) Setup Cloud Storage Bucket
3) Create Notebook Instance 
4) Upload Data to Bucket

5) Training Code in sklearn(x)/tensorflow(o) (or any other framework)
jupyter nbconvert train.ipynb --to python

6) need 3 files - train.py, setup.py, __init__.py
python setup.py sdist --formats=gztar

7) Setup Custom Training with PreBuilt Container 
8) Import Model from Bucket to Model Registry
9) Deploy to Endpoint(15~20분 걸림)
10) Prediction

+ input과 output path를 인자로 받을 수 있도록 변경(train.py)
- setup.py 파일 내 버전 변경
python setup.py sdist --formats=gztar
gsutil cp dist/trainer-0.2.tar.gz gs://training_prebuilt_container/

--input_data=gs://training_prebuilt_container/IRIS.csv
--mod_out=gs://training_prebuilt_container/model_output_with_args


* [중요] prebuilt, custom container은 언제 사용하는가?
>>> 실행환경을 직접 구성해야하는 경우 = custom container
prebuilt container는 머신러닝을 위해 필요한 기본적인 패키지(ex. pytorch or tensorflow 등)가 설치된 환경을 제공한다면 
custom container는 직접 컨테이너 환경에 필요한 머신러닝 및 회사에서 자체 개발한 패키지를 설치하여 환경을 구성할 수 있음.
