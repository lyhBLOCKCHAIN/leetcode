# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=-1
        result=[1]
        if digits[i] < 9:
            digits[i]+=1
            return digits
        while digits[i] == 9 and -i<len(digits):
            digits[i]=0
            i-=1
        if -i==len(digits) and digits[i]==9:
            for j in range(len(digits)):
                result.append(0)
            return result
        if digits[i] < 9:
            digits[i]+=1
            return digits

class Solution(object):
    def plusOne(self, digits):
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            if len(digits) > 1:
                return self.plusOne(digits[:-1]) + [0]
            else:
                return [1] + [0]