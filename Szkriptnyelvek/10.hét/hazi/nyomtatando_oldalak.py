#!usr/bin/env python3


def pages(li: list) -> list[int]:
    li = input().split(",")
    result: list = []
    for page in li:
        if page.find("-") > 0:
            start = page[0 : page.find("-")]
            end = page[page.find("-") + 1 :]
            for i in range(int(start), int(end) + 1):
                result.append(i)
        else:
            result.append(int(page))
    return result


def main():
    li: list[str] = input("Enter the pages you want to print:")
    print(pages(li))


if __name__ == "__main__":
    main()
