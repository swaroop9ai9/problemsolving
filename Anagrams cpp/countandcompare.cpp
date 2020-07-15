#include <iostream>
#include <string>
using namespace std;

// uses an array to count the number of a ocurrences of the two inputs
// if the number of occurrences is the same then the input is an anagram

bool anagramSolution4(string s1, string s2){
    int c1[26] = {0};
    int c2[26] = {0};

    int x;
    int a = 'a';
    for (unsigned int i = 0; i < s1.length(); i++){
        x = s1[i] - a;
        int pos = x;
        c1[pos] = c1[pos] + 1;
    }

    int y;
    int b = 'a';
    for (unsigned int i = 0; i < s2.length(); i++){
        y = s2[i] - b;
        int pos = y;
        c2[pos] = c2[pos] + 1;
    }

    int j = 0;
    bool stillOK = true;
    while (j < 26 && stillOK){
        if (c1[j] == c2[j]){
            j = j + 1;
        } else{
            stillOK = false;
        }
    }
    return stillOK;
}

int main(){
    bool value = anagramSolution4("apple", "pleap");
    cout << value << endl;
    return 0;
}

