"""
Match Statement
----------------
match variable:
    case pattern 1:
        #Code
    case pattern 2:
        #Code
"""

#WAP to ask the user which browser he wants to run an automation on

browser = input('Enter the browser name you want to use: ').lower()

match browser:
    case "firefox":
        print("Execute the Firefox code")
    case "chrome":
        print("Execute the Chrome code")
    case "edge":
        print("Execute the Edge code")
    case "safari":
        print("Execute the Safari code")
    case _:  # _ means default
        print("Browser not found")


