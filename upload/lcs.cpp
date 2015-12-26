#include <iostream>
#include <String>
#define MAX_LENGTH 100
using namespace std;


int c[MAX_LENGTH][MAX_LENGTH] = {0};
int d[MAX_LENGTH][MAX_LENGTH] = {0};

int SearchLCS(string a,string b){

	for(int i =0 ;i<=a.length();i++)
	{
		for (int j=0 ;j<=b.length();j++)
		{
			if(i == 0 || j == 0){
				c[i][j] = 0;
			}
			else if(a[i-1] == b[j-1]){
				c[i][j] = c[i-1][j-1] + 1;
				d[i][j] = 2;
			}
			else if(a[i-1] != b[j-1]){
				c[i][j] = c[i][j-1] > c[i-1][j] ? c[i][j-1] : c[i-1][j];
				d[i][j] = c[i][j-1] > c[i-1][j] ? 1 : 0 ;
			}

		}
	}
	return c[a.length()][b.length()];

}
void PrintChar(string a,string* b)
{
    string a_temp = "";
    int i=a.length();
    int j=b->length();
    int j_t=0;
    while(i > 0 )
    {
        if(d[i][j]==0)
        {
            i--;
        }
        else if(d[i][j] == 1)
        {
            j--;
        }
        else if(d[i][j] == 2){
            char a_t = a[i-1];
            a_temp.push_back(a_t);
            j_t = j-1 ;
            i--;j--;
        }
    }
    for (int i=a_temp.length()-1;i>=0;i--)
    {
        cout << a_temp[i];
    }
    cout << endl;
    b->erase(j_t,1);
    cout << endl ;
}

void show(string a,string b){
    for(int i =0 ;i<=a.length();i++)
	{
		for (int j=0 ;j<=b.length();j++)
		{
			cout << d[i][j];
		}
		cout << endl;
	}
	cout << endl ;
        for(int i =0 ;i<=a.length();i++)
	{
		for (int j=0 ;j<=b.length();j++)
		{
			cout << c[i][j];
		}
		cout << endl;
	}
}
void reset(){
    c[MAX_LENGTH][MAX_LENGTH] = {0};
    d[MAX_LENGTH][MAX_LENGTH] = {0};
}
int main()
{
    string a,b;
    while (true){
        cin >> a >> b ;
        int ans = SearchLCS(a,b);
        show(a,b);
		PrintChar(a,&b);
		reset();
        int ans2 = SearchLCS(a,b);
        cout << ans2 <<endl;
        show(a,b);
        if(ans2 = ans ){
            PrintChar(a,&b);
        }
    }
    return 0;
}
