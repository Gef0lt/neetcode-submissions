class Solution {
public:
    int numDecodings(string s) {
        return devider({}, s).size();
    }

    std::vector<std::vector<int>> devider(std::vector<int> vec, std::string s) {
        std::vector<std::vector<int>> ans, sub1, sub2;

        if (s.empty()) {
            ans.push_back(vec);
            return ans;
        }

        // Single-digit case
        if (s[0] != '0') { // Ensure no number starts with 0
            std::vector<int> vec_copy = vec;
            vec_copy.push_back(s[0] - '0'); // Convert char to int
            sub1 = devider(vec_copy, s.substr(1));
            ans.insert(ans.end(), sub1.begin(), sub1.end());
        }

        // Two-digit case
        if (s.size() >= 2) {
            int two_digit = std::stoi(s.substr(0, 2)); // Convert first two chars to int
            if (two_digit >= 10 && two_digit <= 26) { // Only valid numbers between 10 and 26
                std::vector<int> vec_copy = vec;
                vec_copy.push_back(two_digit);
                sub2 = devider(vec_copy, s.substr(2));
                ans.insert(ans.end(), sub2.begin(), sub2.end());
            }
        }

        return ans;
    }
};
