from time import sleep
import time as timedo

time_sleep = 0.01
time = timedo.perf_counter()
def get_time(t):
    return (t - time)

def ft_progress(lst):
    for e, i in zip(lst, range(len(lst))):
        yield e
        taime = get_time(timedo.perf_counter())
        pr_por = i * 100 / int(len(lst))
        por = i * 100 // int(len(lst))
        hora = time_sleep * float(len(lst)) - taime
        if (hora < 0):
            hora = time_sleep * float(len(lst))
        s = "[" + '+' * (por // 5) + ' ' * int((100 - por) // 5) + "]"
        print(f"\rtiempo para nandear: {hora:.2f}s porcentaje para nandas: {pr_por:.2f}% barrita de nandeo: {s} esperado para nandear: {taime:.2f}", end='', flush = True)

        


if __name__ == "__main__":
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(time_sleep)

    print()
    print(ret)
