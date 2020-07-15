#include <iostream>
#include <string>
using namespace std;

//checks to see if the anagrams have the same number of characters

bool anagramsolution1(string s1, string s2){
    bool stillOK = true;
    if (s1.length() != s2.length()) {
        stillOK = false;
        return stillOK;
    }
    string locals2 = s2;
    int n = s1.length();
    unsigned int pos1 = 0;

    // checks to see if all of the letters are the same in both inputs

    while (pos1 < s1.length() && stillOK){
        int pos2 = 0;
        bool found = false;
        while (pos2 < n && !found){
            if (s1[pos1] == locals2[pos2]){
                found = true;
            } else{
                pos2 = pos2 + 1;
            }
        }
        if (found){
            locals2[pos2] = '\0';
        }
        else{
            stillOK = false;
        }
        pos1 = pos1 + 1;
    }
    return stillOK;
}

int main(){
    bool value = anagramsolution1("abcd", "dcab");
    cout << value << endl;
    return 0;
}

