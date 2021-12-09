msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"


def not_number(x, y):
    return True if x.isalpha() or y.isalpha() else False


def read():
    print(msg_0)
    return input()


def check_oper(oper):
    operations = ['+', '-', '*', '/']
    return True if oper not in operations else False


def start():
    while True:
        calc = read()
        x, oper, y = calc.split()
        if not_number(x, y) is True:
            print(msg_1)
        elif check_oper(oper):
            print(msg_2)
        else:
            break


def main():
    start()


if __name__ == '__main__':
    main()
