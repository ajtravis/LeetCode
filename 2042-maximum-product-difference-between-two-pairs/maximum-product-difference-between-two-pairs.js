/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProductDifference = function(nums) {
    let output;
    let sortArr;
    sortArr=nums.sort(function (a, b) { return b - a });
    output=Math.abs(sortArr[sortArr.length-2]*(sortArr[sortArr.length-1])-sortArr[0]*sortArr[1]);
    return output;
}