def is_anagram(word, word1):
  word = sorted(word.replace(' ', '').lower())
  word1 = sorted(word1.replace(' ', '').lower())
  if word == word1:
    return True
  return False
print(is_anagram('Мама ранг а', 'Анаграмма')) # exapmle
