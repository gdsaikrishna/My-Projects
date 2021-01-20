user_input = str(input(" Enter word to find Acronym: "))
words = user_input.split()
ans = " "
for word in words:
    ans += str(word[0]).upper()
print(ans)