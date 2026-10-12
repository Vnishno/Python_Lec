words = ["python", "generator", "yield", "code", "ai", "developer"]

generator = (x.upper() for x in words if len(x) > 4 )


for i in generator:
    print(i)