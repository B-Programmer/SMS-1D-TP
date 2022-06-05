# Define a function to generate the UTF-8 value of the given SMS
def genTextUTF8(text):
    txtUTF8 = []
    for ch in text:
        txtUTF8.append(ord(ch))
    return txtUTF8