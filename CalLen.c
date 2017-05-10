// 计算两点之间距离
#include <stdio.h>
#include <math.h>
// 函数声明
double CalLen(double, double, double, double);
// main函数
int main(int argc, char** argv){
	double distance, x1, y1, x2, y2;
	scanf("%lf,%lf,%lf,%lf", &x1,&y1,&x2,&y2); // 用%lf 接受浮点数给x1,y1,x2,y2 输入时用 逗号分开 例如： 1,2,3,4

	distance = CalLen(x1,y1,x2,y2); // 调用函数计算
	printf("Distance is %lf\n", distance); // 输出时用 %lf 指定输出的数据类型
	return 0;
}

// 计算两点间距离的函数
double CalLen(double x1, double x2, double y1, double y2){
	// sqrt为开平方函数
	// pow为幂计算函数 返回第一个参数的第二个函数次幂的值 pow(2,3) == 8
	return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2));
}
