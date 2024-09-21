import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print((start_time))
        func()
        end_time = time.time()
        print(end_time)
        print(f"Time taken by function is {end_time-start_time}")
    return wrapper()

@time_decorator
def test_ui():
    print("Doing so and so function........")
    time.sleep(5)
