import random
length = int(input("Enter required password length: "))
choose_from = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
ans = "".join(random.sample(choose_from,length))
print(ans)