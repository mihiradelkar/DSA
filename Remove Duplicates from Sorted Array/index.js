/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  // nums.map((num,index)=>{
  //     if(num==nums.at(index+1)){
  //         nums[index+1]=nums[index+2]
  //     }
  // })

  // for(i=0;i<nums.length-1;i++){
  //     for(j=i+1;j<nums.length;j++){
  //         if(nums[i]!=nums[j]){
  //             nums[i+1]=nums[j]
  //             break;
  //         }
  //     }
  //     console.log(i)
  // }

  // i=0
  // j=i+1
  // while(j<nums.length){
  //     if(nums[i]!=nums[j]){
  //         nums[i+1]=nums[j];
  //         i++;
  //     }
  //     j++
  // }
  // return i+1;
  i = 0;
  for (j = i + 1; j < nums.length; j++) {
    if (nums[i] != nums[j]) {
      nums[i + 1] = nums[j];
      i++;
    }
  }
  return i + 1;
};
