
def save_quote():
    author = input("შეიყვანე საყვარელი მწერალი: ")
    quote = input("შეიყვანე ციტატა: ")
    
    with open("quotes.txt", "w", encoding="utf-8") as file:
        file.write(f"მწერალი: {author}\nციტატა: {quote}")

def read_quote():
    with open("quotes.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)

save_quote()
read_quote()