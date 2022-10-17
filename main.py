numbers = [     [10, 11, 12, 13, 14],
               [20, 21, 22, 23, 24],
               [30, 31, 32, 33, 34]]

# numbers =[] 
# rnum = int(input('Enter the number of rows'))
# for i in range(rnum):
#values for a row: ').split()))
# 	numbers.append(row)
ryum=len(numbers[0])
rnum = len(numbers)
for i in range(rnum):
    sum=0;
    for j in range(ryum):
        sum+=numbers[i][j];
    print(f'The sum of row {i}={sum}');
    
# *****************************