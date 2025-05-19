var containsDuplicate = function (nums) {
  let obj = {};
  for (let i = 0; i < nums.length; i++) {
    // if (obj[nums[i]]) return true; // check does not work as intended for the value 0 because 0 is falsy in JavaScript
    if (nums[i] in obj) return true;
    else obj[nums[i]] = nums[i];
    console.log(obj);
  }
  return false;
};

// using set
// const set =  new Set();
// for (let num in nums){
//     if(set.has(num))return true
//     set.add(num);
// }
// return false

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const seen = new Set();

  for (const num of nums) {
    if (seen.has(num)) {
      return true;
    }

    seen.add(num);
  }
  return false;
};
let nums = [0, 4, 5, 0, 3, 6];
console.log(containsDuplicate(nums));
