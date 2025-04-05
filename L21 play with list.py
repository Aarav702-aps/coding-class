L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Origanal list :", L)
print()

count = 0

for i in L:
    count = count + i

    avg = count/len(L)

print("sum = ", count)
print("avgrage =", avg)
print()

#sorting the elements of the list
L.sort()
print("sorted array in ascending order", L)
print()

# printing the first element
print("the smallest element is:",L[0])

# printing the last element
print("largest element is:", L[-1])