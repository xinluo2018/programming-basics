###-----------------------------------------------------###
## 扩展学习部分：多进程编程中进程池Pool使用，以及队列Queue使用
###-----------------------------------------------------###

import time
import numpy as np
from glob import glob
from multiprocessing import Process, Pool, Queue


### 使用进程池Pool
### apply_async()方法，相比不使用进程池方法（a）可以简单直接获取函数返回值，（b）代码更加简洁高效
## 1. 简单示例
# def task(i_process):
#     print(f"第{i_process}个进程在运行")  
#     time.sleep(1)
# if __name__ == '__main__':
#     with Pool(processes=3) as pool:
#         for i in range(3):
#             proc_result = pool.apply_async(task, args=(i,)) # 异步提交任务
#         pool.close()  ## 关闭进程池，表示不再接受新任务
#         pool.join()   ## 等待所有支进程结束
#     print('所有进程运行结束')

### 2. 具体数据处理示例
###  数据计算任务
# def compute_data(paths):
#     print('子进程计算开始')
#     data = []
#     for path in paths:
#         arr = np.load(path)  # 读取数据
#         arr = ((arr**10) **10)**10  # 复杂计算
#         data.append(arr)
#     print('子进程计算完成')
#     return len(data)

# if __name__ == '__main__':
#     paths = glob('第7章-并发编程/data/*.npy')  # 获取所有数据文件路径
#     ## 将所需处理数据等分为3份
#     paths_list = [paths[i::3] for i in range(3)]  
#     start_time = time.time()    
#     # # 多进程并行计算
#     with Pool(processes=3) as pool:
#         proc_results = []
#         for paths in paths_list:
#             proc_result = pool.apply_async(compute_data, args=(paths,))  # 异步提交任务
#             proc_results.append(proc_result)
#         # 获取每个子进程返回结果
#         output = [r.get() for r in proc_results]
#         ### !!多进程编程需显示关闭进程池和等待所有支进程结束，
#         ### !!多线程编程不用
#         pool.close()  ## 关闭进程池，表示不再接受新任务
#         pool.join()   ## 等待所有支进程结束
#     total_time = time.time() - start_time
#     print(f"\n总耗时: {total_time:.2f}秒")


# ### 使用Queue队列, 实现多进程间通信与交互
# ## 生产者函数：将结果放入队列
# def producer_task(queue):
#     result = 'producer进程计算结果'
#     queue.put(result)  # 将结果放入队列

# ## 消费者函数：从队列获取结果
# def consumer_task(queue):
#     result = queue.get()  # 从队列获取结果
#     print(f"consumer队列获取结果: {result}")

# if __name__ == '__main__':
#     ## 将所需处理数据等分为3份
#     paths_list = [paths[i::3] for i in range(3)] 
#     start_time = time.time()    
#     # 创建队列
#     queue = Queue()
#     # 创建进程
#     producer_process = Process(target=producer_task, args=(queue,))
#     consumer_process = Process(target=consumer_task, args=(queue,))
#     # 启动进程
#     producer_process.start()
#     consumer_process.start()
#     # 等待进程结束
#     producer_process.join()
#     consumer_process.join()
#     # 创建消费者进程获取结果
#     total_time = time.time() - start_time
#     print(f"\n总耗时: {total_time:.2f}秒") 

