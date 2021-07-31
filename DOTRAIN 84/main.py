import time


def main():
    while True:
        try:
            print("testing...")
            time.sleep(1)
        # Local Exception
        except SyntaxError:
            print("Syntax Error")
        except ZeroDivisionError:
            print("Chia cho 0")


if __name__ == '__main__':
    try:
        main()
    # Global Exception
    except KeyboardInterrupt:
        print("Ngat chuong trinh")
    except Exception:
        print("Another Exception")
