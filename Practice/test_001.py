class Fib:
    def __init__(self):
        self.memo = {}

    def fibonacci(self, num):
        if num == 1:
            return 1
        return fibonacci(num - 1) + fibonacci(num - 2)


def main():
    print(fibonacci(10))  # should return 55


if __name__ == "__main__":
    main()
