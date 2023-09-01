phone_book = {}


def input_error(func):
    def inner(*param: tuple) -> str:
        try:
            return func(*param)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Give me name and phone please"

    return inner


@input_error
def save_name_and_phone(*param: tuple) -> str:
    list_of_param = param[0]
    phone_book[list_of_param[0]] = list_of_param[1]
    return f"Done"


@input_error
def find_phone_by_name(*param: tuple) -> str:
    list_of_param = param[0]
    return phone_book[list_of_param[0]]


@input_error
def change_phone(*param: tuple) -> str:
    list_of_param = param[0]
    phone_book[list_of_param[0]] = list_of_param[1]
    return "Done"


@input_error
def all_phones_str() -> str:
    result = ""
    for k, v in phone_book.items():
        result += k + ": " + v + "\n"
    return result.removesuffix("\n")


def command_parcer(input_text: str) -> str:
    words = input_text.split(" ")

    if words[0].lower() == "hello":
        return "How can I help you?"
    elif words[0].lower() == "add":
        return save_name_and_phone(words[1::])
    elif words[0].lower() == "change":
        return change_phone(words[1::])
    elif words[0].lower() == "phone":
        return find_phone_by_name(words[1::])
    elif len(words) == 2 and words[0].lower() == "show" and words[1].lower() == "all":
        return all_phones_str()
    elif (
        (len(words) == 2 and words[0].lower() == "good" and words[1].lower() == "bye")
        or (words[0].lower() == "close")
        or (words[0].lower() == "exit")
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
