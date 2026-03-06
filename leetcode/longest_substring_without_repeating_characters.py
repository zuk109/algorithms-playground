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

    longest=(0,0)
    while j<len(s):
        if s[j] not in seen:
            seen.add(s[j])
            j+=1
            max_len=max(max_len,j-i)
        else:
            seen.remove(s[i])
            i+=1
    return max_len


print(lengthOfLongestSubstring(""))


