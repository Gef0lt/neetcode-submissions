class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        std::unordered_map<char, int> h1;
        std::unordered_map<char, int> h2;

        for (char c : s) {
            if (h1.find(c) == h1.end()) {
                h1.insert(std::make_pair(c, 1));
            } else {
                h1[c]++;
            }
        }
        for (char c : t) {
            if (h2.find(c) == h2.end()) {
                h2.insert(std::make_pair(c, 1));
            } else {
                h2[c]++;
            }
        }

        return h1 == h2;
    }
};
