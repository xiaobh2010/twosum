class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count=0
        n1=0
        n2=0
        L=[]
        for i in nums:
            for j in nums[count:]:
                n2=nums.index(j)
                num=nums[n1]+nums[n2]
                L.append((n1,n2,num))
                n2+=1
            count+=1
            n1+=1
        for k in L:
            if k[2]==target:
                return [k[0],k[1]]
            
sol=Solution()
res=sol.twoSum([2,7,11,15],9)

print(res)
