from typing import Optional
class SinglyLinkedList:
    
    #Private Class Node
    class _Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    #Constructor
    def __init__(self):
        self.head = None


    #Add Method
    def append(self, data):
        newNode = self._Node(data)
        
        #If head is Null it means LinkedList is empty, so we add the new node to the Head
        if not self.head:
            self.head = newNode
            return
        
        #Head is not Null and LinkedList is not empty so we add the new node to the end of the list
        current = self.head
        while current.next is not None:
            current = current.next
        
        #We reached the end Node, now adding the new node to the next of the end node
        current.next = newNode

    def remove(self, data):
        current = self.head
        prev = None
        while current:

            if current.data == data:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return
            else:
                prev = current

            current = current.next


    def prepend(self, data):
        newNode = self._Node(data)
        if self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode

    def insertAfter(self, prevNodeData, data):
        newNode = self._Node(data)
        prevNode = self.find(prevNodeData)

        if prevNode:
            temp = prevNode.next
            prevNode.next = newNode
            newNode.next = temp
            print("Inserted")
            return True
        print("Previous Node Not Found")
        return False





    def find(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                print(f"Found {data}")
                return curr
            curr = curr.next
        print("Not a Node")
        return None
    

    def getHead(self) -> _Node:
        return self.head
    def reverseList(self, Head: Optional[_Node]) -> Optional[_Node]:
        curr = Head
        prev = None
        while curr:
            temp3 = curr
            curr = curr.next
            temp = curr.next
            temp2 = temp3
            temp.next = temp2
            
        return curr
             
                 

        

            

    
    def display(self):
        current = self.head
        while current: #we are checking if current is pointing to an object or not (Node | None)
            print(current.data,end="->")
            current = current.next
        print("None")


        

        

        
    
if __name__ == '__main__':
    List = SinglyLinkedList()
    List.prepend(29)
    List.append(3)
    List.append(11)
    List.append(21)
    List.append(55)
    List.display()
    List.find(3)
    List.remove(3)
    List.display()
    List.find(3)
    List.prepend(99)
    List.display()
    List.insertAfter(99,69)
    List.display()

    List.reverseList(List.getHead())
    List.display()