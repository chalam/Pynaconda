def do_stuff(loop):
    print('stuff', loop)

first_pass = True
while first_pass or condition:
    first_pass = False
    do_stuff('do-while')
    condition = False

condition = True
while condition:
    do_stuff('while')
    condition = False


