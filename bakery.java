import java.util.*;
import java.io.*;
public class bakery{
public static int atoi(String x){
return Integer.parseInt(x);
}
public static void main(String args[]) throws IOException{
BufferedReader lector = new BufferedReader(new InputStreamReader(System.in));
long res =-1;
String aa[]= lector.readLine().split(" ");
String L[] = new String[atoi(aa[1])];
for(int n = 0;n<L.length;n++)
L[n]=lector.readLine();
Vector<Integer> tal = new Vector<Integer>();
boolean fin[] = new boolean[atoi(aa[0])];
String bb[];
if(atoi(aa[2])>0){
bb = lector.readLine().split(" ");
for(int n = 0;n<bb.length;n++){
tal.add(atoi(bb[n]));
fin[atoi(bb[n])-1]=true;
}
}
long mini[] = new long[atoi(aa[0])];
Arrays.fill(mini,Long.MAX_VALUE);
for(int n = 0;n<L.length;n++){
String ll[] = L[n].split(" ");
int a1 = atoi(ll[0]);
int a2 = atoi(ll[1]);
long a3 = Long.parseLong(ll[2]);
if(fin[a1-1]^fin[a2-1]){
mini[a1-1]=(a3<mini[a1-1]?a3:mini[a1-1]);
mini[a2-1]=(a3<mini[a2-1]?a3:mini[a2-1]);
}
}
for(int n = 0;n<tal.size();n++)
if((mini[tal.get(n)-1]<Long.MAX_VALUE && res==-1) || mini[tal.get(n)-1]<res)
res = mini[tal.get(n)-1];
System.out.println(res);
}
}
