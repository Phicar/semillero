import java.util.*;
import java.io.*;
public class bicoloring{
public static void main(String args[]) throws IOException{
BufferedReader lector = new BufferedReader(new InputStreamReader(System.in));
StringBuffer sb = new StringBuffer("");
long mod = 998244353L;
long dd[][] =new long[4][4];// = [[0 for i in range(1<<2)] for j in range(1<<2)]
dd[0][0]=0;
dd[0][1]=1;
dd[0][2]=1;
dd[0][3]=1;
dd[1][0]=0;
dd[1][1]=0;
dd[1][2]=2;
dd[1][3]=0;
dd[2][0]=0;
dd[2][1]=2;
dd[2][2]=0;
dd[2][3]=0;
dd[3][0]=1;
dd[3][1]=1;
dd[3][2]=1;
dd[3][3]=0;
//dp = [[[0 for k in range(1<<2)] for j in range(2001)] for i in range(1001)]
long dp[][][] = new long[1001][2001][4];
for(int x = 0;x<4;x++){//for x in range(1<<2):
	int a = x%2;
	int b = x/2;
	if(a==b)
		dp[1][1][x]+=1;
	else
		dp[1][2][x]+=1;
}
for(int l=2;l<1001;l++)// l in range(2,1001):
	for(int j = 1;j<=2*(l-1);j++)// j in range(1,2*(l-1)+1):
		for(int k = 0;k<4;k++)//for k in range(1<<2):
			for(int kk = 0;kk<4;kk++)//for kk in range(1<<2):
				dp[l][j+(int)dd[kk][k]][k]=(dp[l][j+(int)dd[kk][k]][k]+dp[l-1][j][kk])%mod;
//for i in range(3):
//	for j in range(1,2*i+1):
//		print(i,j,dp[i][j])
String aa[] = lector.readLine().split(" "); //a = map(int,raw_input().split(" "))
long s = 0;
int a[] = {(int)Long.parseLong(aa[0]),(int)Long.parseLong(aa[1])};
for(int x = 0;x<4;x++)//for x in range(1<<2):
	s+=dp[a[0]][a[1]][x];
//print(s%mod)
//Vector<p> nose = new Vector<p>();
//int a = Integer.parseInt(lector.readLine());
//String aa[] = lector.readLine().split("");
System.out.println(s%mod);
}
}
class p implements Comparable<p>{
public int a=0;
public p(int a){
this.a = a;
}
public int compareTo(p q){
return (int)Math.signum(q.a-this.a);
}
public String toString(){
return this.a+"";
}
}
	
