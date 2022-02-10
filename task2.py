import mmap
from concurrent.futures import ProcessPoolExecutor
import time 
values = []
for i in range(100):
    values.append(int(i))
def cube(x):
    start = time.time()
    with open('cubes_threaded.txt', 'w') as f:
        f.write(str(x*x*x)+str(' '))
        print(f'Cube of {x}:{x*x*x}')
    end = time.time()
    print("One thread timing :",str(end-start))
def normalcube(x):
    with open('cubes.txt', 'w') as f:
        f.write(str(x*x*x)+str(' '))
        f.write(str(x*x*x)+str(' '))

if __name__ == '__main__':
    print("Multithreaded I/O Writing operation starts ...")
    result =[]
    start = time.time()
    values=[]
    for i in range(1,30):
        values.append(i)
    with ProcessPoolExecutor(max_workers=5) as exe:
        exe.submit(cube,2)
        result = exe.map(cube,values)
    end = time.time()
    print("Multi-threaded Timing : "+str(end-start))
    print("Multithreaded I/O Writing operation ends ...")
    print("Normal I/O Writing operation starts ...")
    start = time.time()
    with open('cubes_normal.txt', 'w') as f:
        for i in range(1,30):
            f.write(str(i*i*i)+str(' '))
            f.write(str(i*i*i)+str(' '))
    end = time.time()
    print("Normal I/O Writing operation ends ...")
    print("Normal I/O writing operation timing : "+str(end-start))
