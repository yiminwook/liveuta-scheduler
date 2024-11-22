import time
from apscheduler.schedulers.background import BackgroundScheduler
import work
import service

def job1():
  print("1. 커버 이미지 갱신을 시작합니다.")
  print(f"작업일시 '{time.localtime().tm_hour}'")
  image_url = work.get_cover_image_url()
  exist_cover_image = service.get_exist_cover_image()
  if exist_cover_image:
    service.update_cover_image(image_url)
    print("기존 커버 이미지가 갱신되었습니다.")
  else:
    service.insert_cover_image(image_url)
    print("새로운 커버 이미지가 등록되었습니다.")

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(job1, 'interval', days=1, id="job1")

try:
  while True:
    # 프로그램이 종료되지 않도록 대기
    time.sleep(1)
except (KeyboardInterrupt, SystemExit):
  # Ctrl+C 등 종료 시 스케줄러 중지
  scheduler.shutdown()
  print("스케줄러가 종료되었습니다.")
