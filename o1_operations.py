class MyQueue:

    def __init__(self):
        self.queue = []
    
    def push(self, x: int) -> None:
        self.queue.append(x)            

    def pop(self) -> int:
        ret_val = self.queue.pop(0)
        return ret_val

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0        

# More efficient solution:


class MyQueue:

    def __init__(self):
        self.queue = []
        self.indexes = {}
        self.deleted_count = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
    
    def pop(self) -> int:
        
        deleted_value = self.queue[self.deleted_count]
        # Do a logic deletion of the value
        self.queue[self.deleted_count] = -1

        # Increment the deleted_count
        self.deleted_count += 1
        return deleted_value

    def peek(self) -> int:
        return self.queue[self.deleted_count]

    def empty(self) -> bool:
        return len(self.queue) - self.deleted_count == 0        
