#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector> 
using namespace std;
const int maxn = 100010;
struct stu
{
	int num;
	int rank;
}s[maxn];

bool cmp(stu a, stu b){
	if(a.num != b.num) return a.num > b.num;
}

class Solution {
public:
    int thirdMax(vector<int>& nums) {
        int length = nums.size();
		int count = 0;
		for (int i = 0; i < length; i++){
			s[count].num = nums[i];
			count++;
		}
		sort(s, s + count, cmp);
		s[0].rank = 1;
		int index;
		bool flag = false;
		for (int i = 1; i < count; ++i){
			if(s[i].num == s[i-1].num) s[i].rank = s[i-1].rank;
			else s[i].rank = i + 1;
			if(s[i].rank == 3){
				flag = true;
				index = i;
			}
		}
		if(flag == false) return s[0].num;
		else return s[index].num;
    }
};

int main(){
	vector<int> nums;
	for (int i = 0; i < 3; ++i)
	{
		nums.push_back(i + 1);
	}
	class test = Solution();
	int ans  = test.thirdMax();
	printf("%d\n", ans);
}
