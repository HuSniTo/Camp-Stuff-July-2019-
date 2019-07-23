def main():
    verb = input("Type a verb: ")
    verb2 = input("Type another verb: ")
    place = input("Type a place (example: Japan) ")
    name = input("Enter a name: ")
    print ("{} was {} for his friend to {} in {}".format(name, verb, verb2, place))
if __name__ == "__main__":
        main()