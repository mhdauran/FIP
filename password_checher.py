password = input("enter your password: ")

score = 0
tips = []

if len(password) >= 8:
    score += 1
else:
    tips.append("use at least 8 character.")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:

    if char.isupper():
        has_upper = True

    elif char.islower():
        has_lower = True

    elif char.isdigit():
        has_digit = True

    else:
        has_special = True

if has_upper:
    score += 1
else:
    tips.append("add an uppercase letter.")

if has_lower:
    score += 1
else:
    tips.append("add a lowercase.")

if has_digit:
    score += 1
else:
    tips.append("add a number.")

if has_special:
    score += 1
else:
    tips.append("add a special character.")

print("\npassword strength checher")
print("score:", score, "/5")

if score <= 2:
    print("strength: WEAK")
elif score <= 4:
    print("strength: MEDIUM")
else:
    print("strength: STRONG")

if tips:
    print("\nTips to improve your password:")
    for tip in tips:
        print("-", tip)

else:
    print("Excelent! All password checks passed.")