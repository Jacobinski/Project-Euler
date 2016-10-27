# As we are using higher powers, logically we will have a smaller number
# Upper limit is arbitrarily high.
nums = []

for num in range(2,10000000):
    digits = list(str(num))
    if num == sum([int(i)**5 for i in digits]):
        nums.append(num)

print nums
print sum(nums)
