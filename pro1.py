number_of_strings=int(input())
strings=[]
for _ in range(number_of_strings):
    strings.append(input())
common_prefix=strings[0]              
for char in range(1,len(strings)):
    while strings[char].find(common_prefix)!=0:   #finds the substring(last to first)
        common_prefix=common_prefix[:-1]
        if len(common_prefix)==0:
            print("-1")
print(common_prefix)
