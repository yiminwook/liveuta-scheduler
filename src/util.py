import requests

def save_image_to_local(image_url: str):
  response = requests.get(image_url, timeout=10)
  if response.status_code == 200:
    # 이미지 데이터를 'image.png' 파일로 저장합니다.
    with open('image.png', 'wb') as file:
      file.write(response.content)
    return True
  return False
