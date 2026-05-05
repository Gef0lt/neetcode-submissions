class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack;
        for (char c : s) {
            if (c == '{' || c == '[' || c == '(') {
                stack.push(c);
            } else if (stack.empty()) {
                return false;
            } else if (c == '}' && stack.top() == '{') {
                stack.pop();
                continue;
            } else if (c == ')' && stack.top() == '(') {
                stack.pop();
                continue;
            } else if (c == ']' && stack.top() == '[') {
                stack.pop();
                continue;
            } else {
                return false;
            }
        }
        if (stack.empty())
            return true;
        return false;
    }
    
};
