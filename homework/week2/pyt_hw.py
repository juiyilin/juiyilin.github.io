# 1
def calculate(min, max):
    total=0

    # 檢查min是否真的小於max
    if min>max:
        min, max = max, min
    
    for i in range(min, max+1):
        total+=i
    print(total)

calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30


# 2
def avg(data):
    person=data['count']
    #person=len(data['employees'])
    total=0
    for p in range(person):
        salary=data['employees'][p]['salary']
        total+=salary
    avg_salary=total/person
    print(avg_salary)

avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
}) # 呼叫 avg 函式


# 3
def maxProduct(nums):
    result=nums[0]*nums[1]
    for i in range(len(nums)):
        for j in nums[i+1:]:
            multiple=nums[i]*j
            if result<multiple:
                result=multiple

    print(result)


maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值


# 4
def twoSum(nums, target):
    for n in nums:
        if target-n in nums and (target-n) != n:
            return [nums.index(n),nums.index(target-n)]

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


# 5
def maxZeros(nums):
    count=0
    maxcount=0
    for n in nums:
        if n==0:
            count+=1
        else:
            if count>maxcount:
                maxcount=count
            count=0
    if count>maxcount:
        maxcount=count
    print(maxcount)

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0