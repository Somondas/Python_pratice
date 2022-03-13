def sum_of_threeno(x, y, z):
    sum = x+y+z
    if x==y==z:
        sum = sum*3
        return sum
    else:
        return sum

print(sum_of_threeno(3,3,3))
print(sum_of_threeno(1,3,6))
