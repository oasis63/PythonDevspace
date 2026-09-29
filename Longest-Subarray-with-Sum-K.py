# Longest Subarray with Sum K


class Solution:
    def longestSubarray(self, arr, k):
        # code here
        mx_len = 0
        curr_sum = 0
        prefix_sum_map = {}

        for i in range(len(arr)):
            curr_sum += arr[i]

            if curr_sum == k:
                mx_len = i + 1

            complement = curr_sum - k

            if complement in prefix_sum_map:
                sub_len = i - prefix_sum_map[complement]
                mx_len = max(mx_len, sub_len)

            if curr_sum not in prefix_sum_map:
                prefix_sum_map[curr_sum] = i

        return mx_len
