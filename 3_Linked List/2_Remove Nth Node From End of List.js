/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
// head = [1,2]
//         l
//           r
// c = 1  n = 1
var removeNthFromEnd = function (head, n) {
  // let res = head;
  // let left = head;
  // let right = head;
  // let count = 0
  // while(right.next != null){
  //     if(count>=n){
  //         left=left.next;
  //     }
  //     right = right.next;
  //     count++;
  //     console.log(count,left.val,right.val);
  // }
  // console.log(count,left.val,right.val);
  // if(n>1) left.next = right;
  // else left.next =null;
  // return res;

  //   add a dummy node to move ref from prev to nex.next and handle edge cases like removing the head
  let res = new ListNode(0, head);
  let left = res;
  let right = head;

  while (n > 0 && right != null) {
    right = right.next;
    n--;
  }
  while (right != null) {
    right = right.next;
    left = left.next;
  }
  left.next = left.next.next;
  return res.next;
};
