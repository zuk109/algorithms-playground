def isPalindrome(x):
    if x==0:
        return True
    if x<0:
        return False
    if x%10==0:
        return False
    z=x
    y=0
    while x!=0 :
        y=y*10+x%10
        x=x//10

    return y==z

'''
##No need to check the whole number
    while x>y :
        y=y*10+x%10
        x=x//10

    return x==y or x==y//10


'''
        