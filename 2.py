def sum(a, b):
    return a + b


def cmp(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("На ноль делить нельзя")
        return None

def Dis(a, b, c):
    if b**2-4*a*c>0:
        return (-b+(b**2-4*a*c)**0.5)/2*a
        return (-b-(b**2-4*a*c)**0.5)/2*a
    elif b**2-4*a*c==0:
        return (-b+(b**2-4*a*c)**0.5)/2*a
    else:
        print("Нет корней")
        return None


def start():
    print("Укажите интересющую вас операцию: ")
    print("* - умножение")
    print("/ - деление")
    print("+ - сложение")
    print("- - вычитание")
    print("D - дискриминант")

    operation = input("Укажите операцию: ")

    a = input("Введите первое число (коэффициент, если требуется): ")
    b = input("Введите второе число (коэффициент, если требуется): ")
    if operation=="D":
        c = input("Введите третье число (коэффициент, если требуется): ")

    # добавить преобразование a и b в int
    try:
        a = int(a)
        b = int(b)
        if operation == "D":
            c = int(c)
    except ValueError:
        print("Введено неверное значение")
        return
    else:
        result = 0
        if operation == "*":
            result = mul(a, b)
        elif operation == "+":
            result = sum(a, b)
        elif operation == "-":
            result = cmp(a, b)
        elif operation == "/":
            result = div(a, b)
        elif operation == "D":
            result = Dis(a, b, c)
        else:
            print("Неверная операция")
        if operation == "D":
            print(f"D={a}x**2{b}x{c}={result}")
        else:
            print(f"{a}{operation}{b}={result}")


start()