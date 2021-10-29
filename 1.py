def nested_sum(t):
  sm = 0
  for el in t:
    sm += sum(el)
  return sm
print(nested_sum([[1, 2, 3], [4, 5]])) # example
