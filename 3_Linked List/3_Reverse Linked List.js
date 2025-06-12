/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
  //     temp = head
  //     tempN = head.next
  //     head.next = null
  //     head = tempN

  //     temp1 = head
  //     tempN = head.next
  //     head.next = temp
  //     head = tempN

  //     temp = head
  //     tempN = head.next
  //     head.next = temp1
  //     head = tempN

  //     temp1 = head
  //     tempN = head.next
  //     head.next = temp
  //     head = tempN

  //     head.next = temp1

  // n[1,2,3,4,5]
  // p h n

  let previous = null;
  while (head != null) {
    let next = head.next;
    head.next = previous;
    previous = head;
    head = next;
  }
  return previous;
};
