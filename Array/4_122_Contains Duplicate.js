/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  // first apporach
  // let seen ={}
  // for(i=0;i<nums.length;i++){
  //     if(seen.hasOwnProperty(nums[i])){
  //         return true;
  //     }else{
  //         seen[nums[i]]=1;
  //     }
  // }
  // return false;

  // short code
  // let seen ={}
  // for(const num of nums){
  //     // if(seen.hasOwnProperty(num))return true;
  //     if(num in seen) return true;
  //     else seen[num]=1;
  // }
  // return false;

  // space complexity O(1)
  // nums.sort();
  // for(i=0;i<nums.length-1;i++){
  //     if(nums[i]==nums[i+1]) return true;
  // }
  // return false;

  // set
  let set = new Set(nums);
  if (nums.length != set.size) return true;
  return false;
};
let nums = [0, 4, 5, 0, 3, 6];
console.log(containsDuplicate(nums));
