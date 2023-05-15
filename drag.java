import java.util.*;
import java.io.*;
public class drag{
public static void main(String args[]) throws IOException{
BufferedReader lector = new BufferedReader(new InputStreamReader(System.in));
int aa = Integer.parseInt(lector.readLine());
StringBuilder sb = new StringBuilder("");
for(int ccc = 0;ccc<aa;ccc++){
String bb[]= lector.readLine().split(" ");
int nn = (int)Long.parseLong(bb[0]);
long hh = Long.parseLong(bb[1]);
bb= lector.readLine().split(" ");
long cc[] = new long[nn];
for(int i = 0;i<nn;i++)cc[i]=Long.parseLong(bb[i]);
long mini = 1;
long maxi = hh+1;
long la = -1;
while(mini<=maxi){
long mm = (mini+maxi)/2;
long hhh = mm;
for(int i = 0;i<nn-1;i++)hhh+=(long)Math.min(mm,cc[i+1]-cc[i]);
if(hhh<hh)mini=mm+1;
else{
la = mm;
maxi= mm-1;
}
}
sb.append(la+"\n");
}
System.out.print(sb);
}
}
