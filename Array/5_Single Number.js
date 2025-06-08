/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
  // if(nums.length==1) return nums[0];
  // nums.sort();
  // for(i=0;i<nums.length-1;i+=2){
  //     if(nums[i]!=nums[i+1]){
  //         return nums[i];
  //     }
  // }
  // return nums[nums.length-1];
  result = 0;
  for (const num of nums) result = num ^ result;
  return result;
};
