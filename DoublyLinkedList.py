##Doubley Linked List Demonstration

##Austin Shane
##19 March 2020

##Algorithm:
# DoublyLinkedList.py contains two classes, the node class, and the LinkedList class. Importing DoublyLinkedList.py allows the user to create a doubly linked list
# and perform various operations on it. These include: determining whether the doubly linked list(DLL) is empty (is_empty), the size of the DLL (size),
# adding new items to the head (add), appending new items to the end (append), removing and returning the last item of the DLL (pop), search for
# an item in the DLL (search), and remove an item (remove). This allows the user to effectively manage a doubly linked list.


class Node(object):
    def __init__(self, data, next = None, previous = None): #next and previous set to none by default
        '''initilization for data, next, and previous'''
        self.data = data #sets self.data
        self.next = next #sets self.next
        self.previous = previous #sets self.previous

    def __str__(self):
        '''returns node data'''
        return self.data #returns node data


class DoublyLinkedList(object):
    def __init__(self, head = None, tail = None): #head and tail set to none by default
        '''initializes head and tail of doubly linked list'''
        self.head = head #sets head
        self.tail = tail #sets tail

    def is_empty(self):
        '''determines whether list is empty, returns true if it is, false if not'''
        if self.head == None: #if head does not exist then list is empty
            to_return = True #return that it is true the list is empty
        else:
            to_return = False #if not then list must have items, not empty: false
        return to_return #returns true/false

    def size(self):
        '''determines the number of nodes/items in the list'''
        if DoublyLinkedList.is_empty(self) == True: #if is_empty returns true then list length is 0
            to_return = 0
        else:
            current = self.head #current is self.head
            size = 0 #set size to 0
            while current: #loop through nodes
                size = size + 1 #add one to compensate for starting at 0
                current = current.next #go to next node
            to_return = size
        return to_return #returns size

    def add(self, item):
        '''adds a node to the head of the list'''
        new_node = Node(item) #create new node
        new_node.next = self.head #sets (old) head forward one
        self.head = new_node #new head is new_node, the item input

    def __iter__(self):
        '''loops through list with while loop'''
        current = self.head #sets current to be the head
        while current is not None: #while it exists
            yield current
            current = current.next

    def append(self, item):
        '''adds node item to end of the list'''
        new_node = Node(item) #creates new node from item
        if DoublyLinkedList.is_empty(self) == True: #if the list is empty make it the new head then tail
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail #sets tail to be one before tail
            self.tail.next = new_node #sets the item after the old tail
            self.tail = new_node #new node is the new tail

        '''previous attempt, unused code'''
        # if self.prev_node is None:
        #     self.head = Node(item)
        #     self.prev_node = self.head
        # else:
        #     self.prev_node.next = Node(item)
        #     self.prev_node = self.prev_node.next

    def pop(self, pos=None):
        '''removes last item (tail) from the list and returns it if no position is specified.
        if position is specified then item in that position will be removed and returned '''
        #to_return = self.tail #wrong placement, unused code
        if pos == None: #if there is not a position set
            temp = self.tail #save tail in temp
            pos = DoublyLinkedList.size(self)-1 #find the position using size since it is the tail
            DoublyLinkedList.del_node(self, pos) #use delete function to remove based on position
            self.tail = self.tail.previous #sets the new tail to be the previous node of the old tail
            return temp.data #returns the original tail saved in temp

        else:
            '''previous try, unused code'''
            # pos = pos
            # DoublyLinkedList.del_node(self, pos)
            # self.tail = self.tail.previous
            # return

            temp = self.head  # Initialise temp
            count = 0  # Index of node
            while temp: #while loop to step throug nodes
                if count == pos: #when the position is reached
                    DoublyLinkedList.del_node(self, pos) #delete the node using del_node function at position
                    return temp.data #returns the node of position passed in
                count += 1 #add one for each node stepped throufh
                temp = temp.next #temp is the next temp to continue loop

    def del_node(self, pos):
        '''seperate function to delete nodes based on their position'''
        if pos == 0: #if position is the first
            self.head = self.head.next #head is removed
        else: #if poisiton is not 0
            node = self.head #save head in node
            for nodes in range(pos - 1): #iterate throug nodes
                node = node.next #replace node
            node.next = node.next.next #move surrounding node

    def search(self, item):
        '''searches for a node in the list and returns true if it exists, false otherwise'''
        current = self.head #save head in current
        while current != None: #loop as long as current exists
            if current.data == item: #if the seached item and current match
                return True #the item does exist in the list
            current = current.next #continue looping through nodes
        return False #if the loop finishes without returning true then it must be false

    def remove(self, item):
        '''removes a item based on name (rather than position)'''
        current = self.head #saves head in current
        count = 0 #sets counter to 0
        while current != None: #loop as long as current exists
            count +=1 #add one count for each step
            if current.data == item: #if a match is found in the list
                DoublyLinkedList.del_node(self, count-1) #use del_node to remove node based on position found
            current = current.next #continue looping through nodes

