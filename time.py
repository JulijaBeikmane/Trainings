import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()
        function()
        finish_time = time.time()
        main_time = finish_time - start_time
        print(f"{function.__name__} run speed: {main_time}")
        
    return wrapper

@speed_calc_decorator
def function():
    for i in range(1000000):
        print(i * i)

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i * i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

# function()

fast_function()
slow_function()
