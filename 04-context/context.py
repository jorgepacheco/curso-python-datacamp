# Open "alice.txt" and assign the file to "file"
with open('alice.txt') as file:
  text = file.read()

n = 0
for word in text.split():
  if word.lower() in ['cat', 'cats']:
    n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))

# Add a decorator that will make timer() a context manager

import contextlib
import time
@contextlib.contextmanager
def timer():
  start = time.time()
  yield
  end = time.time()
  print('Elapsed time: {:.2f} seconds'.format(end - start))

with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)

@contextlib.contextmanager
def open_read_only(filename):
  """Open a file in read-only mode.

  Args:
    filename (str): The location of the file to read

  Yields:
    file object
  """
  read_only_file = open(filename, mode='r')
  # Yield read_only_file so it can be assigned to my_file
  yield read_only_file
  # Close read_only_file
  read_only_file.close()

with open_read_only('my_file.txt') as my_file:
  print(my_file.read())

# Use the "stock('NVDA')" context manager
# and assign the result to the variable "nvda"
@contextlib.contextmanager
def stock(ticker):
  """Get stock data for a ticker symbol.

  Args:
    ticker (str): The ticker symbol to get data for (e.g. 'NVDA')
  Yields:
    dict: A dictionary containing stock data for the ticker symbol
  """