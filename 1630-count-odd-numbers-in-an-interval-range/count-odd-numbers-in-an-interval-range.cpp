class Solution {
public:
    int countOdds(int low, int high) {
        int count = floor((high-low)/2);
        // If low is even, make it odd.
        if ((low & 1) || (high & 1)) {
            count++;
        }
  
        // low could become greater than high due to incrementation
        // if it is, the answer is 0; otherwise, use the formula.
        return count;
    };
};