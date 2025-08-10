class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mindex = m-1
        nindex = n-1
        k = m+n-1

        while mindex >=0 and nindex >= 0:
            if nums1[mindex]>nums2[nindex]:
                nums1[k] = nums1[mindex]
                mindex-=1
            else:
                nums1[k] = nums2[nindex]
                nindex-=1
            
            k-=1
        

        while nindex >= 0:
            nums1[k] = nums2[nindex]
            k-=1
            nindex-=1
        




