/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function (nums1, nums2) {
  //     nums1.sort(function(a, b){return a - b});
  //     nums2.sort(function(a, b){return a - b});
  //     let i=0;
  //     let j=0;
  //     let res = [];

  //         console.log(nums1,nums2);
  //     while(nums1.length>i && nums2.length>j){
  //         if(nums1[i]==nums2[j]){
  //             res.push(nums1[i]);
  //             i++;
  //             j++;
  //         }else if(nums1[i]>nums2[j]){
  //             j++;
  //         }else i++;
  //     }
  //     return res;

  //     const count1 = {}
  //     const count2 ={}
  //         let res = [];

  //     for(num of nums1){
  //         if(count1.hasOwnProperty(num)){
  //             count1[num]++;
  //         }else count1[num] = 1;
  //     }
  //     for(num of nums2){
  //         if(count2.hasOwnProperty(num)){
  //             count2[num]++;
  //         }else count2[num] = 1;
  //     }
  //     console.log(count1,count2)
  //     for(key of Object.keys(count1)){
  //         if(key in count2){
  //         res.push(...Array(Math.min(count1[key], count2[key])).fill(Number(key)));
  //         }
  //     }
  //     return res;

  let seen = {};
  let res = [];
  for (num of nums1) {
    seen[num] = (seen[num] ?? 0) + 1;
  }
  for (num of nums2) {
    if (num in seen && seen[num] > 0) {
      res.push(num);
      seen[num] = seen[num] - 1;
    }
  }
  return res;
};
