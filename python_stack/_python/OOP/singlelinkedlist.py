class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self

    def add_to_back(self, val):
        new_node = SLNode(val)

        if self.head is None:
            self.head = new_node
            return self

        runner = self.head

        while runner.next is not None:
            runner = runner.next

        runner.next = new_node
        return self

    def print_values(self):
        runner = self.head

        while runner is not None:
            print(runner.value)
            runner = runner.next

        return self

    # BONUS: remove first node
    def remove_from_front(self):
        if self.head is None:
            return None

        removed_value = self.head.value
        self.head = self.head.next
        return removed_value

    # BONUS: remove last node
    def remove_from_back(self):
        if self.head is None:
            return None

        if self.head.next is None:
            removed_value = self.head.value
            self.head = None
            return removed_value

        runner = self.head

        while runner.next.next is not None:
            runner = runner.next

        removed_value = runner.next.value
        runner.next = None
        return removed_value

    # BONUS: remove first occurrence of a value
    def remove_val(self, val):
        if self.head is None:
            return False

        if self.head.value == val:
            self.head = self.head.next
            return True

        runner = self.head

        while runner.next is not None:
            if runner.next.value == val:
                runner.next = runner.next.next
                return True
            runner = runner.next

        return False

    # SENSEI BONUS: insert at position n
    def insert_at(self, val, n):
        new_node = SLNode(val)

        if n == 0:
            new_node.next = self.head
            self.head = new_node
            return self

        runner = self.head
        index = 0

        while runner is not None and index < n - 1:
            runner = runner.next
            index += 1

        if runner is None:
            return self  

        new_node.next = runner.next
        runner.next = new_node

        return self