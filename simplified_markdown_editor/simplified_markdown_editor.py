def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")


def format_header():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 6:
                break
            else:
                print("The level should be within the range of 1 to 6")
        except ValueError:
            print("The level should be within the range of 1 to 6")

    text = input("Text: ")
    return f"{'#' * level} {text}\n"


def format_plain():
    text = input("Text: ")
    return text


def format_bold():
    text = input("Text: ")
    return f"**{text}**"


def format_italic():
    text = input("Text: ")
    return f"*{text}*"


def format_inline_code():
    text = input("Text: ")
    return f"`{text}`"


def format_link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"


def format_new_line():
    return "\n"


def format_list(is_ordered):
    while True:
        try:
            rows = int(input("Number of rows: "))
            if rows > 0:
                break
            else:
                print("The number of rows should be greater than zero")
        except ValueError:
            print("The number of rows should be greater than zero")

    result = ""
    for i in range(1, rows + 1):
        row_text = input(f"Row #{i}: ")
        if is_ordered:
            result += f"{i}. {row_text}\n"
        else:
            result += f"* {row_text}\n"
    return result


def main():
    formatters = {
        "plain": format_plain,
        "bold": format_bold,
        "italic": format_italic,
        "inline-code": format_inline_code,
        "link": format_link,
        "header": format_header,
        "new-line": format_new_line,
        "ordered-list": lambda: format_list(is_ordered=True),
        "unordered-list": lambda: format_list(is_ordered=False),
    }

    markdown_text = ""

    while True:
        command = input("Choose a formatter: ")

        if command == "!help":
            print_help()
        elif command == "!done":
            with open("output.md", "w", encoding="utf-8") as file:
                file.write(markdown_text)
            break
        elif command in formatters:
            markdown_text += formatters[command]()
            print(markdown_text)
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    main()