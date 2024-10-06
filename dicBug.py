def get_dictionary_value(my_dict, key):
    return my_dict[key]

def main():
    my_dict = {"name": "John", "age": 30}
    key = "city"
    value = get_dictionary_value(my_dict, key)
    print(value)

if __name__ == "__main__":
    main()
