#include <iostream>
#include <fstream>
#include <vector> 
using namespace std; 


string TEST = "Day4Test.txt";
string DATA = "Day4Data.txt";
vector<string> Mapa;
vector<string> newMap; 

bool bounded(int tam, int max){
    if(tam < 0) return false; 
    if(tam >= max) return false; 
    return true; 
}

void print(vector<string> cosa){
    for(int i = 0; i < cosa.size(); ++i){
        for(int j = 0; j < cosa.size(); ++j){
            cout << cosa[i][j];
        }
        cout << endl; 
    }

}


bool pasaElTest(int x, int y){
    int cercanos = 0;
    int tam = Mapa.size();
    for(int i = x-1; i <= x+1; ++i){
        for(int j = y-1; j <= y+1; ++j){
            if(i == x && y == j); 
            else if(bounded(i, tam) && bounded(j, tam) && Mapa[i][j] == '@'){ 
                cercanos++;  
            }
        }
    }
    if(cercanos<4){
        newMap[x][y] = '.';
        return true;
    }
    return false; 
}

int main(){
    
     
    ifstream file (DATA);

    string s;
    while(getline(file,s)) Mapa.push_back(s); 
    newMap = Mapa;
    int forklift_certificated_values = 0;


    bool first = true; 
    while(1){
        
        
        int addendum = 0; 
        for(int i = 0; i < Mapa.size(); ++i){
            for(int j = 0; j < Mapa[i].size(); ++j){
                if(Mapa[i][j] == '@' && pasaElTest(i,j)) addendum++;
            }
        }
        forklift_certificated_values += addendum; 
        if(first){ 
            cout << "Problema 1: " << forklift_certificated_values << endl;
            first = false;
        }
        if(addendum == 0) break; 
        Mapa = newMap;
        //print(Mapa);
        //cout << "-----------" << endl;
        //print(newMap);
        //cout << "actualizo mapa" << endl;   
    }
    cout << "Problema 2: " << forklift_certificated_values << endl;
    



}