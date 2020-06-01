# Closure
def green():
    name = "John"
    base = 23
    def hello():
        print(f"Hello, {name}")
    return hello

# print(green())

red = green()
blue = green()
yello = green()

red()
blue()
yello()