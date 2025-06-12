/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (s.length != t.length) return false;

  // s=s.split("").sort().join("");
  // t=t.split("").sort().join("");
  // console.log(s,t)
  // if(s===t) return true;
  // return false;

  // cs = {};
  // ct = {};
  // for(let i=0;i<s.length;i++){
  //     cs[s[i]]= (cs[s[i]]??0)+1;
  //     ct[t[i]]= (ct[t[i]]??0)+1;
  // }
  //     console.log(cs,ct);
  // for (c in cs){
  //     if(cs[c] !== ct[c]){
  //         return false
  //     }
  // }
  // return true;

  cs = {};
  for (let i = 0; i < s.length; i++) {
    cs[s[i]] = (cs[s[i]] || 0) + 1;
    cs[t[i]] = (cs[t[i]] || 0) - 1;
  }
  for (const c in cs) {
    if (cs[c] != 0) {
      return false;
    }
  }
  return true;
};
