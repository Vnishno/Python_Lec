import multiprocessing
import time

def calculate_factorial(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result

if __name__ == '__main__':
  number = 50000

  start_time = time.time()

  results = [calculate_factorial(number) for i in range(4)]

  p_time = time.time() - start_time
  print(f"single process-ის დრო: {p_time:.2f} წამი")

  start_time = time.time()

  with multiprocessing.Pool() as pool:
    results = pool.map(calculate_factorial, [number, number, number, number])

  multiprocessing_time = time.time() - start_time
  print(f"Multiprocessing დრო: {multiprocessing_time:.4f} წამი")

  difference = p_time - multiprocessing_time
  print( f"სხვაობა {difference:.4f} " )
