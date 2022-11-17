class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution_2:
    def addListNode(self, l: ListNode, data: int):
        l.next = data

    def printList(self, l: ListNode):
        while l:
            print(l.val)
            l = l.next if l else None

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        curr = dummy

        carry = 0
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            sum = num1 + num2 + carry
            curr.next = ListNode(sum % 10)
            curr = curr.next
            carry = sum // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            curr.next = ListNode(carry)

        return dummy.next


if __name__ == '__main__':
    listNode = ListNode()
    data_1 = ListNode(1)
    listNode.next = data_1

    solution_2 = Solution_2()
    solution_2.addTwoNumbers(listNode, listNode)
