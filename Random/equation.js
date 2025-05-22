var equation = function (n) {
  for (var a = 0; a < n; a++) {
    for (var b = 0; b < n; b++) {
      for (var c = 0; c < n; c++) {
        for (var d = 0; d < n; d++) {
          checkEquation(a, b, c, d);
        }
      }
    }
  }
};
var checkEquation = function (a, b, c, d) {
  if ((a ^ 2) + (b ^ 2) == (c ^ 2) + (d ^ 2)) {
    console.log("Equation:", a, b, c, d);
  }
};

var n = 3;
equation(n);
