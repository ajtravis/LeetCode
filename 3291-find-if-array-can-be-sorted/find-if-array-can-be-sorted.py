class Solution:
    def canSortArray(self, a: List[int]) -> bool:
        return (m:=-inf) and all(m<=min(deepcopy(i)) and (m:=max(i)) for _,i in groupby(a,int.bit_count))