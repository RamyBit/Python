def repeat(n):
    def outer(func):
        counter = 0
        cached = {}

        def inner(x):
            for i in range(0, n):
                if x in cached:
                    print('wurde von cache gerechnet')
                    return cached[x]

                nonlocal counter
                counter += 1
                print('Inner wurde ausgefuhrt:' + str(counter))
                result = func(x)
                cached[x] = result
            return result
        return inner
    return outer


@repeat(5)
def calculate_x(x):
    print('calculate_x (' + str(x)+')')
    return x * x

print(calculate_x(5))
print(calculate_x(5))
print(calculate_x(4))
print(calculate_x(3))