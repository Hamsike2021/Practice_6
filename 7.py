def has_duplicates(s):
  if len(set(s)) < len(s):
    return True
  return False
print(has_duplicates('aab')) # example
print(has_duplicates([1, 2, 3])) # example
