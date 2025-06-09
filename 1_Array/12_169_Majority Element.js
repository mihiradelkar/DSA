/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  // let freq =  {}
  // for (const num of nums){
  //    // freq[num]==undefined?freq[num]=1:freq[num]+=1;
  //     freq[num]= (freq[num]??0)+1;
  //     if(freq[num]>nums.length/2) return num;
  // }

  // let freq =  {};
  // let result = null;
  // let max = 0;
  // for (const num of nums) {
  //     freq[num]= (freq[num]??0)+1;
  //     if (freq[num]>max){
  //         max = freq[num];
  //         result = num
  //     }
  // }
  // return result;

  // let freq =  {}
  // for (const num of nums){
  //     freq[num]= (freq[num]??0)+1;
  //     if(freq[num]>nums.length/2) return num;
  // }

  // let count = 0;
  // let candidate = nums[0]
  // for (const num of nums){
  //     if(count === 0) candidate = num;
  //     if (candidate === num) count++;
  //     else count--;
  // }
  // return candidate;

  let count = 1;
  let candidate = nums[0];
  for (let i = 1; i < nums.length; i++) {
    if (count === 0) candidate = nums[i];
    if (candidate === nums[i]) count++;
    else count--;
  }
  return candidate;
};
