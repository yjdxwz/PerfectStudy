from io import StringIO
s = StringIO()
s.write("ssssssss")

content = s.getvalue()

print(content)

s.close()