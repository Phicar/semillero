import java.util.*;
import java.io.*;
public class apollo{
public static long mod = 1000000007;
public static int modd = 1000000007;
public static void main(String args[]) throws IOException{
BufferedReader lec = new BufferedReader(new InputStreamReader(System.in));
long tr = System.currentTimeMillis();
long pp[] = new long[60];
pp[0]=1L;
for(int n = 1;n<60;n++)
pp[n]=pp[n-1]<<1;
int tt = Integer.parseInt(lec.readLine());
StringBuffer sb = new StringBuffer("");
for(int ttt = 0;ttt<tt;ttt++){
int ans = 0;
int b = Integer.parseInt(lec.readLine());
String aa = lec.readLine();
long a[] = new long[b];
long q[] = new long[60];
int k = 0;
char ak = '-';
for(int n = 0;n<b;n++){
//long aan = 0;
ak = '-';
while(k<aa.length() && (ak=aa.charAt(k))!=' '){
a[n]=10L*a[n]+(ak-'0');
k+=1;
}
k+=1;
//a[n]=Long.parseLong(aa[n]);
for(int m = 0;m<60;m++)
if((a[n]&pp[m])!=0)q[m]+=1L;
}
long brr = (long)b;
//if(b==500000 && a[0]==1152921504606846975L)System.out.println("->"+(System.currentTimeMillis()-tr));
long ab =0;
long bb = 0;
long s0 =0;
long s1=0;
long pot = 0;
long bn = 0;
long pott = 0;
for(int n = 0;n<b;n++){
s0 = 0;
s1 = 0;
for(int m = 0;m<60;m++){
pot = pp[m];
bn = a[n]&pot;
ab = 0;
bb = 0;
pot = pot%mod;
if(bn!=0){
ab=q[m];
bb=brr;
s0 = (s0+ab*pot)%mod;
}else
bb=q[m];
//s0 = (s0+(ab*pot)%mod)%mod;
s1 = (s1+(bb*pot))%mod;
}
ans = (ans+(int)(((s0*s1))%mod))%modd;
}
sb.append(ans+"\n");
//if(b==500000 && a[0]==1152921504606846975L)System.out.println("->"+(System.currentTimeMillis()-tr));
//if(b==500000)
//System.out.println("->"+(System.currentTimeMillis()-tr));
}
System.out.print(sb);
//System.out.flush();
}
}
