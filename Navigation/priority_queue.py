#smallest priortiy first
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, object, priority):
        #empty queue
        if len(self.queue) == 0:
            self.queue.append((object, priority))
            return
        
        #Non-empty queue
        for i in range(0, len(self.queue)):
            if priority <= self.queue[i][1]:
                self.queue.insert(i, (object, priority))
                return
            
        self.queue.append((object, priority))

    def pop(self):
        return self.queue.pop(0)
