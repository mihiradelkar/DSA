/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  // [0,1,0,3,12]
  // [0,1,2,3,4 ]
  //  i j  -> swap
  // [1,0,0,3,12]
  //    i j -> j++
  // [1,0,0,3,12]
  //    i   j -> swap
  // [1,3,0,0,12]
  //      i    j -> swap
  // [1,3,12,0,0]

  // while(j<n){
  //     if(nums[i]==0){
  //         let temp  = nums[i];
  //         nums[i] = nums[j];
  //         nums[j] = temp;
  //         i++;
  //         j++;
  //     }else j++;
  // }

  // let i=0;
  // let j=1;
  // while(j<nums.length){
  //     if(nums[i]==0){
  //         if(nums[j]!=0){
  //             [nums[i], nums[j]] = [nums[j], nums[i]];
  //             i++;
  //             j++;
  //         }else j++;
  //     }else {
  //         i++;
  //         j++;
  //     }
  // }

  let i = 0;
  for (let j = 0; j < nums.length; j++) {
    if (nums[j] !== 0) {
      [nums[i], nums[j]] = [nums[j], nums[i]];
      i++;
    }
  }
};
