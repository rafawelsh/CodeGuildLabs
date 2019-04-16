#10.average_numbers.py

# version1
# nums = [50,20,6,100]
# sum = 0
# for num in nums:
#     sum = sum + num
# avg = sum/len(nums)
# print(avg)

#version2
nums = []
while True:
    user = input("Add a number or done. ").strip().lower()
    if user == "done":
        print(sum(nums)/len(nums))
        break
    if user.isdigit():
        nums.append(int(user))
        continue
    else:
        continue
