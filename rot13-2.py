#!/usr/bin/env python3

import string


class Rot13:
    # print(codecs.encode('Hello', 'rot_13'))
    def __init__(self, message: str) -> None:
        self.upper_ascii = string.ascii_uppercase
        self.lower_ascii = string.ascii_lowercase
        self.digits = string.digits
        self.message = message

    def encode_decode(self) -> str:
        answer = ""

        try:
            for char in self.message:
                # print(char)
                if char in self.upper_ascii:
                    answer += self.upper_ascii[(self.upper_ascii.index(char) + 13) % 26]
                elif char in self.lower_ascii:
                    answer += self.lower_ascii[(self.lower_ascii.index(char) + 13) % 26]
                if char in self.digits:
                    answer += self.digits[(self.digits.index(char) + 13) % 10]
                if char == " ":
                    answer += char
        except IndexError:
            pass

        return answer


def main() -> None:
    message = input("[+] Provide Rot13 encoded message: \n")

    rot13 = Rot13(message)
    print(rot13.encode_decode())


if __name__ == "__main__":
    main()
