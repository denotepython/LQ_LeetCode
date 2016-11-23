#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
	class Solution {
	public:
	    vector<int> searchRange(vector<int>& nums, int target) {
	        int length = nums.size();
	        int left = lower_bound(nums, nums + length, target) - nums;
	        int right = upper_bound(nums, nums + length, target) - nums - 1;
	        vector<int> ans;
	        ans.push_back(left);
	        ans.push_back(right);
	        return ans;
	    }
	};
	vector<int> nums = [5,7,7,8,8,10];
	int target = 7;
	result = Solution().searchRange(vector<int>& nums, int target);
	printf("[%d, %d]\n", result[0], result[1]);
}


