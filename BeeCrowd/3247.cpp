#include <iostream>
#include <queue>
#include <cmath>
#include<map>
using namespace std;

#define debug(x) cout<<#x<<"= "<<x<<endl
#define mod(x) ((x)>0)?(x):(-(x))
#define MAX(a,b) ((a)>(b))? (a):(b)
#define MIN(a,b) ((a)<(b))? (a):(b)

class node{
public:
	int x;
	int y;

	node(int x, int y)
	{
		this->x = x;
		this->y = y;
	}
};

bool insideGrid (int rows, int cols, int x, int y){
	if (x>=0 && x<rows && y>=0 && y<cols) return true;
	else return false;
}

void push_node (int x, int y, const vector<vector<long long> > &grid,vector<vector<bool> > &vis, queue<node> &q){
	if (insideGrid(grid.size(), grid.size(), x, y) && grid[x][y]>=0 && !vis[x][y]){
		vis[x][y] = true;
		q.push(node(x, y));
	}
}

int bfs(vector<vector<long long> > &grid){
	int n = grid.size();
	queue<node> q;
	vector<vector<bool> > vis;

	for (int i=0; i<n; i++){
		vis.push_back(vector<bool>());
		for (int j=0; j<n; j++) vis[i].push_back(false);
	}

	q.push (node(0, 0));
	vis[0][0] = true;
	while (!q.empty()){
    int x, y;
		node popNode = q.front();
		q.pop();

		if (popNode.x==n-1 && popNode.y==n-1) return true;

    //direita
		x = popNode.x;
		y = popNode.y+1;
		push_node(x, y, grid, vis, q);
    //esquerda
		x = popNode.x-1;
		y = popNode.y;
		push_node(x, y, grid, vis, q);
    //cima
		x = popNode.x+1;
		y = popNode.y;
		push_node(x, y, grid, vis, q);
    //baixo
		x = popNode.x;
		y = popNode.y-1;
		push_node(x, y, grid, vis, q);
	}
	return false;
}

void dynamicMatrix(vector<vector<long long> > &grid){
	int size = grid.size();
	long long modulo = (1LL<<31) -1;
  bool flag = false;

  // coluna 0
	for (int i=0; i<size; i++){
    if (grid[i][0] == 0) grid[i][0] = 1;
		else break;
  }
  // linha 0
	for (int i=1; i<size; i++){
    if (grid[0][i] == 0)grid[0][i]=1;
		else break;
  }
		
	for (int i=1; i<size; i++){
    for (int j=1; j<size; j++){
			if (grid[i][j]==-1)continue;
			if (grid[i-1][j] > 0) grid[i][j] = (grid[i][j] + grid[i-1][j]) % modulo;
			if (grid[i][j-1] > 0) grid[i][j] = (grid[i][j]+ grid[i][j-1]) % modulo;
		}
  }
}

int main (){
	int n;
	cin>>n;
	vector<vector<long long> > grid;
	for (int i=0; i<n; i++){
		grid.push_back(vector<long long>());
		for (int j=0; j<n; j++){
			char c;
			cin>>c;
			if (c == '#') grid[i].push_back(-1);
			else grid[i].push_back(0);
		}
	}

	dynamicMatrix(grid);
	if (grid[n-1][n-1] != 0){
    cout<<grid[n-1][n-1]<<endl;
  }else{
		if (!bfs(grid)) cout<<"INCONCEIVABLE"<<endl;
		else cout<<"THE GAME IS A LIE"<<endl;
	} 
}