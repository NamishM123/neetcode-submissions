class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []

        res = [-1 ]* len(nums1)
        hash1 = {}
        set1 = set(nums1)

        for i,n in enumerate(nums2):
            while stack and stack[-1][1] < n:
                if stack[-1][1] in set1:
                    hash1[stack[-1][1]]  = n 
                    stack.pop()
                else:
                    stack.pop()
                    

            stack.append([i,n])


        for i in range(len(nums1)):
            if nums1[i] in hash1:
                res[i] = hash1[nums1[i]]
            else:
                pass 

        return res




            




        