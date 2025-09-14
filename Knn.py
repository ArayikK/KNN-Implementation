# def merge_sort(arr):
#     n = len(arr)
#     if (n == 1):
#         return arr

#     arr_1 = arr[:n//2]
#     arr_2 = arr[n//2:]

#     arr_1 = merge_sort(arr_1)
#     arr_2 = merge_sort(arr_2)

#     return merge(arr_1, arr_2)  


# def merge(arr_a, arr_b):

#     arr_c = []

#     while (arr_a and arr_b):
#         if (arr_a[0] > arr_b[0]):
#             arr_c.append(arr_b.pop(0))
#         else:
#             arr_c.append(arr_a.pop(0))

#     if (arr_a):
#         arr_c += arr_a
#     if (arr_b):
#         arr_c += arr_b
    
#     return arr_c
K = 4

def Euc_distance(v1, v2):
    n = len(v1)
    if (len(v2) != n):
        print("Dimentions do not match !!!")
        return 0

    return sum([(v1[i] - v2[i]) ** 2 for i in range(n)]) ** 0.5

def most_common(arr):
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_items[0][0]
# print(Euc_distance([1, 2, 3], [4, 6, 3]))


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Մոդելն ըստ պարամետրերի վերադարձնում է թե արդյոք համակարգիչը (նթոբուքը) հզոր է (2), միջին (1) թե փոխելու ժամանակն է։
# x1 -->  RAM - ի չափը 
# x2 -->  Storage
# x3 -->  GPU - ի չապը
# x4 -->  Պրոցեսորի միջուկների թիվը (core)

#      x1      x2      x3      x4   y
M = [
    ["8Gb", "256Gb", "NaN",   "2", 1],
    ["4Gb",  "128Gb", "NaN",  "2", 0], 
    ["4Gb",  "256Gb", "NaN",  "2", 0],
    ["8Gb",  "512Gb", "2Gb",  "4", 1],  
    ["16Gb", "512Gb", "4Gb",  "4", 2], 
    ["32Gb", "1Tb",   "8Gb",  "8", 2],
    ["4Gb",  "128Gb", "NaN",  "2", 0],
    ["16Gb", "256Gb", "2Gb",  "4", 1],
    ["8Gb",  "1Tb",   "4Gb",  "4", 1],
    ["32Gb", "2Tb",   "16Gb", "16",2],
    ["4Gb",  "512Gb", "NaN",  "2", 0],
    ["12Gb", "512Gb", "2Gb",  "4", 1],
    ["16Gb", "1Tb",   "8Gb",  "8", 2],
    ["64Gb", "2Tb",   "16Gb", "16",2],
    ["8Gb",  "128Gb", "NaN",  "2", 0],
    ["12Gb", "256Gb", "2Gb",  "4", 1],
    ["16Gb", "512Gb", "8Gb",  "8", 2],
    ["4Gb",  "256Gb", "NaN",  "2", 0],
    ["32Gb", "1Tb",   "16Gb", "16",2],
    ["8Gb",  "256Gb", "NaN",  "2", 1],
    ["24Gb", "2Tb",   "16Gb", "16",2],   
    ]

# //////////////////////////////////////////////////////////////////////////////////////////////
# x1: 

# 4Gb -> 0
# 8Gb -> 1
# 12Gb -> 2
# 16Gb -> 3
# 24Gb -> 4
# 32Gb -> 5
# 64Gb -> 10

# //////////////////////////////////////////////////////////////////////////////////////////////
# x2: 

# 128Gb → 0
# 256Gb → 1
# 512Gb → 2
# 1Tb → 3
# 2Tb → 4

# //////////////////////////////////////////////////////////////////////////////////////////////
# x3: 

# NaN -> 0
# 2Gb -> 1
# 4Gb -> 2
# 8Gb -> 3
# 16Gb -> 4

# //////////////////////////////////////////////////////////////////////////////////////////////
# x4: 

# 2 -> 0
# 4 -> 1
# 8 -> 2
# 16 -> 3

M_numeric = [
    [1, 1, 0, 0, 1],   # ["8Gb", "256Gb", "NaN",   "2", 1]
    [0, 0, 0, 0, 0],   # ["4Gb",  "128Gb", "NaN",  "2", 0]
    [0, 1, 0, 0, 0],   # ["4Gb",  "256Gb", "NaN",  "2", 0]
    [1, 2, 1, 1, 1],   # ["8Gb",  "512Gb", "2Gb",  "4", 1]
    [3, 2, 2, 1, 2],   # ["16Gb", "512Gb", "4Gb",  "4", 2]
    [5, 3, 3, 2, 2],   # ["32Gb", "1Tb",   "8Gb",  "8", 2]
    [0, 0, 0, 0, 0],   # ["4Gb",  "128Gb", "NaN",  "2", 0]
    [3, 1, 1, 1, 1],   # ["16Gb", "256Gb", "2Gb",  "4", 1]
    [1, 3, 2, 1, 1],   # ["8Gb",  "1Tb",   "4Gb",  "4", 1]
    [5, 4, 4, 3, 2],   # ["32Gb", "2Tb",   "16Gb", "16",2]
    [0, 2, 0, 0, 0],   # ["4Gb",  "512Gb", "NaN",  "2", 0]
    [2, 2, 1, 1, 1],   # ["12Gb", "512Gb", "2Gb",  "4", 1]
    [3, 3, 3, 2, 2],   # ["16Gb", "1Tb",   "8Gb",  "8", 2]
    [10,4, 4, 3, 2],   # ["64Gb", "2Tb",   "16Gb", "16",2]
    [1, 0, 0, 0, 0],   # ["8Gb",  "128Gb", "NaN",  "2", 0]
    [2, 1, 1, 1, 1],   # ["12Gb", "256Gb", "2Gb",  "4", 1]
    [3, 2, 3, 2, 2],   # ["16Gb", "512Gb", "8Gb",  "8", 2]
                                                                  
# -----------------------------------------------------------------------------------------------

    [0, 1, 0, 0, 0],   # ["4Gb",  "256Gb", "NaN",  "2", 0]
    [5, 3, 4, 3, 2],   # ["32Gb", "1Tb",   "16Gb", "16",2]
    [0, 1, 0, 0, 1],    # ["8Gb",  "256Gb", "NaN",  "2", 1]
    [4, 4, 4, 3, 2],   # ["24Gb", "2Tb",   "16Gb", "16",2]
]


x_train = [i[:-1] for i in M_numeric[:-4]]
x_test = [i[:-1] for i in M_numeric[-4:]]

y_train = [i[-1] for i in M_numeric[:-4]]
y_test = [i[-1] for i in M_numeric[-4:]]

# Dist_Matrix = []
# for i in x_test:
#     Dist_Matrix.append([Euc_distance(i, j) for j in x_train])

Dist_Matrix = [[(Euc_distance(i[:-1], x_train[j][:-1]), j) for j in range(len(x_train))] for i in x_test]
Sorted_Dist = [sorted(i, key = lambda x: x[0]) for i in Dist_Matrix]
K_nearest = [[i[j][1] for j in range(K)] for i in Sorted_Dist]

test_values = [[y_train[i[j]] for j in range(len(i)) ]for i in K_nearest]
y_hat = [most_common(i) for i in test_values]
# print(Dist_Matrix[0])
# print(Sorted_Dist[0])
# print(K_nearest[0])
# print(K_nearest)
# print(test_values)
# print(y_hat)
# print([y_hat[i] == y_test[i] for i in range(len(y_hat))])


print(Dist_Matrix[0])
print(Sorted_Dist[0])
print(K_nearest[0])
print(test_values[0])


print("///////////////////////////////")
print(test_values)
print("////////////////////////")
print(y_hat)
print([y_hat[i] == y_test[i] for i in range(len(y_hat))])

