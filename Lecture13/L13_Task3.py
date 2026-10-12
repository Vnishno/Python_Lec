def greeter_bot():
    name = yield "Enter your name"
    
    while True:
        if name is None:
            break
        name = yield f"Hello, {name}!"

gen = greeter_bot()

print(next(gen)) 

print(gen.send("Giorgi")) 

print(gen.send("Nino")) 