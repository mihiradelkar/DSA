/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  s = s.toLowerCase().replace(/[^a-z0-9]/g, "");
  if (s == "") return true;
  const len = s.length - 1;
  for (let i = 0; i < len / 2; i++) if (s[i] != s[len - i]) return false;
  return true;
};
