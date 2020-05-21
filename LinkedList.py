##Linked List Demonstration

##Austin Shane
##19 March 2020

##Algorithm:
# LinkedList.py contains two classes, the node class, and the LinkedList class. Importing LinkedList.py allows the user to create a linked list
# and perform various operations on it. These include: determining whether the linked list(LL) is empty (is_empty), the size of the LL (size),
# adding new items to the head (add), appending new items to the end (append), removing and returning the last item of the LL (pop), search for
# an item in the LL (search), and remove an item (remove). This allows the user to effectively manage a linked list.


class Node(object):
    def __init__(self, data, next = None):
        '''initilization for data, next'''
        self.data = data #sets self.data
        self.next = next #sets self.next

    def __str__(self):
        '''returns node data'''
        return self.data #returns node data


class LinkedList(object):
    def __init__(self, head = None):
        '''initializes head and tail of linked list'''
        self.head = head
        #self.prev_node = None ##commented out, was not needed

    def is_empty(self):
        '''determines whether list is empty, returns true if it is, false if not'''
        if self.head == None: #if there is no head
            to_return = True #it is true the list is empty
        else:
            to_return = False #anything else is false
        return to_return #returns true/false

    def size(self):
        '''determines the number of nodes/items in the list'''
        if LinkedList.is_empty(self) == True: #if the function is_emptyy returns true
            to_return = 0 #then the length is 0
        else: #anything else the length cannot be 0
            current = self.head #save head in current
            size = 0
            while current: #loop through the nodes
                size = size + 1 #add one to the size counter for each iteration
                current = current.next #continue iteration until it cannot continue
            to_return = size #saves final size
        return to_return #returns size

    def add(self, item):
        '''adds a node to the head of the list'''
        new_node = Node(item) #create new node
        new_node.next = self.head #make the old head the second node
        self.head = new_node #make the new node the new head

    def __iter__(self):
        '''loops through list with while loop'''
        current = self.head #save head in current
        while current != None: #when a head exists
            yield current
            current = current.next #continue looping

    def append(self, item):
        '''adds node item to end of the list'''
        if LinkedList.is_empty(self) == True: #if is_empty returns true
            self.add(item) #list is empty and item can be directly added
        else: #if list is not empty
            node = self.head #save head in node
            while node.next != None: #while node.next exists
                node = node.next #continue loop
            node.next = Node(item) #insert item

        '''previous attempt, unused code'''
        # if self.prev_node is None:
        #     self.head = Node(item)
        #     self.prev_node = self.head
        # else:
        #     self.prev_node.next = Node(item)
        #     self.prev_node = self.prev_node.next

    def pop(self, pos=None):
        '''removes last item (tail) from the list and returns it if no position is specified.
        if position is specified then node in that position will be removed and returned '''
        if pos == None: #if position is not speficied
            pos = LinkedList.size(self)-1 #use size function -1 to find length and set position to end
        else: #if a position is specified
            pos = pos #position is the position entered
        temp = self.head  # Initialise temp
        count = 0  # Index of current node
        while temp: #loop through nodes
            if count == pos: #when the counter reaches the position
                LinkedList.del_node(self, pos) #use del_node function to remove it based on position
                return temp.data #returns the data of node position
            count += 1 #add one for each iteration
            temp = temp.next #continue loop

    def del_node(self, pos):
        '''seperate function to delete nodes based on their position'''
        temp = self.head #set temp to the head
        if pos == 0: #if the position set is the first
            self.head = temp.next #set the head to be temp.next
            temp = None #temp is none
            return
        for i in range(pos-1): #iterate through the nodes
            temp = temp.next #set temp to be next
            if temp is None:
                break #breaks if temp is none
        next = temp.next.next
        temp.next = None #removes node
        temp.next = next

    def search(self, item):
        '''searches for a node in the list and returns true if it exists, false otherwise'''
        current = self.head #set current to self.head
        while current != None: #while current exists
            if current.data == item: #if it matches item searched
                return True #the item does exist
            current = current.next #continue looping
        return False #if code reaches bottom then item does not exist in list

    def remove(self, item):
        '''removes a item based on name (rather than position)'''
        current = self.head #set current to head
        count = 0
        while current != None: #while current exists
            count +=1 #keep count of iterations
            if current.data == item: #when the item searched to remove matches
                LinkedList.del_node(self, count-1) #use del_node function to remove it
            current = current.next #continue looping



