/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  // let result = (x+"").split('').reverse().join('');
  // const reversed = parseInt(Math.abs(x).toString().split('').reverse().join(''));
  // const result = x < 0 ? -reversed : reversed;
  // if (result < -2147483648 || result > 2147483647) return 0;
  // return result;

  let result = 0;
  let num = x;
  const isNegative = x < 0;

  if (isNegative) num = -num;
  while (num > 0) {
    result = result * 10 + (num % 10);
    num = Math.floor(num / 10);
  }
  // if(result < -2147483648 || result > 2147483647) return 0;
  if (result > 2 ** 31 - 1) return 0;
  return isNegative ? -result : result;
};
