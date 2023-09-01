phone_book = {}


def input_error():
    pass


def save_name_and_phone(name: str, phone: str) -> str:
    phone_book[name] = phone
    return "Done"


def find_phone_by_name(name: str) -> str:
    return phone_book.get(name)


def change_phone(name: str, phone: str) -> str:
    phone_book[name] = phone
    return "Done"


def all_phones_str() -> str:
    result = ""
    for k, v in phone_book.items():
        result += k + ": " + v + "\n"
    return result.removesuffix("\n")


def command_parcer(input_text: str) -> str:
    words = input_text.split(" ")

    if len(words) == 1 and words[0].lower() == "hello":
        return "How can I help you?"
    elif len(words) == 3 and words[0].lower() == "add":
        return save_name_and_phone(words[1], words[2])
    elif len(words) == 3 and words[0].lower() == "change":
        return change_phone(words[1], words[2])
    elif len(words) == 2 and words[0].lower() == "phone":
        return find_phone_by_name(words[1])
    elif len(words) == 2 and words[0].lower() == "show" and words[1].lower() == "all":
        return all_phones_str()
    elif (
        (len(words) == 2 and words[0].lower() == "good" and words[1].lower() == "bye")
        or (len(words) == 1 and words[0].lower() == "close")
        or (len(words) == 1 and words[0].lower() == "exit")
    ):
        return "exit"
    else:
        return ""


def main():
    while True:
        input_text = input().strip()

        if input_text == "":
            continue

        result = command_parcer(input_text)

        if result == "exit":
            print("Good bye!")
            break
        elif result == "":
            continue
        else:
            print(result)


if __name__ == "__main__":
    main()
