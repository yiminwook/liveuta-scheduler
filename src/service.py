import db

def get_exist_cover_image():
  try:
    connection = db.connecting_db()
    cursor = connection.cursor()   # 연결된 DB 지시자(커서) 생성
    cursor.execute("SELECT * FROM META WHERE KEY = 'cover_image_url'")
    out_data = cursor.fetchall() # 커서의 내용을 out_data에 저장
    return out_data[0] if len(out_data) > 0 else None
  finally:
    if 'cursor' in locals():
      cursor.close()
    if 'connection' in locals():
      connection.close()
