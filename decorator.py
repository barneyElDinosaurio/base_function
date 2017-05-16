import logging


def get_parameter(func):
    print "IN GET PARAMETER"

    def new_func():
        print "inside new func"
        return func()

    print "END GET PARAMETER"
    return new_func


@get_parameter
def show_function():
    print "SHOW Function"
    return "HELLO"


# a=show_function
#a()
#get_parameter()
#a=show_function()
#print a
if __name__ == "__main__":
    #logging.info("Test")
    print "Test"
    #show_function()