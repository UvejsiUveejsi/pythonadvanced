# # names = ["Erina", "Blina", "Uvejs", "Milot", "Diar", "Diar B", "Donart"]
# #
# # for name in names:
# #     print(name)
# #
# #
# # sentence = "Hello Milot"
# #
# # for char in sentence:
# #     if char.isalpha():
# #         print(char)
# #
# #
# # for number in range(1,10):
# #     print(number)
# #
# # numbers = [12,30,40,50,123]
# #
# #
# # maximum = numbers[0]
# #
# # for number in numbers:
# #     if number > maximum:
# #         maximum = number
# #
# # print("the maximum number in this array is: ", maximum)
#
#
# count = 1
#
# while count<=5:
#     print("the number is: ", count)
#     count+=1
#
# numbers=[1,2,3,4,5,6,7,8]
# target = 4
#
# for number in numbers:
#     if number == target:
#         print("target found")
#         break
#
#
# scores = [67, 43, 13 ,24, 16, 87, 34]
# total = 0
# count = 0
#
# mesatarja = 0
#
# for score in scores:
#     if score>50:
#      total += score
#      count+=1
#      continue
# mesatarja = total/count if count>0 else 0
#
# print("avg score for scores is: ", mesatarja)
#
# while True:
#     user_input = input("enter a positive number: ")
#
#     if user_input.isnumeric():
#         number = int(user_input)
#
#         if number > 0:
#             break
#     print("input invalid, try again")
# print("input valid.", number)
#

total = 0

for number in range(1,11):
    if number%2==0:
        total+=number
print(total)