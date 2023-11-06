import functools

# Let's look into the confusing syntax
# Do note that this features can be achieves using if-else too but decorator helps in clean code
user = {"role": "user"}


# check_admin is a decarator and grant access becomes a wrapper real life example is to check whether an user is logged in or not
def check_admin(func1):
    def grant_access():
        if user.get("role") == "admin":
            return func1()

    return grant_access


# Some logic to show admin page
def show_password():
    """
    Allows us to retrieve passwords
    """
    return "your password is 1234"


admin_page = check_admin(show_password)
print(admin_page())
print(show_password.__name__)
print(show_password.__doc__)

# This Syntax is very confusing let's look into something that is used a lot @syntax
# Check for login
logged_in = False


def decator_function(func_to_be_executed):
    @functools.wraps(func_to_be_executed)
    def wrapper():
        """
        Inside wrapper function
        """
        if logged_in:
            func_to_be_executed()
        else:
            print("Go to Register Page")

    return wrapper


@decator_function  # internally :-> my_function = decator_function(my_function)
def my_function():
    """
    Inside my_function
    """
    print("Already Registered")


# Before using @syntax
# check_loggee = decator_function(my_function)
# check_loggee()
my_function()
print(my_function.__name__)
print(my_function.__doc__)

# So Whatever function which will be decaroted by @syntax will be replaced by the wrapper function and __name__ or __doc__ will now point to wrapper function
# So how can we keep functions metadata using functools

# Let's say we want to pass arguments as well so we have pass arguments to so we have to pass the argument in wrapper function and the func_to_be_executed as well which will make that decorator usage consize to only one function as there may be another function which uses the same decarator but didn't get any arguments


# Now here access level is hard coded but what if we want to pass access level as a argument something like @decarator(access level) just like inception one level deep
def third_level(access_level):
    def check_admin(func1):
        @functools.wraps(func1)
        def grant_access():
            if user.get("role") == access_level:
                return func1()

        return grant_access

    return check_admin


# Some logic to show admin page
@third_level("user")
def show_password():
    """
    Allows us to retrieve passwords
    """
    return "your password is 1234"


print(show_password())
print(show_password.__name__)
print(show_password.__doc__)


# args and kwargs for functions
def add(*args):
    return sum(args)


def pretty_print(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")


print(add(1, 2, 3, 4, 5))
pretty_print(**{"username": "joseh123", "value": 25})

# to make generic decorators just pass *args, **kwargs in decorator and wrapper and returning functions
