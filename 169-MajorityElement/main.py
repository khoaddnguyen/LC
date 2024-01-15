def majorityElement(self, nums: List[int]) -> int:
    # hashmap
    count = {}
    res, maxCount = 0, 0
    for n in nums:  # for each valur in nums, update count
        count[n] = 1 + count.get(n, 0)  # if n not in hashmap, return 0
        res = n if count[n] > maxCount else res
        maxCount = max(count[n], maxCount)
    return res
