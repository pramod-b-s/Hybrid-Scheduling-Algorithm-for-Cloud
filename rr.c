#include <stdio.h>
#include <stdlib.h>

int f=-1,r=-1,size=0,q[100];

struct process{
	int at,bt,no,ct,done,tat,wt,ts,vis;
}p[100];

void nq(int x){
	q[++r]=x;
	size++;
}

void swappr(struct process *a,struct process *b,int n){
	int i,j;
	struct process t;
	t=*a;
	*a=*b;
	*b=t;
}

int dq(){
	size--;
	return q[++f];
}

void dispi(int n){
	int i;
	printf("No.\tAT\tBT\n");
	for(i=0;i<n;i++){
		printf("%d\t%d\t%d\n",i,p[i].at,p[i].bt);
	}
	printf("\n");
}

void disp(int n){
	int i,tatsum=0,wtsum=0;
	printf("No.\tAT\tBT\tCT\tTAT\tWT\t\n");
	for(i=0;i<n;i++){
		printf("%d\t%d\t%d\t%d\t%d\t%d\n",i,p[i].at,p[i].bt,p[i].ct,p[i].tat,p[i].wt);
		tatsum+=p[i].tat;
		wtsum+=p[i].wt;
	}
	printf("\n");
	printf("Avg TAT=%f\nAvg WT=%f\n\n",(float)tatsum/(float)n,(float)wtsum/(float)n);
}

int done(int n){
	int i;
	for(i=0;i<n;i++){
		if(p[i].done==0){
			return 0;
		}
	}
	return 1;
}

void swap(int *p,int *q){
   int t;
   
   t=*p; 
   *p=*q; 
   *q=t;
}

void sort(int a[],int n){ 
   int i,j,temp;

   for(i = 0;i < n-1;i++) {
      for(j = 0;j < n-i-1;j++) {
         if(a[j] > a[j+1])
            swap(&a[j],&a[j+1]);
      }
   }
}

double findMedian(int a[], int n) { 
    sort(a, n); 
  
    if (n % 2 != 0){
       return (double)a[n/2]; 
    }
    return (double)(a[(n-1)/2] + a[n/2])/2.0; 
} 

void main(){

	int i,j,n,k,time=0,x,localsize=0;
	
	n=6;
	int atime[6]={0,0,1,2,3,4};
	int btime[6]={12,8,23,10,30,15};

	// n=10;
	// int atime[10]={0,1,2,3,4,4,4,5,3,6};
	// int btime[10]={49,98,143,187,244,252,199,67,83,75};

	// n=10;
	// int atime[10]={0,1,2,3,4,5,3,3,4,6};
	// int btime[10]={251,177,152,299,47,84,244,124,55,180};

	// n=10;
	// int atime[10]={0,1,2,3,4,5,6,7,4,8};
	// int btime[10]={33,201,98,116,11,100,33,78,18,64};

	for(i=0;i<n;i++){
		p[i].at=atime[i];
		p[i].bt=btime[i];
		p[i].no=i;
		p[i].done=0;
		p[i].vis=0;
		p[i].ts=0;
	}
	dispi(n);
	int tq;
	tq=findMedian(btime,n);

	printf("sorted according to AT\n");
	for(i=0;i<n;i++){
		for(j=0;j<n-i-1;j++){
			if(p[j].at>p[j+1].at){
				swappr(&p[j],&p[j+1],n);
			}
		}
	}
	for(i=0;i<n;i++){
		p[i].no=i;
	}
	printf("\nTQ=%d\n",tq);
	dispi(n);

	k=0;
	while(done(n)==0){
		while(k<n){
			if(p[k].at<=time){
				nq(p[k].no);
				localsize++;
				p[k].vis=1;
				k++;
			}
			else{
				break;
			}
		}

		if(localsize){
			x=dq();
			time+=tq;

			while(k<n){
			if(p[k].at<=time){
				nq(p[k].no);
				localsize++;
				p[k].vis=1;
				k++;
			}
			else{
				break;
			}
		}

			p[x].ts+=tq;
			if(p[x].ts>=p[x].bt){
				p[x].done=1;
				time-=(p[x].ts-p[x].bt);
				p[x].ct=time;
				p[x].tat=p[x].ct-p[x].at;
				p[x].wt=p[x].tat-p[x].bt;
			}
			else{
				nq(x);
			}
		}
		else{
			time++;

			while(k<n){
			if(p[k].at<=time){
				nq(p[k].no);
				localsize++;
				p[k].vis=1;
				k++;
			}
			else{
				break;
			}
		}
			
		}
		//printf("%d\n",x)
	}

	disp(n);

}
