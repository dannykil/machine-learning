from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials

api_key_path = "/Users/danniel.kil/Downloads/khlee-demo-8af60a965548.json"

credentials = Credentials.from_service_account_file(
    api_key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

PROJECT_ID = "khlee-demo"
REGION = "us-central1"
# REGION = "global"

import vertexai

vertexai.init(project=PROJECT_ID, location=REGION, credentials=credentials)


import markdown
from IPython.display import display, HTML

def displayMD(llmtext):

    html_output = markdown.markdown(llmtext)
    
    custom_css = """
    /* 기본 스타일 초기화 (선택 사항) */
        body {
          margin: 0;
          padding: 0;
          font-family: sans-serif; /* 기본 글꼴 설정 */
          line-height: 1.6; /* 기본 줄 간격 설정 */
          color: #333; /* 기본 글자 색상 설정 */
          background-color: #f4f4f4; /* 기본 배경 색상 설정 */
        }
        
        /* body 태그 스타일 */
        body {
          padding: 20px; /* 전체 페이지 여백 */
        }
        
        /* h1 태그 스타일 */
        h1 {
          font-size: 2.5em; /* 글자 크기 */
          font-weight: bold; /* 글자 굵게 */
          color: #2c3e50; /* 제목 글자 색상 */
          margin-top: 0; /* 위쪽 여백 제거 */
          margin-bottom: 20px; /* 아래쪽 여백 설정 */
          border-bottom: 2px solid #3498db; /* 아래 테두리 */
          padding-bottom: 10px; /* 아래쪽 패딩 */
        }
        
        /* h2 태그 스타일 */
        h2 {
          font-size: 2em;
          font-weight: semi-bold; /* 약간 굵게 */
          color: #34495e;
          margin-top: 30px;
          margin-bottom: 15px;
          border-bottom: 1px solid #95a5a6;
          padding-bottom: 5px;
        }
        
        /* h3 태그 스타일 */
        h3 {
          font-size: 1.7em;
          font-weight: normal; /* 보통 굵기 */
          color: #4a6572;
          margin-top: 25px;
          margin-bottom: 10px;
        }
        
        /* 추가적인 스타일 (선택 사항) */
        a {
          color: #3498db;
          text-decoration: none;
        }
        
        a:hover {
          text-decoration: underline;
        }
        
        p {
          margin-bottom: 15px;
        }
        
        ul, ol {
          margin-left: 20px;
          margin-bottom: 15px;
        }
        
        li {
          margin-bottom: 5px;
        }
    """
    
    # display(HTML(custom_css + html_output))
    display(HTML(html_output))