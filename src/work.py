import crawler

def get_cover_image_url():
  cover_img = crawler.find_page(
    'https://gall.dcinside.com/mini/board/lists?id=vuta', 
    "//span[@class='cover']"
  )
  img_style = cover_img.get_attribute('style')
  start = img_style.find('url(') + 4     # url( 시작 위치에서 '(' 다음 위치를 계산
  end = img_style.find(')', start)       # ')' 위치를 찾습니다.
  url = img_style[start:end].strip('"')  # 양 끝의 쌍따옴표 제거
  return url
