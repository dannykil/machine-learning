1. 해당 가상 환경 활성화
conda activate your_environment_name

2. ipykernel 설치
conda install ipykernel
# 또는
# pip install ipykernel

3. Jupyter 커널로 등록
python -m ipykernel install --user --name=ml_env --display-name "Python (ml_env)"