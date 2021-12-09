msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"


def calculate_oper(x, oper, y):
    operation = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y}
    return operation[oper](x, y)


def start():
    memory = 0
    while True:
        calc = input(msg_0)
        x, oper, y = calc.split()
        try:
            x = memory if x == 'M' else float(x)
            y = memory if y == 'M' else float(y)
            result = calculate_oper(x, oper, y)
            print(result)
            if input(msg_4) == 'y':
                memory = result
            if input(msg_5) == 'n':
                break
        except ValueError:
            print(msg_1)
        except KeyError:
            print(msg_2)
        except ZeroDivisionError:
            print(msg_3)


if __name__ == '__main__':
    start()
