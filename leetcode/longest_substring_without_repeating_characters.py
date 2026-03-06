"""
def lengthOfLongestSubstring(s):
    if len(s)==0:
        return 0
    if len(s)==1:
        return 1
    i=0
    j=1
    max_len=0
    seen=set()
    seen.add(s[0])

    while j<len(s):
        if s[j] not in seen:
            seen.add(s[j])
            j+=1
            max_len=max(max_len,j-i)
        else:
            seen.remove(s[i])
            i+=1
    return max_len




"""

def lengthOfLongestSubstring(s):
    if len(s)==0:
        return 0
    if len(s)==1:
        return 1
    i=0
    j=1
    max_len=0
    seen={s[0]:0}


    for j in range(1,len(s)):
        if s[j]  in seen and seen[s[j]]>=i:
            i=seen[s[j]]+1

        seen[s[j]]=j
        max_len=max(max_len,j-i+1)
    return max_len


print(lengthOfLongestSubstring("au"))