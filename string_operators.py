# + will perform string concatenation
s1 = "hello"
s2 = "bye"
print(s1 + " " + s2)
print(s2 + " " + s1)

# u can multiply a string by an integer
print(3*s2)
print(s1 + " " + s2 + "!"*10)

# we can iterate over a string using for
for c in s1:
    print(c)

i = 0
while i < len(s1):
    print(s1[i])
    i += 1

s_new = ""
for c in s1:
    s_new = s_new + c*4
print(s_new)