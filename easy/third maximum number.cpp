#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
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
int main(){
	char a[maxn];
	gets(a);
	int length = strlen(a);
	int count = 0;
	for (int i = 1; i < length - 1;){
		s[count].num = a[i] - '0';
		i += 3;
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
	if(flag == false) printf("%d\n", s[0].num);
	else printf("%d\n", s[index].num);
	return 0;
}

