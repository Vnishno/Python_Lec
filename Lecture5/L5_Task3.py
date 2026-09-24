entered_text = input("Enter text:")
new_text =""

# for n in entered_text:
#     if not n.isdigit():
#         new_text += n

for n in entered_text:
     if  n.isdigit():
         continue
     new_text += n

print(new_text)
        