/**
 * @param {number[][]} items
 * @param {number[]} queries
 * @return {number[]}
 */
var maximumBeauty = function (items, queries) {
    items.sort((a, b) => a[0] - b[0]);
    let maxBeauty = 0;
    let prefixMaxBeauty = [];
    for (let [price, beauty] of items) {
        prefixMaxBeauty.push((maxBeauty = Math.max(maxBeauty, beauty)));
    }
    let res = [];
    for (let queryPrice of queries) {
        let low = 0;
        let high = items.length - 1;
        while (low <= high) {
            let mid = ~~(low / 2 + high / 2);
            if (items[mid][0] <= queryPrice) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        res.push(high >= 0 ? prefixMaxBeauty[high] : 0);
    }
    return res;
};