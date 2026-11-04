from concurrent.futures import ThreadPoolExecutor
import time
import requests

URL = 'https://jsonplaceholder.typicode.com/posts/1'

def send_request(url):
  try:
    response = requests.get(url)
    return response.status_code
  except Exception as e:
    print(e)
    return None


if __name__ == '__main__':
  start_time = time.time()

  urls = [URL] * 100

  with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(send_request, urls))

  end_time = time.time()
  total_time = end_time - start_time

  print(f"ჯამური დრო {total_time:.4f} წამი")