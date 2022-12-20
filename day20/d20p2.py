# open and read the input file
input_file = open("day20/input.txt", "r")
decryption_key = 811589153
input = [int(l)*decryption_key for l in input_file.read().split("\n")]
l = len(input)

class node:
    def __init__(self, v: int) -> None:
        self.val, self.prev, self.next = v, None, None

    def print_list(self) -> None:
        n = self
        while n.next is not self:
            print(n.val, " ", end="")
            n = n.next
        print(n.val)

    def append(self, v):
        self.next = node(v)
        self.next.prev = self
        return self.next

    def remove(self) -> None:
        sn, sp = self.next, self.prev
        sn.prev = self.prev
        sp.next = self.next
        self.next, self.prev = None, None

    def insert(self, a) -> None:
        left, right = a, a.next
        left.next = self
        right.prev = self
        self.next = right
        self.prev = left

    def find(self, v):
        n = self
        if n.val == v:
            return n
        while n.next is not self:
            n = n.next
            if n.val == v:
                return n

    def search_forward(self, count):
        n = self
        for i in range(count % (l-1)):  # l-1 because we remove the node before searching
            n = n.next
        return n

    def search_forward1000(self):
        n = self
        for i in range(1000 % l):
            n = n.next
        return n

    def search_backward(self, count):
        n = self
        for i in range(count % (l-1)):  # l-1 because we remove the node before searching
            n = n.prev
        return n

# Create a doubly linked list using the input data
this_node = None
node_order = []
for n in input:
    if this_node == None:
        this_node = node(n)
        node_order.append(this_node)
    else:
        this_node = this_node.append(n)
        node_order.append(this_node)
this_node.next = node_order[0]
node_order[0].prev = this_node

#############
# MAIN LOOP #
#############

for i in range(10):
    for n in node_order:
        if n.val == 0:
            pass
        elif n.val > 0:
            old_loc = n.prev
            n.remove()
            n.insert(old_loc.search_forward(n.val))
        else:
            old_loc = n.prev
            n.remove()
            n.insert(old_loc.search_backward(abs(n.val)))

    # node_order[0].print_list()


zero_node = node_order[0].find(0)
val1_node = zero_node.search_forward1000()
val2_node = val1_node.search_forward1000()
val3_node = val2_node.search_forward1000()

print(f"{val1_node.val} + {val2_node.val} + {val3_node.val} = ", end="")
print(val1_node.val + val2_node.val + val3_node.val)