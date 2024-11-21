"""
환경변수 로드
"""
import os
from dotenv import load_dotenv

load_dotenv()

# RELATIVE_CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH") # 실제 ChromeDriver의 경로로 변경
# ABSOLUTE_CHROME_DRIVER_PATH  = os.path.abspath(RELATIVE_CHROME_DRIVER_PATH)

ORACLEDB_USER = os.getenv("ORACLEDB_USER")
ORACLEDB_PASSWORD = os.getenv("ORACLEDB_PASSWORD")
ORACLEDB_CONNECT_STRING = os.getenv("ORACLEDB_CONNECTSTRING")
