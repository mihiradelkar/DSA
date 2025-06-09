/**
 * @param {string} s
 * @return {string}
 */
var smallestString = function (s) {
  // let i = 0;
  // while (s[i]==='a') i++;
  // if (i===s.length) return s.substring(0,s.length-1)+'z'
  // sl = [...s];
  // while (i < s.length && s[i]!=='a'){
  //     sl[i] = String.fromCharCode(sl[i].charCodeAt(0)-1);
  //     i++;
  // }
  // return sl.join('');

  let i = 0;
  while (s[i] === "a") i++;
  if (i >= s.length) return s.substring(0, s.length - 1) + "z";
  let res = "";
  if (i > 0) res = s.substring(0, i);
  while (i < s.length && s[i] !== "a") {
    const c = s[i];
    res += String.fromCharCode(c.charCodeAt(0) - 1);
    i++;
  }
  if (i < s.length) res += s.substring(i);
  return res;
};
