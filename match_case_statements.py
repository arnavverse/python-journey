print('''How many wonders are there in the world ?
      (1) 8
      (2) 7
      (3) 6
      (4) 5 ''')

x = int(input("Enter your option : "))
match x:
    case 1:
        print("Your choosen option is incorrect ❌")
    case 2:
        print("Your choosen option is correct ✅")
    case 3:
        print("Your choosen option is incorrect ❌")
    case 4:
        print("Your choosen option is incorrect ❌")
    case _:
        print("🤣🥀".center(15))