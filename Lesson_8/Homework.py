
print("🌸 Personal Details Data Conversion 🌸\n")

personal_details = ("Koyna", "Chakraborty", 15, "5'3", "45kg", "Computer Science")

print(" Tuple (original, unchangeable):")
print(personal_details)

details_list = list(personal_details)

print("\n Converted into List (now editable!):")
print(details_list)

details_list.append("Loves Coding 💻")
print("\n Updated List after adding a new detail:")
print(details_list)
