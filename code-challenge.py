using_numbers = []
med = 0
sum_result = 0
square_result = 0
cube_result = 0
def sums(user):
    index = 0
    med = 0
    for item in range(0,using_numbers[-1]):
        med = med+using_numbers[index]
        index = index+1
    return(med)
def squares(user):
    index = 0
    med = 0
    for item in range(0,using_numbers[-1]):
        med = med+using_numbers[index]**2
        index = index+1
    return(med)
def cubes(user):
    index = 0
    med = 0
    for item in range(0,using_numbers[-1]):
        med = med+using_numbers[index]**3
        index = index+1
    return(med)
def supersum(user):
    sum_result = sums(user)
    square_result = squares(user)
    cube_result = cubes(user)
    print(sum_result+square_result+cube_result)
user = int(input('Enter a interger between 1 - 199: '))
for item in range(1,user+1):
    using_numbers.append(item)
supersum(user)