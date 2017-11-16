# basic as you like. Hopefully demonstrates the issue
# thirst may be affecting my choice in test cases here

def pour_tea(with_milk=False, sugars=0):
    tea_string = "White tea" if with_milk else "Black tea"
    if sugars > 0:
        tea_string += " and {} sugar{}".format(sugars, 's' if sugars > 1 else '')
        if sugars >= 20:
            tea_string += "... This drink will probably make you ill. Please reconsider"
    return tea_string

if __name__ == '__main__':
    # run this in the terminal. It will run fine
    print pour_tea()
    print pour_tea(True)
    print pour_tea(True, 2)
    print pour_tea(True, 42)
