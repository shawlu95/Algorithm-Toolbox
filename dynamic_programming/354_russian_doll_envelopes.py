class Solution(object):
    def maxEnvelopes(self, envs):
        def binarySearch(target, nums):
            """
            return type: int (ceiling of the insert position)
            """
            if not nums:
                return 0

            l = len(nums)
            start = 0
            end = l - 1

            while start <= end:
                half = start + (end - start) // 2
                if nums[half] == target:
                    return half
                elif nums[half] < target:
                    start = half + 1
                else:
                    end = half - 1

            return start

        def longestSubsequence(nums):
            """
            return type: int (number of longest subsequence)
            """
            if not nums:
                return 0
            l = len(nums)
            res = []

            for num in nums:
                pos = binarySearch(num, res)
                if pos >= len(res):
                    res.append(num)
                else:
                    res[pos] = num
            return len(res)

        envs = sorted(envs, key = lambda i: [i[0], - i[1]])
        # envs.sort(envs, key = lambda i: [i[0], - i[1]])
        # envs.sort(key=lambda (w,h): (w,-h))

        heights = [env[1] for env in envs]
        return longestSubsequence(heights)

solver = Solution()
print(solver.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))

