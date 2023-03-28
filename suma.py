a = [1, 2, 3, 4]
first, *x = a
[1, 3, 6, 10]
wynik = []
# suma = sum(a[:1])
# suma1 = sum(a[:2])
# suma2 = sum(a[:3])
# suma3 = sum(a[:4])
print(a)
for i in a:
    suma = sum(a[:i])
    print(suma)

def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + nums[i]
    return(nums)
print(runningSum([1, 2, 3, 4]))
