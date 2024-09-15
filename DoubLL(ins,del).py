class node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.nxt = None
class dll:
    def __init__(self):
        self.head = None
    def create(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.nxt:
                temp = temp.nxt
            temp.nxt = new_node
            new_node.prev = temp
    def insert(self,pos,data):
        new = node(data)
        if pos == 1:
            current = self.head
            new.nxt = current
            current.prev = new
            self.head = new
        else:
            current = self.head
            if current.nxt is None:
                current.prev = None
            for i in range(1,pos-1):
                current = current.nxt
            new.nxt = current.nxt
            current.nxt = new
            new.prev = current
            current.nxt.prev = new
    def delete(self,pos):
        if self.head is None:
            print("List is Empty")
            return
        temp = self.head
        if pos == 1:
            self.head = self.head.nxt
            temp.nxt = None
            temp.prev = None
        else:
            for i in range(1,pos):
                temp = temp.nxt
            temp.prev.nxt = temp.nxt
            temp.nxt.prev = temp.prev
            temp.prev = None
            temp.nxt = None

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current:
                print(current.data,end="-->")
                last = current
                current = current.nxt
            print("None")
            while last:
                print(last.data,end="<--")
                last = last.prev
            print("None")


def main():
    l = dll()
    while True:
        print("1.Create Doubly linked list")
        print("2.Insert")
        print("3.Delete")
        print("4.Display")
        print("5.Exit")
        opt = input("Select an option:")
        if opt == "1":
            n = int(input("enter no. of node:"))
            for i in range(n):
                data = input(f"Enter data for node {i+1}:")
                l.create(data)
        elif opt == "2":
            pos = int(input("enter the position to insert at:"))
            data = input("enter data to inser:")
            l.insert(pos,data)
        elif opt == "3":
            pos = int(input("enter position to delete:"))
            l.delete(pos)
        elif opt == "4":
            l.display()
        elif opt == "5":
            print("Exiting, Visit again!")
            break
        else:
            print("Invalid!, Try again")
    
    
if __name__ == '__main__':
    main()