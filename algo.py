from math import gcd


def NumListConverter(raw_nums):
	pure_nums = []
	for string in raw_nums:
		if not string:
			raw_nums.remove(string)
		if string:
			pure_nums.append(int(string))
	return(pure_nums)


def GCD(strings):
    nums = NumListConverter(strings)
    if len(nums) < 3:
        nums.append(0)
    #MCD = gcd((gcd(nums[0], nums[1])), nums[2])
    MCD = gcd(nums[0], nums[1])
    MCD = gcd(MCD, nums[2])
    return(MCD)


def lcm(strings):
	nums = NumListConverter(strings)
	lcm = nums[0]
	for i in nums[1:]:
		lcm = int(lcm*i/gcd(lcm, i))
	if 0 in nums:
		lcm = "non è definito"
	return lcm


numeri = [12, 3, 4, 0]
print(GCD(numeri))