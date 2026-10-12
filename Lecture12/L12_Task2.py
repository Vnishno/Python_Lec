from functools import wraps
import time


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        print(
            f"Running {func.__name__}... Executed in {execution_time:.2f} seconds."
        )
        return result

    return wrapper


@log_execution
def example_function(n):
    """This is a example_function."""
    time.sleep(1) 
    return n * 2


res = example_function(5)
print("Result:", res)
print("Function Name:", example_function.__name__)
print("Docstring:", example_function.__doc__)