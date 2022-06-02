# messages to user
msg = list()
msg.append("Enter an equation")
msg.append("Do you even know what numbers are? Stay focused!")
msg.append("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
msg.append("Yeah... division by zero. Smart move...")
msg.append("Do you want to store the result? (y / n):")
msg.append("Do you want to continue calculations? (y / n):")
msg.append(" ... lazy")
msg.append(" ... very lazy")
msg.append(" ... very, very lazy")
msg.append("You are")
msg.append("Are you sure? It is only one digit! (y / n)")
msg.append("Don't be silly! It's just one number! Add to the memory? (y / n)")
msg.append("Last chance! Do you really want to embarrass yourself? (y / n)")


def is_one_digit(v):
    return bool(10 > v > -10 and int(v) == v)


def check(v1, v2, v3):
    msg_ = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg_ = msg_ + msg[6]
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg_ = msg_ + msg[7]
    if (v1 == 0 or v2 == 0) and (v3 in ['*', '+', '-']):
        msg_ = msg_ + msg[8]
    if msg_ != '':
        msg_ = msg[9] + msg_
        print(msg_)


memory = 0
while True:
    print(msg[0])
    calc = input()
    calc = calc.split(" ")
    try:

        if calc[0] == 'M':
            x = memory
        else:
            x = float(calc[0])
        if calc[2] == 'M':
            y = memory
        else:
            y = float(calc[2])
    except ValueError:
        print(msg[1])
    else:
        operand = calc[1]
        check(x, y, operand)
        if operand == '+':
            result = x + y
        elif operand == '-':
            result = x - y
        elif operand == '*':
            result = x * y
        elif operand == '/':
            try:
                result = x / y
            except ZeroDivisionError:
                print(msg[3])
                continue
            else:
                pass
        else:
            print(msg[2])
            continue
        print(result)
        while True:
            print(msg[4])
            answer = input()
            if answer == 'y':
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        print(msg[msg_index])
                        answer = input()
                        if answer == 'y':
                            if msg_index < 12:
                                msg_index += 1
                            else:
                                memory = result
                                break
                        if answer == 'n':
                            break
                else:
                    memory = result
                break
            if answer == 'n':
                break
        while True:
            print(msg[5])
            answer = input()
            if answer == 'y':
                break
            if answer == 'n':
                exit()
