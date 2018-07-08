def use_log(func):
    # print("In log")
    def wrapper(*args, **kwargs):
        print("Function name %s" % func.__name__)
        return func(*args)

    return wrapper


@use_log
def foo():
    print("foo")


@use_log
def bar():
    print("bar")


def decorator_a(func):
    print("decorator_a")
    print('func id: ' + str(id(func)))
    return func

def decorator_b(func):
    print("decorator_b")
    print('func id: ' + str(id(func)))
    return func

print('Begin declare foo with decorators')
@decorator_a
@decorator_b
def foo():
    print("foo")
print('End declare foo with decorators')

print('First call foo')
foo()
print('Second call foo')
foo()
print('Function infos')
print('decorator_a id: ' + str(id(decorator_a)))
print('decorator_b id: ' + str(id(decorator_b)))
print('fooid : ' + str(id(foo)))


#if __name__ == "__main__":
    #foo()
    #bar()