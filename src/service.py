import db
import const

def get_exist_cover_image():
  try:
    connection = db.connecting_db()
    cursor = connection.cursor()   # 연결된 DB 지시자(커서) 생성
    # META 테이블에서 KEY가 'cover_image_url'인 데이터를 조회
    cursor.execute(f"""
                   SELECT * 
                   FROM META 
                   WHERE KEY = '{const.COVER_IMAGE_KEY}'
                   """)
    out_data = cursor.fetchall() # 커서의 내용을 out_data에 저장
    return out_data[0] if len(out_data) > 0 else None
  finally:
    if 'cursor' in locals():
      cursor.close()
    if 'connection' in locals():
      connection.close()

def insert_cover_image(image_url: str):
  try:
    connection = db.connecting_db()
    cursor = connection.cursor()
    # META 테이블에 KEY가 'cover_image_url'인 데이터를 삽입
    cursor.execute(f"""
                   INSERT INTO META (KEY, VALUE)
                   VALUES ('{const.COVER_IMAGE_KEY}', '{image_url}')
                   """)
    connection.commit()
    return True
  except Exception as e:
    print("An unexpected error occurred:", e)
    return False
  finally:
    if 'cursor' in locals():
      cursor.close()
    if 'connection' in locals():
      connection.close()

def update_cover_image(image_url: str):
  try:
    connection = db.connecting_db()
    cursor = connection.cursor()
    # META 테이블에 KEY가 'cover_image_url'인 데이터를 삽입
    cursor.execute(f"""
                   UPDATE META
                   SET value = '{image_url}'
                   WHERE key = '{const.COVER_IMAGE_KEY}'
                   """)
    connection.commit()
    return True
  except Exception as e:
    print("An unexpected error occurred:", e)
    return False
  finally:
    if 'cursor' in locals():
      cursor.close()
    if 'connection' in locals():
      connection.close()
