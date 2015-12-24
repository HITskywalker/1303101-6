/*************************************************************************
    > File Name: Maze2.cpp
    > Author: muyeby
    > Mail: muyeby@gmail.com 
    > Created Time: 2015年04月05日 星期日 21时01分05秒
 ************************************************************************/

#include<iostream>
using namespace std;
int sI=1,sJ=1,eI=7,eJ=7;
void visit(int i,int j);
int maze[9][9]={{2,2,2,2,2,2,2,2,2}
	,{2,0,0,0,0,0,0,0,2}
	,{2,0,2,2,0,2,2,0,2}
	,{2,0,2,0,0,2,0,0,2}
	,{2,0,2,0,2,0,2,0,2}
	,{2,0,0,0,0,0,2,0,2}
	,{2,2,0,2,2,0,2,2,2}
	,{2,0,0,0,0,0,0,0,2}
	,{2,2,2,2,2,2,2,2,2}
};
int main(){
	cout<<"显示迷宫:\n";
	for(int i=0;i<9;i++){
		for(int j=0;j<9;j++)
			if(maze[i][j]==2)
				cout<<"&";
			else
				cout<<" ";
		cout<<endl;
	}
	visit(sI,sJ);
	return 0;
}
void visit(int i,int j){
	maze[i][j]=1;
	if(i==eI&&j==eJ){
		cout<<"\n显示路径:\n";
		for(int m=0;m<9;m++){
			for(int n=0;n<9;n++)
				if(maze[m][n]==2)
					cout<<"&";
				else if(maze[m][n]==1)
					cout<<"^";
				else
					cout<<" ";
			cout<<endl;
		}
	}
	if(maze[i][j+1]==0) visit(i,j+1);
	if(maze[i+1][j]==0) visit(i+1,j);
	if(maze[i][j-1]==0) visit(i,j-1);
	if(maze[i-1][j]==0) visit(i-1,j);
	maze[i][j]=0;
}
