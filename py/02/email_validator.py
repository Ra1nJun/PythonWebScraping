import re

email = "user@example.com"

matched = re.search(r'(\w+\@\w+\.\w+)(\.\w+)?', email)

if matched == None:
    print(email)
    print("유효하지 않음")
else:
    print(email)
    print("유효함")
