class Solution:
    # num length
    def numLength(self, n: int):
        length = 0
        while n:
            n //= 10
            length += 1

        return length

    def sortNum(self, n: int):
        sn = str(n)
        l1 = list(sn)
        l1.sort(reverse=True)
        return int("".join(l1))

    def maximizeSum(self, nums: list[int], k: int) -> int:

        gains = []

        for num in nums:
            sorted_num = self.sortNum(num)
            gain = sorted_num - num
            gains.append((gain, sorted_num))

        total = sum(nums)
        gains.sort(reverse=True)

        for i in range(min(k, len(nums))):
            gain, _ = gains[i]
            total += gain

        return total


sol = Solution()
nums = [3, 6, 24, 13, 17]
k = 1
res = sol.maximizeSum(nums, k)
print(f"{res=}")
