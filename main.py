import timeit
import random

from insertion_sort import insertion_sort
from merge_sort import merge_sort

if __name__ == '__main__':
  data_small = [random.randint(0, 1000) for _ in range(1000)]
  data_medium = [random.randint(0, 10000) for _ in range(10000)]

  time_merge_small = timeit.timeit(lambda: merge_sort(data_small[:]), number=10)
  time_insertion_small = timeit.timeit(lambda: insertion_sort(data_small[:]), number=10)
  time_sorted_small = timeit.timeit(lambda: sorted(data_small[:]), number=10)
  time_sort_small = timeit.timeit(lambda: data_small[:].sort(), number=10)

  time_merge_medium = timeit.timeit(lambda: merge_sort(data_medium[:]), number=10)
  time_insertion_medium = timeit.timeit(lambda: insertion_sort(data_medium[:]), number=10)
  time_sorted_medium = timeit.timeit(lambda: sorted(data_medium[:]), number=10)
  time_sort_medium = timeit.timeit(lambda: data_medium[:].sort(), number=10)

  print(f"{'| Algorithm': <20} | {'Time 1000 items': <20} | {'Time 10 000 items': <20}")
  print(f":{'-'*19} | :{'-'*19} | :{'-'*19}")
  print(f"{'| Merge sort': <20} | {time_merge_small: <20.5f} | {time_merge_medium: <20.5f}")
  print(f"{'| Insertion sort': <20} | {time_insertion_small: <20.5f} | {time_insertion_medium: <20.5f}")
  print(f"{'| Sorted': <20} | {time_sorted_small: <20.5f} | {time_sorted_medium: <20.5f}")
  print(f"{'| Sort': <20} | {time_sort_small: <20.5f} | {time_sort_medium: <20.5f}")
