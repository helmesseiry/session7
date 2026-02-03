from string import punctuation
s = "A man, a plan, a canal: Panama"
# s = "Yo! Banana Boy!"
# s = "a nut for a jar of tuna"

# step 1: remove punctuation
# step 2: remove spaces
# step 3: convert to upper/lower
# step 4: compare with reversed
# step 5: profit

punctuation = "!,.?-"
for p in punctuation:
    s = s.replace(p, "") # removing punctuation
print(s)

#spaces
s = s.replace(" ", "")
print(s)

#upper
s = s.lower()
print(s)

if s == s[::-1]:
    print("Is palindrome")
else :
    print("Is not palindrome")

