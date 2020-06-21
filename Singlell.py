class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def AtBegining(self,newdata):
        NewNode = Node(newdata)

        #Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode
        
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
 '''   def RemoveNode(self, Removekey):

        HeadVal = self.headval

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None


        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode'''


Listl = SLinkedList()
Listl.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

#Link first Node to second node
Listl.headval.nextval = e2

#Link second Node to third node
e2.nextval = e3

Listl.AtBegining("Sun")
Listl.AtEnd("Fri")
Listl.Inbetween(Listl.headval.nextval,"Thu")
print("Before removing elements")
Listl.listprint()
#Listl.RemoveNode("Tue")
#Listl.RemoveNode("Fri")
print("After removing")
Listl.listprint()


