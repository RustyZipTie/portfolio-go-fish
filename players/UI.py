def menu(options: list, caption: str = None):
    """
    presents the user with a list of options and returns the one they pick

    includes input validation
    Args:
        options (list[any]): options to present to user
        caption (str, optional): caption to display above menu
    Returns:
        whichever item from options the user picks
    """
    if len(options) == 0:
        print(">>>Error: empty options list")
        return

    show_list(options, caption=caption)
    while True:
        try:
            choice = int(input(">>>"))

            if not 1 <= choice <= len(options):
                raise ValueError()

            print(f">>>{options[choice - 1]}")

            return options[choice - 1]
        except:
            print(">>>Invalid choice")
            print(f">>>Enter a number between 1 and {len(options)}, inclusive")


def show_list(options: list, caption: str = None):
    """
    neatly displays a list to the user

    Args:
        options (list[any]): list to display
        caption (str, optional): caption to display above menu
    """
    if len(options) == 0:
        print(">>>Error: empty options list")
        return

    width = max(len(str(i)) for i in options)
    if caption:
        print(f">>>{caption}")

    print("+" + ("-" * (width + 6)) + "+")
    for i, option in enumerate(options):
        print(f"| {(i + 1):<3} {str(option):<{width}} |")
    print("+" + ("-" * (width + 6)) + "+")
