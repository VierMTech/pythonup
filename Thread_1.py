import threading
import time
from queue import Queue

class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n, out_q):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            out_q.put(n)            
            time.sleep(1)

#開啟一個queue，發送訊息給main thread 用的
q = Queue()
#啟動一個倒數計時的TASK
c = CountdownTask()
#設置啟動，目標是run，傳入參數10及queue，Daemon要使用，跟主thread一同關閉
t = threading.Thread(target=c.run, args=(10,q), daemon=True)
#thread啟動
t.start()

#c.terminate() # Signal termination
#t.join()      # Wait for actual termination (if needed)

#設置計數器等於零(給main thread用)
counter = 0
while 1:	
	if counter > 50:
		c.terminate()#當>50關閉thread
		break
	counter += 1	#計數器+1
	#print('Queue.qsize()A',q.qsize())	#用於顯示柱列現在有沒有東西
	if q.qsize() > 0:	#柱列內有東西，取出來
		print('main loop ' , counter , ' counter :' , q.get())	#取出柱列的資料
	
	time.sleep(.1)




