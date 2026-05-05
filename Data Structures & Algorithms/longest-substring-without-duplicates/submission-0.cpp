class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() < 1)
            return s.size();

        int l = 0, r = 1, max_l = 1;
        std::set<char> ch;
        ch.insert(s[0]);
        while (r < s.size()) {
            while (r < s.size() && ch.find(s[r]) == ch.end()) {
                ch.insert(s[r]);
                r++;
            }
            max_l = max(max_l, r - l);

            while (ch.find(s[r]) != ch.end()) {
                ch.erase(s[l]);
                l++;
            }
            
            ch.insert(s[r]);
            r++;
        }
        return max_l;
    }
};
