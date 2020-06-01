# First class function - passing function as a parameter
def hello():
    print("Hello, World")

def polo(hell):
    hell()

polo(hello)