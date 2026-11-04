import threading
import time
import requests

URL = 'https://jsonplaceholder.typicode.com/posts/1'

def send_request():
  try:
    response = requests.get(URL)
  except Exception as e:
    print(e)


if __name__ == '__main__':
  start_time = time.time()

  threads = []

  for _ in range(100):
    thread = threading.Thread(target=send_request)
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()

  end_time = time.time()
  total_time = end_time - start_time

  print(f"ჯამური დრო {total_time:.4f} წამი")