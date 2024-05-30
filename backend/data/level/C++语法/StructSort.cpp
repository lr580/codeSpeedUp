#include <bits/stdc++.h>
using namespace std;
struct student {
    int chinese, math, english, id;
};
bool cmp(student a, student b) {
    if(a.chinese+a.math+a.english!=b.chinese+b.math+b.english) {
        return a.chinese+a.math+a.english < b.chinese+b.math+b.english;
    }
    if(a.chinese!=b.chinese) {
        return a.chinese < b.chinese;
    }
    if(a.math!=b.math) {
        return a.math < b.math;
    }
    if(a.english!=b.english) {
        return a.english < b.english;
    }
    return a.id > b.id;
}
int main() {
    student s[100];
    int n;
    cin>>n;
    for(int i=0;i<n;++i) {
        cin>>s[i].chinese>>s[i].math>>s[i].english;
        s[i].id=i+1;
    }
    sort(s, s+n, cmp);
    reverse(s, s+n);
    for(int i=0;i<n;++i) {
        cout<<s[i].id<<' ';
    }
    return 0;
}