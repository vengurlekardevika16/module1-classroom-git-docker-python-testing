import sys


def main():
    name = ""
    if len(sys.argv) > 1:
        name = sys.argv[1]
    output = f"Hello, {name}"
    console_out(output)


def get_argument_as_string(arg: int = 1) -> str:
    return sys.argv[arg]


def console_out(output):
    print(output)


if __name__ == '__main__':
    main()
