def some_gen():
    print('start')
    yield 1
    print('middle')
    yield 2
    print('end')

gen = some_gen()
print(gen)

print(gen.gi_code.co_code)
print(gen.gi_frame.f_lasti)
next(gen)
print(gen.gi_frame.f_lasti)
next(gen)
print(gen.gi_frame.f_lasti)
next(gen)
