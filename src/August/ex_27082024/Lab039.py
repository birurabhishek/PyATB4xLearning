def testing_ui_before_after(func):
    def wrapper():
        print("Before running UI Test case")
        print("Open Browser")
        func() #test_ui
        print("After running UI Test case")
        print("Quit Browser")
    return wrapper()

@testing_ui_before_after
def test_ui():
    print("Testing UI")

#Can also be made using below code

def start():
    print("Before running UI Test case")
    print("Open Browser")
def stop():
    print("After running UI Test case")
    print("Quit Browser")
def test_ui():
    print("Testing UI")

start()
test_ui()
stop()