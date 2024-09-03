import multiprocessing
import datetime


file_list = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            all_data.append(file.readline())
            if not file.readline():
                break
'''start = datetime.datetime.now()
for x in file_list:
    read_info(x)
end = datetime.datetime.now()
print(end - start)'''  #0:00:07.063824

if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_list)
    end = datetime.datetime.now()
    print(end - start) #0:00:00.248108


