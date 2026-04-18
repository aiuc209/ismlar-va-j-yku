ismlar = ["Ali", "Vali", "Soli", "Guli"]
jinslar = ["erkak", "ayol", "erkak", "ayol"]

for i in range(len(ismlar)):
    if jinslar[i] == "erkak":
        print(f"Salom, Mr. {ismlar[i]}!")
    else:
        print(f"Salom, Ms. {ismlar[i]}!")
