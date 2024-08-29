__author__ = "730700749"


def mimic(message: str) -> str:
    """Mimicing a message."""
    return message


print(mimic(message="hello"))


def main() -> None:
    """Main function."""
    return print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
