"""
DB 연결
"""
import oracledb
import config

try:
    connection = oracledb.connect(user=config.ORACLEDB_USER, password=config.ORACLEDB_PASSWORD, dsn=config.ORACLEDB_CONNECT_STRING)   # DB에 연결 (호스트이름 대신 IP주소 가능)
    cursor = connection.cursor()   # 연결된 DB 지시자(커서) 생성
    
    result =  cursor.execute("SELECT * FROM META") # 데이터베이스 명령 실행( cursor가 임시로 보관)
    
    out_data = cursor.fetchall() # 커서의 내용을 out_data에 저장
    
    print(out_data) # out_data의 내용을 출력 
    for record in out_data: # out_data의 내용을 출력
      print(record)


except oracledb.DatabaseError as e:
    error, = e.args
    print(f"Oracle-Error-Code: {error.code}")
    print(f"Oracle-Error-Message: {error.message}")

finally:
    # 커서 및 연결 닫기
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()