class Solution:
    def merge(self, nums1: List[int], n: int, nums2: List[int], m: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k=m+n-1
        j=n-1
        i=m-1
        while j>=0 and k>=0 and k>=0:
            if nums1[j]>=nums2[k]:
                nums1[k]=nums1[j]
                k=k-1
                j=j-1
            else:
                nums1[k]=nums2[i]
                i-=1
                k-=1
        while i>=0:
            nums1[k]=nums2[i]
            k-=1
            i-=1