#include <iostream>
#include <vector> 

using namespace std;


int main()
{
    string c, c2, c3; 
    int sumOfPrios; 
    sumOfPrios = 0; 
    vector<int> rep; 
    char rep2 = '1'; 
    while(1){
        while(getline(cin, c)){
            getline(cin, c2);
            getline(cin, c3);
            for(int i = 0; i < c.size(); ++i){
                for(int j = 0; j < c2.size(); ++j){
                    if (c[i] == c2[j]){
                        rep.push_back(c[i]);
                    } 
                }
            }
            for(int i = 0; i<rep.size(); ++i){
                for(int j = 0; j < c3.size(); ++j){
                    if(rep[i] == c3[j]){
                        rep2 = rep[i];
                        i = rep.size();
                        j = c3.size(); 
                    }
                }
            }
            if(rep2 == '1'){}
            else if(rep2 >= 'a' and rep2 <= 'z') sumOfPrios += rep2 - 'a' + 1; 
            else sumOfPrios += rep2 - 'A' + 27; 
            //cout << "Prios so far: " << sumOfPrios << endl;
            rep.clear(); 
            //cout << "Letra encontrada: " << rep2 <<" y size rep: " << rep.size() <<  endl; 

            rep2 = '1'; 
        }
    }
}
