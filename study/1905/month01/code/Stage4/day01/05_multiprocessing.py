import redis
import time
import random
from multiprocessing import Process


class Spider(object):
    def __init__(self):
        self.r = redis.Redis(host='127.0.0.1',port=6379,db=0)

    # 生产者 - 进程函数
    def product(self):
        for page in range(67):
            url = 'http://app.mi.com/category/2#page={}'.format(page)
            self.r.lpush('xiaomi:spider', url)
            time.sleep(random.randint(1, 3))

    # 消费者 - 进程事件函数
    def consumer(self):
        while True:
            # url:(b'xiaomi:spider',b'http://app.mi.com/category/2#page=0')
            url = self.r.brpop('xiaomi:spider', 4)
            if url:
                print('正在抓取', url[1].decode())
            else:
                print('抓取结束')
                break

    # 主函数
    def run(self):
        p1 = Process(target=self.product)
        p2 = Process(target=self.consumer)
        p1.run()
        p2.run()


if __name__ == "__main__":
    spider = Spider()
    spider.run()
