def use_log(func):
    # print "In log"
    def wrapper(*args, **kwargs):
        print "Function name %s" % func.__name__
        return func(*args)

    return wrapper


@use_log
def foo():
    print "foo"


@use_log
def bar():
    print "bar"


if __name__ == "__main__":
    foo()
    bar()