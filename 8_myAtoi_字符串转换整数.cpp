class Solution {
public:
    int myAtoi(string str) {
        long int res=0;
        int sign=1;
        int i=0;
        for(;i<str.length();i++){
            if(str[i]==' '){
                continue;
            }else if(str[i]>='0' && str[i]<='9'){
                res=str[i]-'0';
                break;
            }else if(str[i]=='+'){
                break;
            }else if(str[i]=='-'){
                sign=-1;
                break;
            }
            else{
                return 0;
            }
        }
        for(i++;i<str.length();i++){
            if(str[i]>='0' && str[i]<='9'){
                res=res*10+str[i]-'0';
                if(sign*res>2147483647) return 2147483647;
                if(sign*res<-2147483648) return -2147483648;
            }
            else return sign*res;
        }
        return sign*res;
    }
};
//4ms,81.82%
//6.2MB,100%
