print(dir(""))
print(help("bob".capitalize))
print("hello BOBOB".capitalize()) #only first letter of first world is capitalized and rest is lowercase
s = "Hello World"
print(s.upper()) #everything capital
print(s.lower()) #everything lower

print(help(s.center))
print(s.center(30)) #Spaces
print(s.center(30, "*"))  #center with stars

# fake xmas tree
for i in range(10):
    s = "*"*(2*i+1)
    print(s.center(50))
for i in range(4): #stump
    print("|||".center(50))

#find, finds the position of substring
s = "I see a cat. The cat is black. cats are nice"
print(s.find("cat")) # 8 is the first occurrence
print(s.find("dog")) # -1 when ir cant find
pos = 0
while True:
    pos = s.find("cat", pos)
    if pos == -1:
        break
    print(f"cat on position {pos}")
    pos += 1

print(s.count("cat"))
print(s.replace("cat", "dog"))
print(s.split())