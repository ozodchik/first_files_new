cook_book = {}
with open("recept.txt") as new_cookbook:
  line = new_cookbook.readline()
  # recept_begin = True
  while line != '':
    recept_name = line.strip()
    ingr_count = int(new_cookbook.readline())
    ingr = {}
    new_ingr = []
    for result in range(ingr_count):
      tmp = new_cookbook.readline().strip().split('|')
      ingredient_name, quantity, measure = tmp
      ingredient_list = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
      new_ingr.append(ingredient_list)
    ingr[recept_name] = new_ingr
    cook_book.update(ingr)
    new_cookbook.readline()
    line = new_cookbook.readline()

print(cook_book)


