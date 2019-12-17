def print_class_method(class_input):
    for i in class_input.__dir__():
        if not i.startswith('_'):
            print(i)


if __name__ == "__main__":
    print_class_method(set())