import time


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f'Время работы: {dt} c.')
        return dt

    return wrapper

@test_time
def for_each(l):
    for elem in l:
        print(elem)

@test_time
def for_(l):
    for i in range(len(l)):
        print(l[i])




if __name__=='__main__':
    # l=[x for x in range(1000000)]
    # time1=for_each(l)
    # time2= for_(l)
    # print(time1, time2)
    # print(time1/time2)
    time1=10.85208511352539
    time2=10.906313180923462
    time2=10.85308511352539
    circ=((time1 - time2) / time1)*100
    print(f'{circ}%')


