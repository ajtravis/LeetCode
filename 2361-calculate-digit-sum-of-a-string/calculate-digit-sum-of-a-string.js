/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var digitSum = function(s, k) {
    str = ""
    while (s.length > k) {
        i = 0
        j = k
        sum = 0
        while(i < j && i < s.length){ 
            sum += parseInt(s[i])
            if(i == j-1){
                str += String(sum)
                sum = 0
                j += k
                console.log(str)
            }
            if(i == s.length-1 && s.length % k != 0){
                str += String(sum)
                console.log(str,j, s)
            }
            i++
        }
        s = str
        str = ""
    }      
    return s
};