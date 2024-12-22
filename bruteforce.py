#include <iostream>
#include<cstring>

using namespace std;

int main()
{
    int n,x;
    double Total_bill;
    string s,s1,s2;
    s1="Domestic";
    s2="Private";
    cout<<"Domestic or Private"<<endl;
    cin>>s;
    cout<<"Enter the total numbers in the house"<<endl;
    cin>>x;
    cout<<"Total Number of Units used"<<endl;
    cin>>n;
    if(s==s1){
        if(n>0&&n<101)
        Total_bill = (n*4.80);
        if(n>100&&n<200)
        Total_bill = (n*5.80);
        if(n>200)
        Total_bill = (n*6.50);
        }
    if(s==s2){
        if(n>0&&n<101)
        Total_bill = (n*6.05);
        if(n>100)
        Total_bill = (n*6.70);
        }
    cout<<"Total bill = "<<Total_bill<<endl; 
    cout<<"Bill per each person = "<<Total_bill/x<<endl;
    cout<<"\"Save Energy, Save Money, Save Nation, Save the planet....!!!\"";    
    
    return 0;
}