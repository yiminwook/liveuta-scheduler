# 가상환경 설정

python -m venv .venv

# 가상환경 활성화

source .venv/bin/activate

# 가상환경 비활성화

deactivate

# 패키지 기록

pip freeze > requirements.txt

# 패키지 설치

pip install -r requirements.txt
