import java.io.*;
import java.util.*;
public class news{
public static int pad[][];
public static int find(int a){
//System.out.println(a+" "+pad[a][0]+" "+(a==pad[a][0]));
if(a==pad[a][0])return a;
pad[a][0]=find(pad[a][0]);
return pad[a][0];
}
public static void union(int a,int b){
int pa = find(a);
int pb = find(b);
if(pa==pb)return;
pad[pa][0]=pb;
pad[pb][1]+=pad[pa][1];
}
public static void main(String args[]) throws IOException{
BufferedReader lector = new BufferedReader(new InputStreamReader(System.in));
String tt[] = lector.readLine().split(" ");
int a = Integer.parseInt(tt[0]);
int b = Integer.parseInt(tt[1]);
pad = new int[a][2];
for(int n = 0;n<a;n++){
pad[n][0]=n;
pad[n][1]=1;
}
StringBuilder sb = new StringBuilder("");
for(int n = 0;n<b;n++){
tt = lector.readLine().split(" ");
for(int m = 1;m<tt.length;m++)
union(Integer.parseInt(tt[m])-1,Integer.parseInt(tt[1])-1);

}
for(int m =0;m<a;m++)sb.append(pad[find(m)][1]+(m==a-1?"\n":" "));
System.out.print(sb);
}
}
