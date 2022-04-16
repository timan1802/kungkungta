import easyocr

reader = easyocr.Reader(['ko'])
result = reader.readtext("img/test1.png")

print(result)