class Solution {
public:
    std::vector<int> twoSum(std::vector<int> nums, int target) {
        std::vector<int> sorted_num = nums;
        std::sort(sorted_num.begin(), sorted_num.end());
        int l = 0, r = nums.size() - 1;
        while (sorted_num[l] + sorted_num[r] != target) {
            if (sorted_num[l] + sorted_num[r] < target)
                l++;
            else if (sorted_num[l] + sorted_num[r] > target)
                r--;
        }
        int r_val = sorted_num[r], l_val = sorted_num[l];
        bool flag = true;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == l_val and flag) {
                l = i;
                flag = false;
            } else if (nums[i] == r_val) {
                r = i;
            }
        }
        if (r > l)
            return {l, r};
        else
            return {r, l};
    }
};
