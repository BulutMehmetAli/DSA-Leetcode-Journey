class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):              # sona ekleme: O(1)
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    @staticmethod
    def _to_str(node):                    # adımları göstermek için: [5, 1, 3]
        values = []
        while node:
            values.append(str(node.data))
            node = node.next
        return "[" + ", ".join(values) + "]"

    # ---------------- MERGE SORT ----------------

    def sort(self, show_steps=False):
        self.head = self._merge_sort(self.head, 0, show_steps)

        # tail'i güncelle (sıralama sonrası son düğüm değişti)
        current = self.head
        while current and current.next:
            current = current.next
        self.tail = current

    def _merge_sort(self, head, depth, show):
        indent = "    " * depth

        # base case: boş ya da tek elemanlı liste zaten sıralıdır
        if head is None or head.next is None:
            if show:
                print(f"{indent}{self._to_str(head)}  <- base case")
            return head

        if show:
            print(f"{indent}Böl: {self._to_str(head)}")

        # 1) Ortayı bul ve ikiye böl
        mid = self._get_middle(head)
        right_head = mid.next
        mid.next = None                   # sol yarıyı sağdan kopar

        # 2) İki yarıyı ayrı ayrı sırala
        left = self._merge_sort(head, depth + 1, show)
        right = self._merge_sort(right_head, depth + 1, show)

        # 3) Birleştir
        if show:
            left_str, right_str = self._to_str(left), self._to_str(right)
        merged = self._merge(left, right)
        if show:
            print(f"{indent}Birleştir: {left_str} + {right_str} -> {self._to_str(merged)}")

        return merged

    def _get_middle(self, head):
        slow = head
        fast = head.next                  # head.next ile başla, bölme dengeli olsun
        while fast and fast.next:
            slow = slow.next              # 1 adım
            fast = fast.next.next         # 2 adım
        return slow                       # sol yarının son düğümü

    def _merge(self, a, b):
        dummy = Node(0)                   # sahte başlangıç düğümü
        tail = dummy

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b         # kalan kısmı olduğu gibi ekle
        return dummy.next


if __name__ == "__main__":
    ourList = LinkedList()
    for x in [5, 1, 3, 2, 9, 6, 7, 12, 4]:
        ourList.addNode(x)

    print("Önce:  ", end="")
    ourList.print_list()
    print()

    ourList.sort(show_steps=True)         # adımları görmek istemezsen False yap

    print()
    print("Sonra: ", end="")
    ourList.print_list()