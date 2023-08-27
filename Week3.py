# Question 1

# [1,3,7,2, 9]


def expanding(l):
    prev_abs_diff = abs(l[0] -l[1])
    
    for index in range(len(l) - 1):
        if index == 0:
            continue
        abs_diff = abs(l[index] - l[index + 1])
        if prev_abs_diff >= abs_diff:
            return False
        prev_abs_diff = abs_diff
        
    return True


# result = expanding([1,3,7,2,-3])
# print(result)




#Question 2

# [1,3,5]


def sumsquare(l):
    result = [0, 0]
    for index in range(len(l)):
        if l[index] % 2 != 0:
            result[0] += pow(l[index], 2)
        else:
            result[1] += pow(l[index], 2)
            
    return result

# print(sumsquare([-1,-2,3,7]))




#Question 3

#[[1, 2, 3, 4], [5, 6, 7, 8]]


def transpose(m):
    transposed_matrix = []
    No_of_columns = len(m[0])
    No_of_rows = len(m)
    for col in range(No_of_columns):
        temp = []
        for row in range(No_of_rows):
            temp.append(m[row][col])
        transposed_matrix.append(temp)
    return transposed_matrix  

# print(transpose([[3]]))