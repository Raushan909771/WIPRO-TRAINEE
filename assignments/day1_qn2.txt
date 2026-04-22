string = 'banana is a tasty fruit'
count = 0
for i, ch in enumerate(string):
    if ch =='a':
        count = count + 1
        print(count)