class Solution {
public:
    bool hasDuplicate(std::vector<int>& nums) {
        std::unordered_map<int, bool> hash;
        for (int num : nums) {
            if (hash[num]) {
                return true;
            } else {
                hash[num] = true;
            }
        }
        return false;
    }
};
