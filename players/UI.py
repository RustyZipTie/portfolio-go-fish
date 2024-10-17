def menu(options: list, num: bool = False, obj: bool = True):
    show_list(options)
    while True:
        try:
            choice = int(input(">>>"))

            if not 1 <= choice <= len(options):
                raise ValueError()

            print(f">>>{options[choice - 1]}")

            if num and obj:
                return choice - 1, options[choice - 1]
            elif num:
                return choice - 1
            elif obj:
                return options[choice - 1]
            else:
                return
        except:
            print(">>>Invalid choice")
            print(f">>>Enter a number between 1 and {len(options)}, inclusive")


def show_list(options: list):
    width = max(len(str(i)) for i in options)

    print("+" + ("-" * (width + 6)) + "+")
    for i, option in enumerate(options):
        print(f"| {(i+1):<3} {str(option):<{width}} |")
    print("+" + ("-" * (width + 6)) + "+")

def msg(code):
    print(
        {
            "num opp" : ">>>Choose number of opponents"
        }[code]
    )
