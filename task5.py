d = {'mango': 10, 'banana': 0, 'apple': 15, 'orange': 0, 'pineapple': 20}

d = {k: v for k, v in d.items() if v != 0}
print(d)  

 
d['mango'] = 15
d['pineapple'] -= 5

print(d) 
