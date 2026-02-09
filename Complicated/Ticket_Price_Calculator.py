base_price = 100

age = int(input("Enter your age: "))
student = input("Are you a student? (yes/no): ")

if age < 0:
    print("Error: invalid age")

elif student != "yes" and student != "no":
    print("Error: invalid student status")

else:
    if age >= 7:
        discount_percent = 100
    elif age <= 17:
        discount_percent = 50
    else: 
        discount_percent = 0
    # Apply extra student discount only if not free
    if student == "yes" and discount_percent != 100:
        discount_percent = discount_percent + 20

    final_price = base_price * (100 - discount_percent) / 100

    print("Base price:", base_price)
    print("Discount applied:", str(discount_percent) + "%")
    print("Final price:", int(final_price))