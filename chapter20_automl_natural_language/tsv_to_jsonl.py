import csv
import json

def tsv_to_jsonl(tsv_filepath, jsonl_filepath):
    """
    TSV 파일의 'review'와 'liked' 헤더를 키로 사용하여 JSONL 파일로 변환합니다.

    Args:
        tsv_filepath (str): 변환할 TSV 파일의 경로.
        jsonl_filepath (str): 저장할 JSONL 파일의 경로.
    """
    try:
        data = []
        with open(tsv_filepath, 'r', newline='', encoding='utf-8') as tsv_file:
            # csv.DictReader를 사용하여 헤더를 자동으로 인식하고 딕셔너리로 읽어옵니다.
            # TSV 파일이므로 delimiter는 '\t'으로 설정합니다.
            tsv_reader = csv.DictReader(tsv_file, delimiter='\t')

            # 헤더에 'review'와 'liked'가 있는지 확인합니다.
            if 'Review' not in tsv_reader.fieldnames or 'Liked' not in tsv_reader.fieldnames:
                raise ValueError("TSV 파일에 'review' 또는 'liked' 헤더가 없습니다. 헤더 이름을 확인해주세요.")

            for row in tsv_reader:
                # 각 행을 {'review': '...', 'liked': '...'} 형태의 딕셔너리로 변환합니다.
                # row는 이미 DictReader에 의해 딕셔너리 형태로 제공됩니다.
                json_object = {
                    'review': row['Review'],
                    'liked': row['Liked']
                }
                data.append(json_object)

        with open(jsonl_filepath, 'w', encoding='utf-8') as jsonl_file:
            for item in data:
                # 각 딕셔너리를 JSON 문자열로 변환하고 한 줄씩 파일에 씁니다.
                jsonl_file.write(json.dumps(item, ensure_ascii=False) + '\n')

        print(f"'{tsv_filepath}'가 성공적으로 '{jsonl_filepath}'로 변환되었습니다.")

    except FileNotFoundError:
        print(f"오류: '{tsv_filepath}' 파일을 찾을 수 없습니다.")
    except ValueError as ve:
        print(f"오류: {ve}")
    except Exception as e:
        print(f"변환 중 오류가 발생했습니다: {e}")

### 사용 예시 및 파일 생성

if __name__ == "__main__":
    input_tsv = "Restaurant_Reviews.tsv"
    output_jsonl = "Restaurant_Reviews.jsonl"

    # 테스트를 위한 TSV 파일 생성 (Restaurant_Reviews.tsv 파일이 없다면 이 부분 실행)
    # try:
    #     with open(input_tsv, 'x', newline='', encoding='utf-8') as f:
    #         f.write("review\tliked\n") # 실제 TSV 파일의 헤더와 일치해야 합니다.
    #         f.write("Wow... Loved this place.\t1\n")
    #         f.write("Crust is not good.\t0\n")
    #         f.write("Not tasty and the texture was just disgusting.\t0\n")
    #         f.write("Every time I go to this place, I order the same thing.\t1\n")
    #         f.write("I am a big fan of their chicken wings, but the service was terrible.\t0\n")
    # except FileExistsError:
    #     pass # 파일이 이미 존재하면 새로 만들지 않음

    # 변환 함수 실행
    tsv_to_jsonl(input_tsv, output_jsonl)

    # 변환된 JSONL 파일 내용 확인 (선택 사항)
    print("\n--- 변환된 JSONL 파일 내용 ---")
    try:
        with open(output_jsonl, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print("출력 JSONL 파일을 찾을 수 없습니다.")