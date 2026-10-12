def make_counter(start_value=0):
    count = start_value

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


counter = make_counter(start_value=16) 

print(counter())
print(counter())
print(counter())