import copy

books = {
  "Book1": {"title": "Learn Python", "authors": ["Author A", "Author B"]},
  "Book2":{"title": "AI Basics", "authors": ["Author C"]}
}

#shallow_copy
shallow_copy=copy.copy(books)
shallow_copy["Book1"]["authors"].append("Author D")

print('after shallow copy')
print('shallow copy:',shallow_copy)
print('original dict',books)
print()
 #deep_copy
deep_copy=copy.deepcopy(books)
deep_copy["Book1"]["authors"].append("Author E")

print('after deep copy')
print('deep copy:',deep_copy)
print('original dict',books)