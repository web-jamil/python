""" 
You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
Return the modified string after the spaces have been added.

 

Example 1:

Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
Output: "Leetcode Helps Me Learn"
Explanation: 
The indices 8, 13, and 15 correspond to the underlined characters in "LeetcodeHelpsMeLearn".
We then place spaces before those characters.
Example 2:

Input: s = "icodeinpython", spaces = [1,5,7,9]
Output: "i code in py thon"
Explanation:
The indices 1, 5, 7, and 9 correspond to the underlined characters in "icodeinpython".
We then place spaces before those characters.
Example 3:

Input: s = "spacing", spaces = [0,1,2,3,4,5,6]
Output: " s p a c i n g"
Explanation:
We are also able to place spaces before the first character of the string.
 

Constraints:

1 <= s.length <= 3 * 105
s consists only of lowercase and uppercase English letters.
1 <= spaces.length <= 3 * 105
0 <= spaces[i] <= s.length - 1
All the values of spaces are strictly increasing.




"""


def insert_spaces(s, spaces):  
    modified_string = []  
    space_index = 0  
    n = len(s)  

    for i in range(n):  
        # Check if the current index requires a space  
        if space_index < len(spaces) and i == spaces[space_index]:  
            modified_string.append(' ')  # Add a space before the character  
            space_index += 1  
        modified_string.append(s[i])  # Add the current character  

    return ''.join(modified_string)  

# Example usage  
print(insert_spaces("LeetcodeHelpsMeLearn", [8, 13, 15]))  # Output: "Leetcode Helps Me Learn"  
print(insert_spaces("icodeinpython", [1, 5, 7, 9]))      # Output: "i code in py thon"  
print(insert_spaces("spacing", [0, 1, 2, 3, 4, 5, 6]))   # Output: " s p a c i n g"


def add_spaces(s, spaces):
    result = []
    last_index = 0

    # Iterate through the spaces list
    for space_index in spaces:
        # Add the part of the string from the last index to the current space index
        result.append(s[last_index:space_index])
        # Add the space
        result.append(" ")
        # Update the last index
        last_index = space_index

    # Add the remaining part of the string after the last space
    result.append(s[last_index:])

    # Join the parts to form the final string
    return "".join(result)

# Example 1
s1 = "LeetcodeHelpsMeLearn"
spaces1 = [8, 13, 15]
print(add_spaces(s1, spaces1))  # Output: "Leetcode Helps Me Learn"

# Example 2
s2 = "icodeinpython"
spaces2 = [1, 5, 7, 9]
print(add_spaces(s2, spaces2))  # Output: "i code in py thon"

# Example 3
s3 = "spacing"
spaces3 = [0, 1, 2, 3, 4, 5, 6]
print(add_spaces(s3, spaces3))  # Output: " s p a c i n g"





def add_spaces(s, spaces):
    """
    Inserts spaces in the string `s` at indices specified in the `spaces` list.

    Args:
        s (str): The input string.
        spaces (List[int]): A list of indices where spaces need to be added.

    Returns:
        str: The modified string with spaces inserted.
    """
    result = []
    last_index = 0

    # Iterate through the spaces list
    for space_index in spaces:
        # Add the part of the string from the last index to the current space index
        result.append(s[last_index:space_index])
        # Add the space
        result.append(" ")
        # Update the last index
        last_index = space_index

    # Add the remaining part of the string after the last space
    result.append(s[last_index:])

    # Join the parts to form the final string
    return "".join(result)

# Test Cases
def test_add_spaces():
    # Test Case 1: Standard input with spaces in the middle
    s1 = "LeetcodeHelpsMeLearn"
    spaces1 = [8, 13, 15]
    assert add_spaces(s1, spaces1) == "Leetcode Helps Me Learn"

    # Test Case 2: Spaces at various positions
    s2 = "icodeinpython"
    spaces2 = [1, 5, 7, 9]
    assert add_spaces(s2, spaces2) == "i code in py thon"

    # Test Case 3: Spaces before every character
    s3 = "spacing"
    spaces3 = [0, 1, 2, 3, 4, 5, 6]
    assert add_spaces(s3, spaces3) == " s p a c i n g"

    # Edge Case 1: Empty string
    s4 = ""
    spaces4 = []
    assert add_spaces(s4, spaces4) == ""

    # Edge Case 2: No spaces to add
    s5 = "HelloWorld"
    spaces5 = []
    assert add_spaces(s5, spaces5) == "HelloWorld"

    # Edge Case 3: Space at the start and end
    s6 = "HelloWorld"
    spaces6 = [0, 5, 10]
    assert add_spaces(s6, spaces6) == " Hello World "

    # Edge Case 4: Consecutive spaces
    s7 = "HelloWorld"
    spaces7 = [1, 2, 3]
    assert add_spaces(s7, spaces7) == "H e l l oWorld"

    # Edge Case 5: Large input size
    s8 = "a" * 100000
    spaces8 = list(range(0, 100000, 10))
    assert add_spaces(s8, spaces8) == "a a a a a a a a a a " + "a" * 9 * 9999

    print("All test cases passed!")

# Run tests
test_add_spaces()



def add_spaces(s, spaces):
    """
    Inserts spaces in the string `s` at indices specified in the `spaces` list.

    Args:
        s (str): The input string.
        spaces (List[int]): A list of indices where spaces need to be added.

    Returns:
        str: The modified string with spaces inserted.
    """
    result = []
    last_index = 0

    for space_index in spaces:
        # Append part of the string from `last_index` to `space_index`
        result.append(s[last_index:space_index])
        # Append a space
        result.append(" ")
        # Update `last_index` to the current `space_index`
        last_index = space_index

    # Append the remaining part of the string
    result.append(s[last_index:])
    return "".join(result)


# Test Case
s = "icodewithpython"
spaces = [1, 5, 7, 9]  # Insert spaces at positions 1, 5, 7, and 9
output = add_spaces(s, spaces)
print(output)  # Expected Output: "i code with py thon"
# Test cases to validate the function
test_cases = [
    ("icodeinpython", [1, 5, 7, 9], "i code in py thon"),
    ("LeetcodeHelpsMeLearn", [8, 13, 15], "Leetcode Helps Me Learn"),
    ("spacing", [0, 1, 2, 3, 4, 5, 6], " s p a c i n g"),
    ("", [], ""),  # Empty string
    ("HelloWorld", [], "HelloWorld"),  # No spaces to insert
    ("HelloWorld", [0, 5, 10], " Hello World "),  # Spaces at start and end
]

# Validate all test cases
for s, spaces, expected in test_cases:
    assert add_spaces(s, spaces) == expected, f"Failed for {s} with spaces {spaces}"

print("All test cases passed!")



def add_spaces(s, spaces):
    arr = []
    arr.append(s[:spaces[0]])
    for i in range(1, len(spaces)):
        arr.append(s[spaces[i-1]:spaces[i]])
    arr.append(s[spaces[-1]:])
    return ' '.join(arr)
  
  
  
  
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []                   # Use a list for efficient string construction
        it = 0                        # Pointer for spaces array

        for i, char in enumerate(s):
            if it < len(spaces) and i == spaces[it]: # Insert space if index matches
                result.append(' ')
                it += 1
            result.append(char)       # Append character to result

        return ''.join(result)  
      
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ''
        idx, size = 0, len(spaces)
        for i, ch in enumerate(s):
            if idx < size and i == spaces[idx]:
                idx += 1
                ans += ' '
            ans += ch
        return ans# Combine list into final string
      
      
class Solution(object):
    def addSpaces(self, s, spaces):
        result = []
        i, j = 0, 0
        n, m = len(s), len(spaces)
        
        while j < m:
            if i == spaces[j]:
                result.append(' ')
                j += 1
            result.append(s[i])
            i += 1
        
        while i < n:
            result.append(s[i])
            i += 1
        
        return ''.join(result)
      
class Solution(object):
    def addSpaces(self, s, spaces):
        result = []
        i, j = 0, 0
        n, m = len(s), len(spaces)
        
        while j < m:
            if i == spaces[j]:
                result.append(' ')
                j += 1
            result.append(s[i])
            i += 1
        
        while i < n:
            result.append(s[i])
            i += 1
        
        return ''.join(result)
          
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ind = 0
        ans = ""
        for i in range(len(s)):
            if ind < len(spaces) and i == spaces[ind]:
                ans += " "
                ind += 1
            ans += s[i]
        return ans
      
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        i , k = 0, 0
        while i < len(s) and k < len(spaces):
            if i == spaces[k]:
                res += " "
                k += 1
            res += s[i]
            i += 1
        
        while i < len(s):
            res += s[i]
            i += 1
        
        return res
      
            
def add_spaces(s: str, spaces: list[int]) -> str:
    result = []
    n = len(s)
    j = 0
    count = 0

    for i in range(len(spaces)):
        while j < n and count < spaces[i]:
            result.append(s[j])
            j += 1
            count += 1
        result.append(' ')  # Add space at the specified position

    while j < n:
        result.append(s[j])
        j += 1

    return ''.join(result)
  
  
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        prev_index = 0
        
        for space in spaces:
            # Append substring from the previous index to the current space index
            result.append(s[prev_index:space])
            # Add a space
            result.append(" ")
            # Update the previous index
            prev_index = space
        
        # Add the remaining part of the string
        result.append(s[prev_index:])
        
        # Join the list into a single string
        return "".join(result)

def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        idx = 0
        n = len(spaces)
        
        for i in range(len(s)):
            space_idx = spaces[idx]
            if(i == space_idx):
                res += " "
                if(idx != n - 1): idx += 1 
            res += s[i]
                
        return res

def addSpaces(self, s: str, spaces: List[int]) -> str:
	res = s[:spaces[0]] + " "

	for j in range(1, len(spaces)):
		res +=  s[spaces[j- 1]:spaces[j]] + " "

	res +=  s[spaces[-1]:]       
	return res


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        spaces = set(spaces)
        for i in range(len(s)):
            if i in spaces:
                result+= ' ' + s[i]
            else:
                result+=s[i]
        return result

def addSpaces(self, s: str, spaces: List[int]) -> str:
        resArr = []
        i = 0
        
		# Take portions of the string between spaces and put them in the list
        for index in spaces:
            portion = s[i:index]
            resArr.append(portion)
            i = index
            
        #Put the remaining string in resArr
        resArr.append(s[spaces[len(spaces) - 1]:])
        return " ".join(resArr)



class Solution:
    def addSpaces(self, s: str, S: List[int]) -> str:
        
        curr_j = 0
        ans = ""
        
        for i in range(len(s)):
            if curr_j == len(S):
                ans += s[i:]
                break
            elif i == S[curr_j]:
                ans += " " + s[i]
                curr_j += 1
            else:
                ans += s[i]
            
            

        return ans
        
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr = []
        prev = 0
        for space in spaces:
            arr.append(s[prev:space])
            prev = space
        arr.append(s[space:])
        return " ".join(arr)        
        
def addSpaces(self, s: str, spaces: List[int]) -> str:        
    l=0
    a=''
    for i in spaces:            
        a += s[l:i]+ ' '
        l=i
    a+=s[spaces[-1]:]
    return a
  


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        arr = []
        prev = 0
        for space in spaces:
            arr.append(s[prev:space])
            prev = space
        arr.append(s[space:])
       
        return " ".join(arr)
      
      
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        lastIdx = 0
        for i in spaces:
            res += s[lastIdx:i]
            res += " "
            lastIdx = i
        res += s[lastIdx:]
        return(res)

        #TLE ->
        # s = list(s)
        # for i in range(len(spaces)):
        #     idx = spaces[i] + i
        #     s.insert(idx, " ")
        # res = ''.join(s)
        # return(res)
        
class Solution:
    
    # Define the method
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        # Create the dict
        d= {}
        
        # Create the ans variable
        ans= ""
        
        # Iterate on the string and store into the dict
        for i in range(len(s)): d[i]= s[i]
            
        # Iterate on the spaces
        for i in spaces:
            
            # If the i is found in the d then add the spaces before the char
            if i in d: d[i]= ' '+d[i]

        # How iterate on the dict and keep appending the string into the ans as the required ans
        for i in d: ans = ans + d[i]

        # Finally return the required ans
        return ans        
class Solution(object):
    def addSpaces(self, s, spaces):
        result = []
        prev = 0
        for i in spaces:
            result.append(s[prev:i])  
            result.append(' ')     
            prev = i
        result.append(s[prev:])      
        return ''.join(result)        


class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        result = []  
        space_pointer = 0  

        for i, char in enumerate(s):  
            
            if space_pointer < len(spaces) and i == spaces[space_pointer]:
                result.append(' ')  
                space_pointer += 1  
            
            result.append(char) 
        
        return ''.join(result)  


class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        modified = []
        space_index = 0

        for i in range(len(s)):
            if i <= spaces[-1]:
                if i != spaces[space_index]:
                    modified.append(s[i])
                else:
                    space_index += 1
                    modified.append(' ')
                    modified.append(s[i])

            else:
                modified.append(s[i])

        modified_string = ''.join(modified)
        return modified_string

class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        prev= 0
        newString = []
        for i in spaces:
            newString.append(s[prev:i])
            prev = i
        newString.append(s[spaces[-1]:])
        return " ".join(newString)


        





class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        previous = 0

        for index in spaces:
            # Append the substring from `previous` to `index`
            result.append(s[previous:index])
            # Append a space
            result.append(" ")
            # Update `previous` to the current index
            previous = index

        # Append the remaining part of the string
        result.append(s[previous:])

        # Join all parts efficiently
        return "".join(result)



class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        space_index = 0
        space_count = len(spaces)
        
        for i in range(len(s)):
            if space_index < space_count and i == spaces[space_index]:
                result.append(' ')
                space_index += 1  
            
            result.append(s[i])
        
        return ''.join(result)


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        st=""
        k=0
        for i in spaces:
            if i==0:
                st+=' '
            else:
    
                st+=s[k:i]
                st+=' '
            k=i
        
        return st+s[k:len(s)]
            

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        st='';k=0
        for i in spaces:
            st += s[k:i]+' '
            k=i
        st+=s[k:]
        return st
        

                
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ns=[]
        b=set(spaces)
        for i in range(len(s)):
            if i in b:
                ns.append(' ')
            ns.append(s[i])
        return (''.join(ns))