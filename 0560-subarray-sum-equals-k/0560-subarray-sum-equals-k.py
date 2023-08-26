class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # To handle subarrays starting from index 0
        cnt = 0
        
        for num in nums:
            prefix_sum += num
            target_sum = prefix_sum - k
            cnt += prefix_sum_count[target_sum]
            prefix_sum_count[prefix_sum] += 1
        
        return cnt