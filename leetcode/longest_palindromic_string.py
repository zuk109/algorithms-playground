def longestPalindrome(s):
    """
    This function finds the longest palindromein a given string.
    uses the helper function expands(s,l,r) 
    time complexity- O(n**2), space complexity O(1)
    """
    longest=(0,0)

    for i in range(0,len(s)):
        temp=expand(s,i,i) #odd size palindrome
        if longest[1]-longest[0]<temp[1]-temp[0]:
            longest=temp
        temp=expand(s,i,i+1) #even size palindrome
        if longest[1]-longest[0]<temp[1]-temp[0]:
            longest=temp

    longests=s[longest[0]:longest[1]+1]

    return longests



def expand(s,l,r):
    """
    this function finds the longest palindrome in string s, where l,r are the middle index-
    by expanding from the center outwards. returns the index as a tuple.
    """
    while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1


    return (l+1,r-1)




print(longestPalindrome(""))