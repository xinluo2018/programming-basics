## 多进程编程， 采用.py文件运行, 
## 在windows环境.ipynb文件中，进程内函数中print()失效。

import time
import numpy as np
from glob import glob
from multiprocessing import Process, Pool

def task(i_process):
    print(f"第{i_process}个进程在运行")  ## 该功能在windows环境下使用.ipynb文件会有问题
    time.sleep(1)

# ## 创建单个进程
# if __name__ == "__main__":
#     print("主进程开始运行")    
#     p = Process(target=task, args=(1,))
#     p.start()  # 启动进程
#     p.join()   # 等待子进程结束
#     print("子进程是否仍在运行:", p.is_alive())
#     print("主进程结束运行")


# ### 创建多个进程
# if __name__ == "__main__":
#     process_list = []
#     for i in range(5):
#       p = Process(target=task, args=(i,))
#       p.start()  # 启动进程
#       process_list.append(p)
#     for p in process_list:
#       p.join()   # 等待子进程结束
#     print('进程运行结束')


### 单进程 vs. 多进程 (数据计算)
def compute_data(paths):
    data = []
    for path in paths:
        arr = np.load(path)  # 读取数据
        arr = ((arr**10) **10)**10  # 复杂计算
        data.append(arr)
    return len(data)

paths = glob('第7章-并发编程/data/*.npy')  # 获取所有数据文件路径

# if __name__ == '__main__':
#     # 创建一组计算任务
#     start_time = time.time()  # 记录开始时间    
#     # 单进程顺序计算
#     num_data = compute_data(paths)  # 测试函数
#     total_time = time.time() - start_time
#     print(f"\n总耗时: {total_time:.2f}秒")


### !!如要求返回函数结果，需用进程池Pool
if __name__ == '__main__':
    # 相同的计算任务
    paths_list = [paths[i::3] for i in range(3)]  # 将路径分成3份
    start_time = time.time()    
    # # 多进程并行计算
    processes = []
    for paths in paths_list:
        p = Process(target=compute_data, args=(paths,))
        processes.append(p)
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    total_time = time.time() - start_time
    print(f"\n总耗时: {total_time:.2f}秒") 

