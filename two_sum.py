
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count=1
        n1=0
        L=[]
        for i in nums:
            n2=count
            for j in nums[count:]:
                num=nums[n1]+nums[n2]
                if num==target:
                    return [n1,n2]
                    # L.append((n1,n2,num))
                n2+=1
            count+=1
            n1+=1
                return [k[0],k[1]]
            
sol=Solution()
res=sol.twoSum([2,7,11,15],9)

print(res)
