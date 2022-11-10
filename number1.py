from tkinter import E


data = []
data.append([5, 4, 3, 2, 0.4807692307692308])
data.append([9, 1, 4, 6, 1.5576923076923077])

def compute_data(a, b, c, d):
   return (a / b) * (a / (c**2 + d**2)) 

for test in data:
    print(compute_data(test[0], test[1], test[2], test[3](5, 4, 3, 2)))

print(compute_data(9, 1, 4, 6))
