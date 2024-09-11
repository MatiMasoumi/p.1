items=['file.txt','image.jpeg',4,'document.pdf','notes.txt',22]
unique=set()
for i in items:
  if type(i)==str and '.' in i:
    extention=i.split('.')[-1]
    unique.add(extention)
print(unique)