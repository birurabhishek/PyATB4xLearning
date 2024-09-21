user_type = input("Enter the user type, Admin, Manager, Guest: ").lower()

match user_type:
    case "admin" | "manager":
        print("Hello Sir")
    case "guest":
        print("Hello Guest..!")
    case _:
        print("Hello there...!")