#occurence of  vowels in a sentense
def v_c(s):
    count=0
    for i in s:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count=count+1
    return count
a=input("Enter sentence: ").lower()
print(v_c(a))
