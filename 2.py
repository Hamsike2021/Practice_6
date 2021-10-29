def cumsum(t):
  t1 = []
  for i in range(len(t)):
    t1.append(sum(t[:i + 1]))
  return t1
print(cumsum([1, 2, 3, 4, 5])) # example
