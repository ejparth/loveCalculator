# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lowecase = name1.lower()
name2_lowercase = name2.lower()
both_names = name1_lowecase + name2_lowercase
print(both_names)
T_count = both_names.count("t")
R_count = both_names.count("r")
U_count = both_names.count("u")
E_count = both_names.count("e")

print(f"T occurs {T_count} times")
print(f"R occurs {R_count} times")
print(f"U occurs {U_count} times")
print(f"E occurs {E_count} times")

total_true = T_count + R_count + U_count+ E_count
print(f"Total = {total_true}")


L_count = both_names.count("l")
O_count = both_names.count("o")
V_count = both_names.count("v")
E_count = both_names.count("e")

print(f"L occurs {L_count} times")
print(f"O occurs {O_count} times")
print(f"V occurs {V_count} times")
print(f"E occurs {E_count} times")

total_love = L_count + O_count + V_count+ E_count

print(f"Total = {total_love}")

print(f"Love Score = {total_true}{total_love}")

total_Score = int(str(total_love) + str(total_true))


if total_Score <10 or total_Score >90:
  print(f"Your score is {total_true}{total_love}, you go together like coke and mentos")
elif total_Score >= 40 or total_Score <=50:
  print(f"Your score is {total_true}{total_love}, you are alright together." )
else:
  print(f"your score is {total_true}{total_love}.")

