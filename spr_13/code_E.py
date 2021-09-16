# Comment it before submitting
class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return f'{self.prev}<-[{self.value}]->{self.next}'

def solution(node):
    while node:
        new_node = node
        new_node.prev = node.next
        new_node.next = node.prev
        # print(f'{node.prev}<-{new_node.value}->{node.next}')
        print(new_node)
        node = node.next

    # return new_node

def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)

    # print(new_head.value)

    # result is new_head == node3
    # node3.next == node2
    # node2.next == node1 node2.prev == node3
    # node1.next == node0 node1.prev == node2
    # node0.prev == node1
test()