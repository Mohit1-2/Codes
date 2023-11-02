def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(nums)
    print(maxSubArray(nums))

def maxSubArray(nums):
    max_num = nums[0]
    temp_ans = 0
    for num in nums:
        temp_ans += num
        # if max_num is smaller than temp ans then we save temp ans as max_num
        max_num = max(max_num, temp_ans)

        # if temp_ans is less than 0 then we consider it zero as it will not give max subarray
        if temp_ans < 0:
            temp_ans = 0

    return max_num


if __name__ == "__main__":
    main()