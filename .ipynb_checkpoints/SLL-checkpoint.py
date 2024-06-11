class Node:
    def __init__(self, item= None, next = None):
        self.item = item
        self.next = next


class SLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):   # creating iterator
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


class SLL:
    def __init__(self, start = None):
        self.start = start

    def is_empty(self):
        return self.start == None


    def insert_at_start(self, item):
        n = Node(item, self.start)
        self.start = n

    def insert_at_last(self, item):
        n = Node(item)

        if not self.is_empty():
            temp = self.start
            while(temp.next is not None):
                temp = temp.next
            temp.next = n
        else:
            self.start = n        
        
    def search(self,val):
        temp = self.start
        if not self.is_empty():
            while(temp.next is not None):
                if(temp.item == val):
                    return temp
                temp = temp.next

        return None

    def insert_after(self, item, temp):
        if temp is not None:
            n = Node(item,temp.next)
            temp.next = n

    def print_list(self):
        temp = self.start
        while(temp is not None):
            print(temp.item, end=" ")
            temp= temp.next


    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while (temp.next.next is not None):
                temp = temp.next
            temp.next = None

    def delete_item(self,item):
        if self.start is None:
            pass
        elif self.start.next is None :
            if self.start.item == item:
                self.start = None
        else:
            temp = self.start
            if temp.item == item:
                self.start =  temp.next
            else:
                while( temp.next is not None):
                    if(temp.next.item == item):
                        temp.next = temp.next.next
                        break                        
                    temp = temp.next

    def __iter__(self):
        return SLLIterator(self.start)
                
            