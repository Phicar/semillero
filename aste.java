import java.util.*;
import java.io.*;
public class aste{
public static void main(String args[]) throws IOException{
BufferedReader le = new BufferedReader(new InputStreamReader(System.in));
int aa = Integer.parseInt(le.readLine());
StringBuilder sb = new StringBuilder("");
for(int cc = 0;cc<aa;cc++){
String a = le.readLine();
int la = a.length();
String b = le.readLine();
int lb = b.length();
if(a.charAt(0)==b.charAt(0)){
sb.append("YES\n");
sb.append(a.charAt(0)+"*\n");
continue;
}else if(a.charAt(la-1)==b.charAt(lb-1)){
sb.append("YES\n");
sb.append("*"+a.charAt(la-1)+"\n");
continue;
}
boolean si = false;
for(int i = 0;!si && i<la-1;i++){
for(int j = 0;!si && j<lb-1;j++){
if(a.charAt(i)==b.charAt(j) && a.charAt(i+1)==b.charAt(j+1)){
si = true;
sb.append("YES\n");
sb.append("*"+a.substring(i,i+2)+"*\n");
break;
}
}
}
if(!si)sb.append("NO\n");
}
System.out.print(sb);
}
}
