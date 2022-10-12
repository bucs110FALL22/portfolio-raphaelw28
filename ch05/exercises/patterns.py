def star_pyramid():
  rows = (input("How many rows of stars?"))
  rows = int(rows)
  for i in range(rows):
    rows = ((rows - rows+1)+i)
  for i in range(rows):
    print(("*")*(i+1))

star_pyramid()


rows = (input("How many rows of stars?"))
rows = int(rows)
for i in range(rows, 0, -1):
  for i in range(0, i):
    print(("*")*i)



    
  
