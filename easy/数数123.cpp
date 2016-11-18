#include <cstdio>

const int people = 300;
bool three[people + 1] = {false};

int num = 0, count = 0, loop = 1;
int main(){
	while(num != people - 1){
		for (int i = 1; i <= people; ++i)
		{
			if(three[i] == false){
				if(loop % 3 == 0){
					three[i] = true;
					num++;
					loop = 1;
					printf("%d\n", i);
				}
				else{
					loop++;
				}
				count++;
			}
		}
	}
	printf("count%d\n", count - 1);
	return 0;
}
