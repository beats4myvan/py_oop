def reverse_text(text):
    i = len(text)
    while i > 0:
        yield text[i-1]
        i -= 1


for char in reverse_text("step"):
    print(char, end='')
