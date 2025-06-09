/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let profit = 0;
  let buy = false;
  let buyprice = 0;
  //     for(j=0;j<prices.length-1;j++){
  //         if(prices[j]<prices[j+1] && buy==0){
  //             console.log("buy",prices[j],prices[j+1])
  //             buy=prices[j];
  //         }
  //         // if(prices[j]>prices[j+1] && buy!=0){
  //         if(prices[j]>prices[j+1] && buy!=0){
  //             console.log("sell",prices[j],prices[j+1], "profit", prices[j]-buy)
  //             profit = profit + (prices[j]-buy)
  //             buy=0;
  //         }
  //         if(j==prices.length-2 && buy!=0){
  //             profit = profit + (prices[j+1]-buy)
  //         }
  //     }

  for (i = 1; i < prices.length; i++) {
    if (prices[i] > prices[i - 1] && !buy) {
      // console.log("buy",prices[i-1],prices[i])
      buyprice = prices[i - 1];
      buy = true;
    }
    if (prices[i] > prices[i + 1] && buy) {
      // console.log("sell",prices[i],prices[i+1], "profit", prices[i]-buy)
      profit = profit + (prices[i] - buyprice);
      buy = false;
    }
    // console.log(i,prices.length-1, prices[i],buyprice)
    if (i == prices.length - 1 && buy) {
      profit = profit + (prices[i] - buyprice);
    }
  }

  return profit;
};
// simple solution
var maxProfit = function (prices) {
  let profit = 0;
  for (i = 1; i < prices.length; i++) {
    if (prices[i - 1] < prices[i]) {
      profit += prices[i] - prices[i - 1];
    }
  }
  return profit;
};
