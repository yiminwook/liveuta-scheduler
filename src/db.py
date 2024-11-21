import oracledb
import config

def connecting_db():
  try:
    connection = oracledb.connect(
      user=config.ORACLEDB_USER,
      password=config.ORACLEDB_PASSWORD,
      dsn=config.ORACLEDB_CONNECT_STRING
    )

    return connection
  except oracledb.Error as e:
    # oracledb 관련 예외 처리
    error_obj, *_ = e.args
    # 확인후 제거
    print("An oracle error occurred:", e)

    print("Customer ID already exists")
    print("Error Code:", error_obj.code)
    print("Error Full Code:", error_obj.full_code)
    print("Error Message:", error_obj.message)
    raise
  except Exception as e:
    # 그 외 모든 예외 처리
    print("An unexpected error occurred:", e)
    raise
