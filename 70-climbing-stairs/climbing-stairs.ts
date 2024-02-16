function climbStairs(n: number): number {
    if(n ===1 || n === 2 || n === 3){
        return n;
    }
    
    let cache = [0,1,2,3];
    
    for(let i = 4;  i <= n ; i++){
        cache[i] = cache[i - 1] + cache[i - 2];
    }

    return cache[n];
};