ls = ['sameh', 2, 'amr', 5, 10]
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(ls[len(ls)-2])
# print last item
# print(ls[-1])
# i = 0
# for i in range(len(ls)):
#     print(ls[i])


for number in ls:
    if(str(number).isnumeric() == True):
        print(number)

for number in ls:
    if(str(number).isnumeric()):
        print(number)

for number in ls:
    if(str(number).isnumeric() == False):
        continue

    print(number)
