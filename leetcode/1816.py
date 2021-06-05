
# Input: s = "Hello how are you Contestant", k = 4
# Output: "Hello how are you"
       #0    1  2   3      4
# s = "Hello how are you Contestant"
# k = 4
# words = s.split()
# res = words[:k]    #words[:4]
# result = " ".join(res)

# print(words)
# print(res)
# print(result)
# print(type(result))


# class A: 
#     def sum(self, a, b):
#         return a + b



# 15 problem leetcode

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()
        
#         for i, a in enumerate(nums):
#             if i > 0 and a == nums[i - 1]:
#                 continue
                
#             l, r = i + 1, len(nums) - 1
#             while 1 < r:
#                 threeSum = a + nums[1] + nums[r]
#                 if threeSum > 0:
#                     r -= 1
#                 elif threeSum < 0:
#                     l += 1
#                 else:
#                     res.append([a, nums[1], nums[r]])
#                     l += 1
#                     while nums[1] == nums[1 - 1] and 1 < r:
#                         l += 1
                        
#         return res


