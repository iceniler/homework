// 计算两点之间距离
#include <stdio.h>
#include <math.h>

double CalLen(double, double, double, double);

int main(int argc, char** argv){
	double distance, x1, y1, x2, y2;
	scanf("%lf,%lf,%lf,%lf", &x1,&y1,&x2,&y2);

	distance = CalLen(x1,y1,x2,y2);
	printf("Distance is %lf\n", distance);
	return 0;
}

double CalLen(double x1, double x2, double y1, double y2){
	return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2));
}
