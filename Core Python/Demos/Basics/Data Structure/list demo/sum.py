# li= [[10,20],[30,40],[50,60]]
# total = 0
# for i in li:
#     for j in i:
#         total += j
# print("Sum of all elements =", total)

li = [5,[10,20],[30,40],[50,60]]
sum = li[0]
for i in li[1:]:
    for j in i:
        sum += j
print(sum)