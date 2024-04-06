if __name__ == '__main__':
    person = {"li":18,"wang":50,"zhang":20,"sun":22}
    max_age = 0
    for key, value in person.items():
        if value > max_age:
            max_age = value
            name = key
    print("The oldest gay is %s. His age is %d." %(name, max_age))