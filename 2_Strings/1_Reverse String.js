/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function (s) {
  // for (let i=0; i<(s.length-1)/2;i++) [s[i] , s[(s.length-1)-i]] = [s[(s.length-1)-i], s[i]] ;
  let i = 0;
  while (i < (s.length - 1) / 2) {
    const temp = s[s.length - 1 - i];
    s[s.length - 1 - i] = s[i];
    s[i] = temp;
    i++;
  }
};
