import java.util.*;
import java.io.*;
public class freedom{
public static void main(String args[]) throws IOException{
BufferedReader lector = new BufferedReader(new InputStreamReader(System.in));
StringBuffer sb = new StringBuffer("");
//Vector<p> nose = new Vector<p>();
int a = Integer.parseInt(lector.readLine());
for(int nn = 0;nn<a;nn++){
String aa[] = lector.readLine().split(" ");
boolean ans = true;
int ar = Integer.parseInt(aa[0]);
int br = Integer.parseInt(aa[1]);
for(int k = 2;k<=(int)Math.sqrt((double)ar)+1;k++){
if(k>br || k>ar)break;
int vec = ar/k;
if(ar%k==0 && ((vec==1 && ar==k) ||(br-k)*(vec-1)>=(ar-vec*k) )){
ans = false;
break;
}
}
if(br!=1 && ar%br==0)ans = false;
sb.append(ans?"YES\n":"NO\n");
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
	
