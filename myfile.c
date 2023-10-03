#include<stdio.h>
#include<stdlib.h>
int main(){
	int n,i,j,count=0,k,index;
	int queue[n],head,headmov=0,diff,visited[n];
		
		
		
	printf("enter the number of requests:");
	scanf("%d",&n);

	
	printf("enter the %d requests:",n);
	for(i=0;i<n;i++)
	{
	    visited[i]=0;
		scanf("%d",&queue[i]);
	}
	printf("enter the head:");
	scanf("%d",&head);
	
	
	while(n--){
		int min=1000000;
		for(i=0;i<n;i++){
		    
			diff=abs(head-queue[i]);
			if(diff<min)
			{
				min=diff;
				index=i;
			}
		}
		
			headmov=headmov+min;
			head=queue[index];
		
	
	}
	printf("Total Head Movement is :%d",headmov);
	return 0;
}