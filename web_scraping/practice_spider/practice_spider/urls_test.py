import pytest
import urllib.request

with open('../book_urls.csv') as f:
  lines = f.readlines()
del lines[0]

@pytest.mark.parametrize("book_urls", lines, ids=str)
def test_urls(book_urls):
  assert urllib.request.urlopen(book_urls).getcode() == 200

# def create_set():
#   myset = set([])
#   for i in range(len(lines)):
#     myset.add(lines[i])
#   return myset

# def test_unique_urls():
#   assert len(create_set()) == len(lines)
