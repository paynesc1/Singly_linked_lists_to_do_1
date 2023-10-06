
class SList():
    def __init__(self):
        self.head = None

    def add_to_front(self, *vals):
        for val in vals:
            new_node = SLNode(val)
            current_node = self.head
            if not self.head:
                self.head = new_node
            new_node.next = current_node
            self.head = new_node
        return self

    def display_vals(self):
        runner = self.head
        while runner != None:
            print(runner.val)
            runner = runner.next
        return self


class SLNode():
    def __init__(self, val):
        self.val = val
        self.next = None

my_list = SList()
# my_list.add_to_front(10,9,8,7,6,5,4,3,2,1)
my_list.add_to_front(3).add_to_front(2).add_to_front(1)
my_list.display_vals()