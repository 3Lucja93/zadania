# items = [
#     ("product1", 10)
#     ("product2", 9)
#     ("product3", 12)
# ]
# prices = list(map(lambda item: item[1], items))
# print(prices)
#
# x = list(filter(lambda item: item[1] >= 10, items))
# print(x)

#
# students = [
#   {"imie": "Tomek", "wiek": 20},
#   {"imie": "Karolina", "wiek": 18}
# ]
# students.sort(key=lambda student: student["wiek"])
# print(students[0])



def Winner(file):
  with open('mecz.txt', 'r') as file:
    results = file.readline()
  count = 0
  for i in results:
    if i+1 != i:
      count += 1

return Winner







