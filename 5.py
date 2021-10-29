def is_sorted(t):
  if sorted(t) == t:
    return True
  return False
print(is_sorted([1, 2, 3])) # example
print(is_sorted([3, 1, 2])) # example
