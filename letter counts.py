'''
NOT PRETTY BUT WORKS!!!!

PROBLEM STATEMENT:
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''


import time
start = time.time()
def numLetCount(n):
    dict = {1:'One',
           2:'Two',
           3:'Three',
           4:'Four',
           5:'Five',
           6:'Six',
           7:'Seven',
           8:'Eight',
           9:'Nine',
           10:'Ten',
           11:'eleven',
           12:'twelve',
           13:'thirteen',
           14:'fourteen',
           15:'fifteen',
           16:'sixteen',
           17:'seventeen',
           18:'eighteen',
           19:'nineteen',
           20:'twenty',
           30:'thirty',
           40:'forty',
           50:'fifty',
           60:'sixty',
           70:'seventy',
           80:'eighty',
           90:'ninety',
           1000:'onethousand'}
    if 1<= n <= 19:
        return dict[n]
    elif 20<= n < 100:
        if n%10 == 0:
            return dict[n]
        return dict[n - n%10] + dict[n%10]
    elif 100 <= n < 1000:
        if n%100 == 0:
            return dict[int(str(n)[0])] + 'hundred'
        elif int(str(n)[1:])%10 == 0:
            return dict[int(str(n)[0])] + 'hundredand' + dict[int(str(n)[1:])]
        elif 1<=int(str(n)[1:]) <=19:
            return dict[int(str(n)[0])] + 'hundredand' + dict[int(str(n)[1:])]
        return dict[int(str(n)[0])] + 'hundredand' + dict[int(str(n)[1:]) - int(str(n)[1:])%10] + dict[int(str(n)[1:])%10]
    elif n == 1000:
        return dict[n]

count = 0
for i in range(1,1001):
    count += len(numLetCount(i))
print(count)                         #------------> 21,124
end = time.time()               
print('%d ms' %((end-start)*1000))   #------------> 24 ms
