/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let diff = {};
  // for (let [index, num] of nums.entries()){
  //     if(diff.hasOwnProperty(num)){
  //         return[diff[num],index];
  //     }else diff[target-num]=index;
  // }
  for (let i = 0; i < nums.length; i++) {
    // if(nums[i] in diff){
    if (diff[nums[i]] != undefined) {
      return [diff[nums[i]], i];
    } else diff[target - nums[i]] = i;
  }
};
