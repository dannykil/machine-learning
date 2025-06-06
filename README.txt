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


