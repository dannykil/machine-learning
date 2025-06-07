# 1. Cloud Storage 버킷 경로 설정 (당신의 버킷 경로로 수정하세요!)
GCS_BUCKET_PATH="gs://automl_images_dataset/datasets"

# 2. CSV 파일 이름 설정
OUTPUT_CSV_FILE="automl_dataset.csv"

# 3. Cloud Storage에서 파일 목록을 가져와서 CSV 형식으로 변환
#    - 'gsutil ls' 로 파일 목록을 가져옵니다.
#    - 'awk' 를 사용하여 각 줄을 파싱하고 CSV 형식으로 변환합니다.
#      - FILENAME (전체 GCS 경로)에서 라벨을 추출합니다.
#      - 용도는 'TRAINING'으로 고정합니다. 필요에 따라 'VALIDATION', 'TEST' 등을 사용할 수 있습니다.
#    - '> $OUTPUT_CSV_FILE' 로 결과를 파일에 저장합니다.

# gsutil ls "$GCS_BUCKET_PATH"**/*.jpg | awk -F'/' '{print "TRAINING," $0 "," $(NF-1)}' > "$OUTPUT_CSV_FILE"
gsutil ls "$GCS_BUCKET_PATH"**/*.* | awk -F'/' '{print "TRAINING," $0 "," $(NF-1)}' > "$OUTPUT_CSV_FILE"

# 파일의 첫 줄에 헤더를 추가하려면 (선택 사항)
# echo "USE_CASE,IMAGE_PATH,LABEL" | cat - "$OUTPUT_CSV_FILE" > temp && mv temp "$OUTPUT_CSV_FILE"

GCS_BUCKET_PATH="gs://automl_images_dataset/datasets"
OUTPUT_CSV_FILE="automl_dataset.csv"
gsutil ls "$GCS_BUCKET_PATH"/**/*.* | awk -F'/' '{print $0 "," $(NF-1)}' > "$OUTPUT_CSV_FILE"