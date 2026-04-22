# find sum of numbers from 1 to 50 using xrange.
sum = 0
for i in range(1,51):
    sum += i
print('sum from 1 to 50:', sum)

# count how many times "a" appears in a string using enumerate.
string = 'banana is a tasty fruit'
count = 0
for i, ch in enumerate(string):
    if ch =='a':
        count = count + 1
        print(count)