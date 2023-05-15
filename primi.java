import java.util.*;
import java.io.*;
public class primi{
public static void main(String args[]) throws IOException{
BufferedReader lector = new BufferedReader(new InputStreamReader(System.in));
StringBuffer sb = new StringBuffer("");
int crib[] = new int[10000001];
int sq = (int)Math.sqrt(10000000)+1;
for(int x = 2;x<sq;x++){
if(crib[x]!=0)continue;
for(int y = x;y<10000001;y+=x)crib[y]=x;
}
//Vector<p> nose = new Vector<p>();
int a = Integer.parseInt(lector.readLine());
//String aa[] = lector.readLine().split("");
for(int cc = 0;cc<a;cc++){
long ans = 0;
int nn = Integer.parseInt(lector.readLine());
String br[] = lector.readLine().split(" ");
HashMap<Integer,Integer> ha = new HashMap<Integer,Integer>();
for(int n = 0;n<nn;n++){
int xx = Integer.parseInt(br[n]);
while(crib[xx]>0){
int q = 0;
int c = crib[xx];
while(xx%c==0){
q+=1;
xx/=c;
}
if(!ha.keySet().contains(c))ha.put(c,q);
else
ha.put(c,ha.get(c)+q);
//System.out.println(c+" "+q+"  "+xx);
}

if(xx!=1){
if(!ha.keySet().contains(xx))ha.put(xx,1);
else
ha.put(xx,ha.get(xx)+1);
}
}
//System.out.println(ha);
int np = 0;
int so = 0;
for(int x:ha.keySet()){
np+=ha.get(x)%2;
ans+=(long)(ha.get(x)/2);
}
ans+=(long)np/3;
np%=3;
//if(np>ans)ans = 0;
sb.append(ans+"\n");
}
System.out.print(sb);
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
	
