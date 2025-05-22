/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {
  n = nums.length; //7
  k = k % n; // if k>n less swaps
  // for(i=0;i<k;i++){
  // temp = nums[n-1];
  // for(j=n-2;j>=0;j--){
  //     nums[j+1]=nums[j];
  // }
  //     nums[0]=temp;
  // }

  // for(i=0;i<k;i++){
  //     nums.unshift(nums[n-1]);
  //     nums.pop();
  // }

  function reverse(start, end) {
    while (start < end) {
      temp = nums[start];
      nums[start] = nums[end];
      nums[end] = temp;
      start += 1;
      end -= 1;
    }
  }

  reverse(0, n - 1);
  reverse(k, n - 1);
  reverse(0, k - 1);
};
