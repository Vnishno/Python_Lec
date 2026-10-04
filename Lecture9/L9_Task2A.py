
def add_task(task_name, task_list=[]):
    task_list.append(task_name)
    return task_list


print(add_task("practice_1"))
print(add_task("practice_2"))
print(add_task("practice_3"))

# task_list არის ცვლადი ტიპის ობიექტი, 
# რის გამოც ფუნქცია ყოველ გამოძახებაზე ერთი და იგივე ლისტში ამატებს თასქებს და არ ქმნის ახალ ცვლას.