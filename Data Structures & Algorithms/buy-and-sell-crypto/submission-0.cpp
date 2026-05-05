class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0, r = 1, max_pr = 0;
        while (r < prices.size()) {
            if (prices[l] < prices[r]) {
                max_pr = max(max_pr, prices[r] - prices[l]);
            } else {
                l = r;
            }
            r++;
        }
        return max_pr;
    }
};
