import java.util.*;
import java.io.*;
import java.math.BigDecimal;
public class fract{
public static void main(String args[]) throws IOException{
BufferedReader lector = new BufferedReader(new InputStreamReader(System.in));
String s[] = lector.readLine().split(" ");
BigDecimal a = new BigDecimal(s[0]).divide(new BigDecimal(s[1]),1001,BigDecimal.ROUND_HALF_UP);
String aa = String.valueOf(a);
aa = aa.substring(0,aa.length()-1);
int pun = aa.indexOf(".");
if(aa.indexOf(s[2],pun+1)==-1)
System.out.println("-1");
else
System.out.println(aa.indexOf(s[2],pun+1)-pun);
}
}
