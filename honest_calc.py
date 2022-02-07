# write your code here

def get_equation(memory):
    print("Enter an equation")
    x, operation, y = input().split(" ")
    try:
        x = float(x) if "." in x else (
            int(x) if "M" not in x and memory != 0.0 else float(x.replace("M", str(memory))))
        y = float(y) if "." in y else (int(y) if "M" not in y and memory != 0.0 else float(y.replace("M", str(memory))))
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
        return ""
    if operation not in ["+", "-", "/", "*"]:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        return ""
    check(x, y, operation)
    return x, operation, y


def store_result(result_computed):
    print("Do you want to store the result? (y / n):")
    store = input()
    msgs = ["Are you sure? It is only one digit! (y / n)",
            "Don't be silly! It's just one number! Add to the memory? (y / n)",
            "Last chance! Do you really want to embarrass yourself? (y / n)"]
    if store not in ["y", "n"]:
        return store_result(result_computed)
    elif store == "y":
        if is_one_digit(float(result_computed)):
            msg_index = 0
            while True:
                print(msgs[msg_index])
                answer = input()
                if answer == "y":
                    if msg_index < 2:
                        msg_index += 1
                        continue
                    else:
                        return float(result_computed)
                else:
                    if answer == "n":
                        return 0.0
            return 0.0
        else:
            return float(float(result_computed))
    else:
        return 0.0


def another_calcul():
    print("Do you want to continue calculations? (y / n):")
    proceed = input()
    if proceed not in ["y", "n"]:
        return another_calcul()
    elif proceed == "y":
        return True
    else:
        return False


def is_one_digit(value):
    value = float(value)
    return -10 < value < 10 and value.is_integer()


def check(x_value, y_value, operation_value):
    msg = ""
    if is_one_digit(x_value) and is_one_digit(y_value):
        msg += " ... lazy"
    if (x_value == 1 or y_value == 1) and operation_value == "*":
        msg += " ... very lazy"
    if (x_value == 0 or y_value == 0) and (operation_value == "*" or operation_value == "+" or operation_value == "-"):
        msg += " ... very, very lazy"
    if msg != "":
        msg = "You are" + msg
        print(msg)


def apply_operation(memory_argument):
    try:
        x, operation, y = get_equation(memory_argument)
    except ValueError:
        return ""

    result = 0.0

    if operation == "/":
        try:
            result = x / y
        except ZeroDivisionError:
            print("Yeah... division by zero. Smart move...")
            return apply_operation(memory_argument)
    elif operation == "+":
        result = x + y
    elif operation == "-":
        result = x - y
    elif operation == "*":
        result = x * y

    print(float(result))
    stored_result = store_result(result)
    if stored_result == 0.0:
        pass
    else:
        memory_argument = stored_result
    while another_calcul():
        return apply_operation(memory_argument)
    else:
        return ""


memory_value = 0.0
print(apply_operation(memory_value))
