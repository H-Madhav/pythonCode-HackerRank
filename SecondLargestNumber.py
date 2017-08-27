n = int(input())
    arr = map(int, input().split())
    nums = sorted(arr, reverse=True)
    for num in nums:
        if num < nums[0]:
            print(num)
            break