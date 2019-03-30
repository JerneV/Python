# Jerne Vingerhoets
# 2/03/2019

## Simple Binary to Decimal converter 

inp = input("Enter a binary number. ")[::-1]  #Flips the whole number. 
out = 0

length = len(inp)

for x in range(length):
    if int(inp[x]) == 1:
        out += 2**x


print(out)

input("Press enter to exit")
