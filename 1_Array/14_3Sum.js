/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  res = [];
  // for(let i = 0; i<nums.length-2; i++){
  //     for(let j = i+1; j<nums.length-1; j++){
  //         for(let k = j+1; k<nums.length; k++){
  //             if(nums[i]+nums[j]+nums[k]===0){
  //                 res.push([nums[i],nums[j],nums[k]]);
  //             }
  //         }
  //     }
  // }

  // for(let i = 0; i<nums.length-1; i++){
  //     target = -1 * nums[i];
  //     seen = {}
  //     for(let j = i; j<nums.length; j++){
  //         if(i==j)continue;
  //         if(seen[nums[j]]!=undefined){
  //             res.push([nums[i],nums[j],seen[nums[j]]]);
  //         }else seen[target-nums[j]]=nums[j];
  //     }
  // }
  // console.log(res)

  nums.sort((a, b) => a - b);
  for (let i = 0; i < nums.length - 2; i++) {
    if (nums[i] > 0) break;
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let left = i + 1;
    let right = nums.length - 1;
    while (left < right) {
      let sum = nums[i] + nums[left] + nums[right];
      if (sum == 0) {
        res.push([nums[i], nums[left], nums[right]]);
        left++;
        while (nums[left] === nums[left - 1] && left < right) left++;
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  }
  return res;
};
