class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0, r = 1, total = 0, curr = 0;

        while (r < height.size() - 1) {
        while (r < height.size() - 1 && height[r+1] > height[r]  && height[r+1] <= height[l]) {
            r++;
        }
        if (height[r] < height[l]) {
            for (int i = r + 1; i < height.size(); i++) {
                if (height[i] > height[r]) {
                    r = i;
                    if (height[r] >= height[l])
                        break;
                }

            }
        }

        for (int i = l + 1; i < r; i++)
            curr += height[i];

        if (height[l] < height[r]) {
            if (height[l] * (r - l - 1) - curr > 0)
                total += height[l] * (r - l - 1) - curr;
        }
        else {
            if (height[r] * (r - l - 1) - curr > 0)
                total += height[r] * (r - l - 1) - curr;
        }

//        std::cout << total << '\n';
        l = r;
        r++;
        curr = 0;
        }
        return total;
    }
};