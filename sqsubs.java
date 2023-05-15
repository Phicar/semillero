import java.util.*;
import java.io.*;
public class sqsubs{
public static long mod = 1000000007;
public static void main(String args[]) throws IOException{
BufferedReader lector = new BufferedReader(new InputStreamReader(System.in));
int a = Integer.parseInt(lector.readLine());
int crib[] = new int[71*71];
for(int n = 2;n<72;n++)
if(crib[n]==0)
for(int m = n;m<crib.length;m+=n)
crib[m]=n;
int b[] = new int[a];
String bb[] = lector.readLine().split(" ");
Vector<Integer> pr = new Vector<Integer>();
pr.add(2);
for(int n = 3;n<70;n+=2)if(crib[n]==n)pr.add(n);
System.out.println(pr);
int desc[][] = new int[a][pr.size()];
for(int n =0;n<a;n++){
b[n] = Integer.parseInt(bb[n]);
int xx = b[n];
for(int m = 0;xx>1 && m<pr.size();m++){
int pp = pr.get(m);
while(xx%pp==0){
desc[n][m]++;
xx/=pp;
}
}
}
long ans = 0;
for(int s = 0;s<(1<<pr.size());s++){
long vec = 1;
for(int m = 0;m<pr.size();m++){
if((s&(1<<m))==0)continue;

}
}
System.out.println(ans);
}
}
