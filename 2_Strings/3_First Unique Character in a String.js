/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
  let seen = {};
  for (let i of s) seen[i] = (seen[i] ?? 0) + 1;
  for (let i = 0; i < s.length; i++) if (seen[s[i]] === 1) return i;
  return -1;
};
