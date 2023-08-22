#include<iostream>
using namespace std;
int main(){
    char out;
    cout << "Enter your choice of ICE CREAM: ";
    cin >> out;
    if(tolower(out)== 'choclate'){
        cout>>"ICE CREAM of your choice is " << out << endl;
    }
    else if (tolower(out)== 'vanilla"){
        cout>>"ICE CREAM OF YOUR CHOICE IS: " << out << endl;
    }
    else{
        cout>>"Invalid." << out << endl;
    }
    return 0;
}