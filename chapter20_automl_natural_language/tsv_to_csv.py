# 파이썬으로 작성된 아래 소스코드를 실행하면 csv 파일이 생성되는데 tsv파일에 쌍따옴표가 없는데 csv로 변환하면 어떤 문장은 쌍따옴표가 생기고 어떤 문장은 없는 현상이 발생하고 있어. 왜그런지 알아?
import csv

def tsv_to_csv(tsv_filepath, csv_filepath):
    """
    TSV 파일을 CSV 파일로 변환합니다.

    Args:
        tsv_filepath (str): 변환할 TSV 파일의 경로.
        csv_filepath (str): 저장할 CSV 파일의 경로.
    """
    with open(tsv_filepath, 'r', newline='', encoding='utf-8') as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter='\t')

        # 첫 번째 행(헤더)을 건너뜁니다.
        next(tsv_reader, None)

        with open(csv_filepath, 'w', newline='', encoding='utf-8') as csv_file:
            # csv_writer = csv.writer(csv_file, delimiter=',')
            # csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE) # 여기가 중요!
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            # csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for row in tsv_reader:

                if row:  # 빈 행이 아닌지 확인
                    # 첫 번째 열(인덱스 0)의 텍스트 처리
                    original_text = row[0]

                    # 텍스트 내의 모든 쌍따옴표(")를 홀따옴표(')로 바꿉니다.
                    # 홀따옴표(')는 그대로 유지됩니다.
                    processed_text = original_text.replace('"', "'")

                    # 수정된 텍스트를 첫 번째 열에 다시 할당합니다.
                    row[0] = processed_text

                csv_writer.writerow(row)
                
    print(f"'{tsv_filepath}'가 성공적으로 '{csv_filepath}'로 변환되었습니다.")

# 사용 예시
if __name__ == "__main__":
    input_tsv = "Restaurant_Reviews.tsv"
    output_csv = "Restaurant_Reviews.csv"

    tsv_to_csv(input_tsv, output_csv)

    # 변환된 CSV 파일 내용 확인 (선택 사항)
    with open(output_csv, 'r', encoding='utf-8') as f:
        print("\n변환된 CSV 파일 내용:")
        print(f.read())