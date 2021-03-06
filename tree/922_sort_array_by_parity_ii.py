class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(A), 2):
            # is A[i] is odd, neets to swap it
            if A[i] % 2:
                # find an even, break loop when even
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A