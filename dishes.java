import java.util.*;
import java.io.*;
public class dishes{
public static void main(String args[]) throws IOException{
BufferedReader lector = new BufferedReader(new InputStreamReader(System.in));
StringBuffer sb = new StringBuffer("");
//Vector<p> nose = new Vector<p>();
//int a = Integer.parseInt(lector.readLine());
//String aa[] = lector.readLine().split("");
String aa[] = lector.readLine().split(" ");
int n = Integer.parseInt(aa[0]);
int m = Integer.parseInt(aa[1]);
int k = Integer.parseInt(aa[2]);//n,m,k = map(int,raw_input().split(" "))
aa = lector.readLine().split(" ");
int a[] = new int[n];
for(int nn = 0;nn<n;nn++)a[nn]=Integer.parseInt(aa[nn]);//a = map(int,raw_input().split(" "))
Vector<Vector<Integer>> rt = new Vector<Vector<Integer>>();
for(int nn = 0;nn<n+1;nn++)rt.add(new Vector<Integer>());//rt = [[] for i in range(n+1)]
for(int x = 0;x<(1<<n);x++)rt.get(Integer.bitCount(x)).add(x);
//for x in range(1<<n):
//        rt[CountBits(x)].append(x)
int mat[][] = new int[n][n];
//mat = [[0 for i in range(n)] for j in range(n)]
for(int nn = 0;nn<k;nn++){
aa = lector.readLine().split(" ");
int c0 = Integer.parseInt(aa[0])-1;
int c1 = Integer.parseInt(aa[1])-1;
int c2 = Integer.parseInt(aa[2]);
mat[c0][c1]=c2;
}
//for _ in range(k):
//        c = map(int,raw_input().split(" "))
//        mat[c[0]-1][c[1]-1] = c[2]
long dp[][] = new long[1<<n][n];//dp = [[0 for i in range(n)] for j in range(1<<n)]
for(int i = 0;i<n;i++)//for i in range(n):
        dp[1<<i][i]=a[i];
for(int i = 2;i<m+1;i++){// i in range(2,m+1):
        for(int x:rt.get(i)){
                for(int j = 0;j<n;j++){// j in range(n):
                        if(((1<<j)&x)==0)
                                continue;
                        int xx = x^(1<<j);
                        for(int l = 0;l<n;l++){
                                if(l==j || ((1<<l)&x)==0)
                                        continue;
                                dp[x][j]=Math.max(dp[x][j],dp[xx][l]+a[j]+mat[l][j]);
}
}
}
}
long s = 0;
for(int x:rt.get(m))// x in rt[m]:
        for(int i = 0;i<n;i++)// i in range(n):
                s = Math.max(s,dp[x][i]);
//print(s)
System.out.println(s);
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
	
