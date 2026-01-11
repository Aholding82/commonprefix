#python module capable of searching and outputting the largest common prefix
#amongst a given list of strings

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:

#read the str list elements
#take the first letter of the first list element of strs
#run a loop through every element of strs checking whether the first letter 
#every other element
#they only have to be checked against the first element

class Solution:
    def longest_common_prefix(self, strs):
        self.strs = strs
        result = ''
        for x in self.strs:             # taking the first letter of the first string
            for i in range(len(x)):

                for z in self.strs[1:]:     # checking the first letter against successive strings
                    if z[i] != x[i]:
                        break
                
                result = result + x[i]

            return result

strs = []
c = Solution()
results = c.longest_common_prefix(strs)