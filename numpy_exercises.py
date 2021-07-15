##### NUMPY EXERCISES #####

import numpy as np # import numpy




a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7]) # create array to work with

#1. How many negative numbers are there?

print(len(a[a < 0]))

#2. How many positive numbers are there?

print(len(a[a > 0]))

#3. How many even positive numbers are there?

b = a[a > 0]
c = b[b % 2 == 0]
print(len(c))

#4. If you were to add 3 to each data point, how many positive numbers would there be?

a2 = a + 3
b2 = a2[a2 > 0]
pirnt(len(b2))

#5. If you squared each number, what would the new mean and standard deviation be?

squared = a ** 2
print(squared.mean())
print(squared.std())

#6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set.

centered = a - a.mean()
print(centered)

#7. Calculate the z-score for each data point.

z_score = centered / a.std()
print(z_score)




#8.

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a = sum(a)
print(sum_of_a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a)
print(min_of_a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = max(a)
print(max_of_a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = sum(a) / len(a)
print(mean_of_a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

product_of_a = 1
for number in a:
    product_of_a *= number
    
print(product_of_a)

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = list()

for number in a:
    squares_of_a.append(number ** 2)
    
print(squares_of_a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = list()

for number in a:
    if number % 2 != 0:
        odds_in_a.append(number)
        
print(odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = list()

for number in a:
    if number % 2 == 0:
        evens_in_a.append(number)
        
print(evens_in_a)




## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.

b = [
    [3, 4, 5],
    [6, 7, 8]
]

# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
# make b into a numpy array called b_array

b_array = np.array([
    [3, 4, 5],
    [6, 7, 8]
])

print(b)
print(type(b))
print(b_array)
print(type(b_array))

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 

sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

# using numpy

sum_of_b = b_array.sum()
print(sum_of_b)

# Exercise 2 - refactor the following to use numpy. 

min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

# using numpy

min_of_b = b_array.min()
print(min_of_b)

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.

max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

# using numpy

max_of_b = b_array.max()
print(max_of_b)

# Exercise 4 - refactor the following using numpy to find the mean of b

mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

# using numpy

mean_of_b = b_array.mean()
print(mean_of_b)

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.

product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

# using numpy

product_of_b = b_array.prod()
print(product_of_b)

# Exercise 6 - refactor the following to use numpy to find the list of squares 

squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

# using numpy

squares_of_b = np.square(b_array).flatten()
print(squares_of_b)

# Exercise 7 - refactor using numpy to determine the odds_in_b

odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

# using numpy

odds_in_b = b_array[b_array % 2 != 0]
print(odds_in_b)

# Exercise 8 - refactor the following to use numpy to filter only the even numbers

evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

# using numpy

evens_in_b = b_array[b_array % 2 == 0]
print(evens_in_b)

# Exercise 9 - print out the shape of the array b.

print(b_array.shape)

# Exercise 10 - transpose the array b.

print(np.transpose(b_array))

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

print(list(b_array.flatten()))

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

print(b_array.reshape(6 , 1))




## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# make c into a numpy array called c_array

c_array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(c)
print(type(c))
print(c_array)
print(type(c_array))

# Exercise 1 - Find the min, max, sum, and product of c.

print(c_array.min())
print(c_array.max())
print(c_array.sum())
print(c_array.prod())

# Exercise 2 - Determine the standard deviation of c.

print(c_array.std())

# Exercise 3 - Determine the variance of c.

print(c_array.var())

# Exercise 4 - Print out the shape of the array c

print(c_array.shape)

# Exercise 5 - Transpose c and print out transposed result.

print(c_array.transpose())

# Exercise 6 - Get the dot product of the array c with c. 

print(np.dot(c_array, c))

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

print((c_array * c_array.transpose()).sum())

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

print((c_array * c_array.transpose()).prod())




## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# make d into a numpy array called d_array

d_array = np.array(
[
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
)

print(d)
print(type(d))
print(d_array)
print(type(d_array))

# Exercise 1 - Find the sine of all the numbers in d

print(np.sin(d_array))

# Exercise 2 - Find the cosine of all the numbers in d

print(np.cos(d_array))

# Exercise 3 - Find the tangent of all the numbers in d

print(np.tan(d_array))

# Exercise 4 - Find all the negative numbers in d

print(d_array[d_array < 0])

# Exercise 5 - Find all the positive numbers in d

print(d_array[d_array > 0])

# Exercise 6 - Return an array of only the unique numbers in d.

print(np.unique(d_array))

# Exercise 7 - Determine how many unique numbers there are in d.

print(len(np.unique(d_array)))

# Exercise 8 - Print out the shape of d.

print(d_array.shape)

# Exercise 9 - Transpose and then print out the shape of d.

print(d_array.transpose().shape)

# Exercise 10 - Reshape d into an array of 9 x 2

print(d_array.reshape(9, 2))