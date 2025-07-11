def log(filename=None):
    def log_decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            try:
                result = function(*args, **kwargs)
                message = f"{function.__name__} ok"
                if filename is None:
                    print(message)
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message)
                return result
            except Exception as e:
                message = f"{function.__name__} error: {type(e).__name__}. Inputs: {args}, {{}}"
                if filename is None:
                    print(message)
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message)
                raise e
        return wrapper
    return log_decorator
