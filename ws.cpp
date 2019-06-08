#include<iostream>
#include<string.h>
using namespace std;
string weave(string str1, string str2){
	int i = 0;
	string rs;
	while(i != str1.length() && i != str2.length()){
		rs += str1[i] + str2[i];
		i++;

	}
	if(i < str1.length()){
		while( i != str1.length()){
			rs += str1[i];
			i++;
		}

	}
	if(i < str2.length()){
		while( i != str2.length()){
			rs += str2[i];
			i++;
		}

	}
	return rs;
}


int main(int argc, char *argv[]){
	cout << weave(argv[1], argv[2]) << endl;
	return 0;
}
