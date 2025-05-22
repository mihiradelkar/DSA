/**
 * @param {number[]} digits
 * @return {number[]}
 */

var plusOne = function (digits) {
  //     var shiftOne = function(index){
  //         if(digits[index] == 9) {
  //             if (index == 0) {
  //                 addDigit();
  //             }
  //             else {
  //                 digits[index] = (digits[index] + 1) % 10;
  //                 shiftOne(index - 1);
  //             }
  //         }
  //         else {
  //             digits[index] = digits[index] + 1;
  //         }
  //     }

  //     var addDigit = function() {
  //         for (let i = digits.length; i > 0; i--) {
  //             digits[i] = digits[i - 1];
  //         }
  //         digits[0]= 1;
  //         digits[1] = (digits[1] + 1) % 10;
  //     }

  //     n=digits.length-1; //4
  //     shiftOne(n);
  //     return digits;

  // [0,0,0]
  //  0 1 2 3
  // [1,0,0,0]

  // var shiftOne = function(){
  //     for(i=digits.length;i>0;i--){
  //         digits[i]=digits[i-1];
  //         if(i=1) digits[i-1]=1;
  //     }
  // }

  // var addOne = function(i){
  //     if(digits[i]==9){
  //         digits[i]=0;
  //         if(i>0)addOne(i-1);
  //         else shiftOne();
  //     }else{
  //         digits[i]=digits[i]+1;
  //     }
  // }
  // addOne(digits.length-1);
  // return digits;

  //   var addOne = function (i) {
  //     if (digits[i] == 9) {
  //         digits[i] = 0;
  //         if (i > 0) addOne(i - 1);
  //         else return digits = [1, ...digits];
  //     } else digits[i] = digits[i] + 1;
  //   };
  //   addOne(digits.length - 1);
  //   return digits;

  // var addOne = function (i) {
  //     if (digits[i] < 9) {
  //         digits[i]++;
  //         return digits;
  //     }else{
  //         digits[i] = 0;
  //         if (i > 0) addOne(i - 1);
  //         else return digits = [1, ...digits];
  //     }
  //   };
  //   addOne(digits.length - 1);
  //   return digits;

  for (let i = digits.length - 1; i >= 0; i--) {
    if (digits[i] < 9) {
      digits[i]++;
      return digits;
    }
    digits[i] = 0;
  }
  return [1, ...digits];
};
