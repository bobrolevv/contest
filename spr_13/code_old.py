# Comment it before submitting
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return f'[{self.value}]->{self.next_item}'

def solution(node):
    head = None
    index = None

    def get_node_by_index(node, index):
        while index:
            node = node.next
            index -= 1
        return node


    def insert_node(head, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = head
            return new_node
        previous_node = get_node_by_index(head, index - 1)
        new_node.next = previous_node.next
        previous_node.next = new_node
        return head

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    print(node0)
    solution(node0)
    # Output is:
    # node0
    # node1
    # node2
    # node3
test()