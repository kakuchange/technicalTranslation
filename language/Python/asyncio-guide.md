## 首先, 这是更新此项目后的第一篇, 有些事还是要提前说明: 

1. 此系列的文章, 多为零散的技术文章. 

2. 已经不再是纯翻译(考虑对英语的表达习惯如果直译, 会不通顺, 再全篇润色翻译又有些浪费精力). 改为技术性的**总结**, 会配以原文说明问题. 

3. 这篇是对asyncio的一篇指南guide. 我默认你已了解相关知识, 如果不的话, 请看看相关概念介绍再看这篇.

原文地址: [A guide to asynchronous programming in Python with asyncio](https://medium.freecodecamp.org/a-guide-to-asynchronous-programming-in-python-with-asyncio-232e2afa44f6)

对于(I/O)异步编程, 目前我了解到的主要有两种实现方式: 1. 多线程/多进程, 如 threading/multiprocess/concurrent 2. 基于事件循环的实现, 如:asyncio. 这里先简单提一下, 关于两的区别, 后面我会在跟进一篇说明的. 这里先介绍asyncio. 

# 首先什么是asynchronous?

原文举例说, 你某个程序要请求3个服务器, 依次得到响应结果, 如果一个接一个执行(请求-拿到结果-再请求-拿结果...)会很容易理解. 但如果其中某一个请求, 由于网络或某种原因得到响应很慢, 这时整个程序是**阻塞**的. 程序没有做任何事情! 如果你希望在没有响应时做点什么, 而非一直等着, (这是异步的核心!)你需要异步代码来完成这三次调用. 所以理解异步的关键在于**非阻塞**.

明白了这一点, 后面的问题就好交待了. 如果没有或很少有I/O操作(网络I/O, 磁盘I/O), 你是不需要写异步代码的.

~~其次, 有一点需要说明, 程序在某种程度上都是**阻塞**的, 在执行时.(针对单个线程而言)都需要耗时, 在这一步的程序执行时, 只是CPU从磁盘或网络读写数据相较内存极慢, 所以说这两种IO操作阻塞~~

asyncio中基本组成:

**Coroutine** — generator that consumes data, but doesn’t generate it. Python 2.5 introduced a new syntax that made it possible to send a value to a generator. I recommend checking David Beazley’s “[A Curious Course on Coroutines and Concurrency](http://www.dabeaz.com/coroutines/Coroutines.pdf)” for a detailed description of coroutines.(协程, 如果你不了解这个概念, 暂且不要看这篇, 可能你会很困惑, ~~它是可反复进入, 退出的函数~~, 你可暂且这么理解. 上面的链接很经典, 值得一看)

**Tasks** — schedulers for coroutines. If you check a source code below, you’ll see that it just says event_loop to run its _step as soon as possible, meanwhile _step just calls next step of coroutine. 事件循环调度的对象, 下面是相关代码

```
class Task(futures.Future):  
    def __init__(self, coro, loop=None):
        super().__init__(loop=loop)
        ...
        self._loop.call_soon(self._step)
    def _step(self):
            ...
        try:
            ...
            result = next(self._coro)
        except StopIteration as exc:
            self.set_result(exc.value)
        except BaseException as exc:
            self.set_exception(exc)
            raise
        else:
            ...
            self._loop.call_soon(self._step)
```

**Event Loop**— think of it as the central executor in asyncio.(asyncio的调度中心)

之前说过了,对于单线程而言, 你是无法在阻塞时做其实的事情(多线程可以实现异步程序), 但asyncio基于事件循环的不同, 具体看下面的图.

![](../../resources/img/asyncio1.jpg)

从图中你可看出:

- The event loop is running in a thread
- It gets tasks from the queue
- Each task calls the next step of a coroutine
- If coroutine calls another coroutine (await \<coroutine\_name\>)the current coroutine gets suspended and context switch occurs. Context of the current coroutine (variables, state) is saved and context of a called coroutine is loaded.
- If coroutine comes across a blocking code(I/O, sleep), the current coroutine gets suspended and control is passed back to the event loop.
- Event loop gets next tasks from the queue 2,...n
- Then the event loop goes back to task 1 from where it left off.

(感觉说的已经很明白了, 还是略翻一下:)

- 事件循环是跑在(主)线程
- 从队列中取task
- 每个task 调用(next step of a coroutine)
- 如果这个coroutine 中调用了另一个coroutine (类似于await \<coroutine\_name\>), 则当前coroutine 挂起并切换上下文(原: context switch orccurs. 对上下文概念这里不做说明, 自行了解), 当前context is saved and context of a called coroutine is loaded.
- 如果coroutine 发生阻塞(I/O, sleep), 当前coroutine 挂起, 程序控制权回到事件循环(event loop)
- 事件循环从队列中取出下一个task, 2,...,n
- then the event loop goes back to task 1 from where it left off.

# Asynchronous vs. Synchronous Code

(举例对比, 但我觉得对我来讲已经比较熟了, 不做翻译)

Let’s try to prove that asynchronous approach really works. I will compare two scripts, that are nearly identical, except the sleep method. In the first one I am going to use a standard time.sleep, and in the second one — asyncio.sleep.

Sleep is used here because it is the simplest way to show the main idea, how asyncio handles I/O.

Here we use synchronous sleep inside async code:

```python3
import asyncio  
import time  
from datetime import datetime

async def custom_sleep():  
    print('SLEEP', datetime.now())
    time.sleep(1)
async def factorial(name, number):  
    f = 1
    for i in range(2, number+1):
        print('Task {}: Compute factorial({})'.format(name, i))
        await custom_sleep()
        f *= i
    print('Task {}: factorial({}) is {}\n'.format(name, number, f))

start = time.time()  
loop = asyncio.get_event_loop()
tasks = [  
    asyncio.ensure_future(factorial("A", 3)),
    asyncio.ensure_future(factorial("B", 4)),
]
loop.run_until_complete(asyncio.wait(tasks))  
loop.close()
end = time.time()  
print("Total time: {}".format(end - start))
```

**Output:**

```
Task A: Compute factorial(2)  
SLEEP 2017-04-06 13:39:56.207479  
Task A: Compute factorial(3)  
SLEEP 2017-04-06 13:39:57.210128  
Task A: factorial(3) is 6
Task B: Compute factorial(2)  
SLEEP 2017-04-06 13:39:58.210778  
Task B: Compute factorial(3)  
SLEEP 2017-04-06 13:39:59.212510  
Task B: Compute factorial(4)  
SLEEP 2017-04-06 13:40:00.217308  
Task B: factorial(4) is 24
Total time: 5.016386032104492
```

Now the same code, but with the asynchronous sleep method:

```python3
import asyncio  
import time  
from datetime import datetime

async def custom_sleep():  
    print('SLEEP {}\n'.format(datetime.now()))
    await asyncio.sleep(1)
async def factorial(name, number):  
    f = 1
    for i in range(2, number+1):
        print('Task {}: Compute factorial({})'.format(name, i))
        await custom_sleep()
        f *= i
    print('Task {}: factorial({}) is {}\n'.format(name, number, f))

start = time.time()  
loop = asyncio.get_event_loop()
tasks = [  
    asyncio.ensure_future(factorial("A", 3)),
    asyncio.ensure_future(factorial("B", 4)),
]
loop.run_until_complete(asyncio.wait(tasks))  
loop.close()
end = time.time()  
print("Total time: {}".format(end - start))
```

**Output:**

```
Task A: Compute factorial(2)  
SLEEP 2017-04-06 13:44:40.648665
Task B: Compute factorial(2)  
SLEEP 2017-04-06 13:44:40.648859
Task A: Compute factorial(3)  
SLEEP 2017-04-06 13:44:41.649564
Task B: Compute factorial(3)  
SLEEP 2017-04-06 13:44:41.649943
Task A: factorial(3) is 6
Task B: Compute factorial(4)  
SLEEP 2017-04-06 13:44:42.651755
Task B: factorial(4) is 24
Total time: 3.008226156234741
```

我这里解释下为什么后者会比前者快2S?  
首先, custom_sleep被调用做了2件事: print一句; sleep一秒.  
其次, task都是range(2, number+1), 2个task, 一个调用2次, 一个调用3次.

第三点, time.sleep是会挂起当前线程的, 真正的sleep...(in fact, because of standard sleep, the current thread releases a Python interpreter, and it can work with other threads if the exist, but that is another topic.). 而asyncio.sleep是异步调用sleep, 这么说你可能有些困惑. 它本质上也是一个coroutine 如同前面图所示的执行流程它也适用.

所以, 同步的sleep, 5次调用真正的sleep了5秒, 从输出(taskA-2-3, taskB-2-3-4)也可以看出. 而对于异步的asyncio.sleep而言, 就像上面图示的那样, 在发生阻塞时(如果没有再调用别的coroutine)调用其它tasks, 从输出可以看出(taskA2-taskB2, taskA3-taskB3, taskB4), 在taskA2阻塞时调用taskB2, 再阻塞(就等着唄, 没有其它task需要被调度)

# Several reasons to use asynchronous programming

Facebook 大量使用异步编程, 例如, 它们的Reactive Native and RocksDB software use asynchrnous operatioins. 不然Twitter 如何处理超过5 billion sessions a day?

重构你的代码(可以从异步代码中获益的部分), 如果能让你的代码更快些, 这很值得尝试.

另,有个老哥的评论有些有用信息, 贴上:

Thanks for the intro to asyncio, which I knew but never really tried or looked at seriously. That’s very helpful.

You also explain the needs & whys of async paradigm in a very clear way.

However, you don’t mention a few things. First, there are several async framework in Python, such as gevent, that compete with asyncio. I guess there are pros and cons, maybe asyncio is by far the best, but how to choose ? (Tornado is there too).

Furthermore, I think your conclusion is right but lacks details. If you have a large app in Django, how to make it asynchronous ? It’s actually not trivial, and Channels are here to help but still.

And finally, I think that if you know your service will heavily be asynchronous-oriented and don’t have legacy code, it is worth looking at other languages, such as Javascript with Node.js or Golang. They are “born” asynchronous, so probably a better fit than Python.

(这一段是我加的)好吧, 我又双叕看了一篇软广, 然后推荐了一个社区, 一个博客. 我去看了, 里面并没有我想要的进一步关于asyncio的说明. 源码我大楖看了不少, 但还缺一个提纲类的东西, 能从大的方面讲解一下的. 这篇文章, 说的内容和我之前了解猜测的相互应证了. 

之后看文章, 先大体速览一篇, 老外也不地道的...

贴上: [“I don’t even feel like I’ve scratched the surface of what I can do with Python”](https://realpython.com/products/python-tricks-book/)

唯一有用的信息: 
```python3
a = {'a': 0}
b = {'b': 1}
c = {**a, **b}
print(c)
{'a': 0, 'b': 1}
```