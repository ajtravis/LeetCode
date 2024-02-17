class Solution {
public:
    int findLucky(vector<int>& arr) {
        unordered_map<int,int> mp;
        int ans=0;
        for(auto ch:arr)
        {
            mp[ch]++;
        }
        for(int i=0;i<arr.size();i++)
        {
            if(mp[arr[i]]==arr[i]&&arr[i]>ans)
            {
                ans=arr[i];
            }
        }
        if(ans!=0)
        {
            return ans;
        }
        return -1;
    }
};