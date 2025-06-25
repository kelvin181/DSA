class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # first positive number indices
        positive1 = 0
        positive2 = 0
        
        while positive1 < len(nums1) and nums1[positive1] < 0:
            positive1 += 1
        
        while positive2 < len(nums2) and nums2[positive2] < 0:
            positive2 += 1

        l = - 10 ** 10
        r = 10 ** 10

        # find number of nums smaller than or equal to mid
        while l <= r:
            m = l + (r - l) // 2
            count = 0

            # negative * negative
            i = 0
            j = positive2 - 1
            while i < positive1 and j >= 0:
                if nums1[i] * nums2[j] > m:
                    i += 1
                else:
                    count += positive1 - i
                    j -= 1
            
            # positive * positive
            i = positive1
            j = len(nums2) - 1
            while i < len(nums1) and j >= positive2:
                if nums1[i] * nums2[j] > m:
                    j -= 1
                else:
                    count += j - positive2 + 1
                    i += 1
            
            # negative * positive
            i = 0
            j = positive2
            while i < positive1 and j < len(nums2):
                if nums1[i] * nums2[j] > m:
                    j += 1
                else:
                    count += len(nums2) - j
                    i += 1
            
            # positive * negative
            i = positive1
            j = 0
            while i < len(nums1) and j < positive2:
                if nums1[i] * nums2[j] > m:
                    i += 1
                else:
                    count += len(nums1) - i
                    j += 1
            
            # update l and r
            if count < k:
                l = m + 1
            else:
                r = m - 1
        
        return l
