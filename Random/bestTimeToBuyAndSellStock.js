/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let low = prices[0];
  let profit = 0;
  // for(i=1;i<prices.length;i++){
  //     if(prices[i]-low>profit) profit= prices[i]-low;
  //     if(prices[i]<low) low=prices[i];
  // }

  for (const price of prices) {
    if (price - low > profit) profit = price - low;
    if (price < low) low = price;
  }
  return profit;
};
