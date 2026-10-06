import re

text = """
Meeting on 12/09/2026.
Call 9876543210.
#NLP is an important topic.
@OpenAI develops AI technologies.
Natural language processing is useful.
"""

print("========== SMART PATTERN MATCHING ENGINE ==========")
print("\nText:")
print(text)


def search_date():
    pattern = r"\b\d{2}/\d{2}/\d{4}\b"
    result = re.findall(pattern, text)

    print("\nDates Found:")
    for item in result:
        print(item)


def search_phone():
    pattern = r"\b[6-9]\d{9}\b"
    result = re.findall(pattern, text)

    print("\nPhone Numbers Found:")
    for item in result:
        print(item)


def search_hashtag():
    pattern = r"#\w+"
    result = re.findall(pattern, text)

    print("\nHashtags Found:")
    for item in result:
        print(item)


def search_mention():
    pattern = r"@\w+"
    result = re.findall(pattern, text)

    print("\nMentions Found:")
    for item in result:
        print(item)


def search_prefix():
    word = input("Enter prefix: ")

    pattern = r"\b" + re.escape(word) + r"\w*\b"
    result = re.findall(pattern, text, re.IGNORECASE)

    print("\nPrefix Matches:")
    for item in result:
        print(item)


def search_suffix():
    word = input("Enter suffix: ")

    pattern = r"\b\w*" + re.escape(word) + r"\b"
    result = re.findall(pattern, text, re.IGNORECASE)

    print("\nSuffix Matches:")
    for item in result:
        print(item)


def search_word():
    word = input("Enter word: ")

    pattern = r"\b" + re.escape(word) + r"\b"
    result = re.findall(pattern, text, re.IGNORECASE)

    print("\nWord Matches:")
    for item in result:
        print(item)


# Menu
while True:

    print("\n========== MENU ==========")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Search Word")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        search_date()

    elif choice == "2":
        search_phone()

    elif choice == "3":
        search_hashtag()

    elif choice == "4":
        search_mention()

    elif choice == "5":
        search_prefix()

    elif choice == "6":
        search_suffix()

    elif choice == "7":
        search_word()

    elif choice == "8":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")