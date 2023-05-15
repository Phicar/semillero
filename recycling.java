import java.io.*;
import java.util.*;
public class recycling{
public static void main(String args[]) throws IOException{
BufferedReader lector = new BufferedReader(new InputStreamReader(System.in));
int a = Intger.parseInt(lector.readLine());
int tal[] = new int[a];
String s = "";
int ind = 0
while((s = lector.readLine())!=null){
String ss[] = s.split(" ");
for(int n = 0;n<ss.length();n++)
tal[ind++]=Integer.parseInt(ss[n]);
}
int min = Integer.MAX_VALUE;
int mins = new int[a];
Vector<Integer> mi = new Vector<Integer>();
Vector<Integer> emp = new Vector<Integer>();
Vector<Integer>  = new Vector<Integer>();
int emp = -1;
int term = -1;
for(int n = 0;n<a;n++){
if(tal[n]<min){
min = tal[n];

}
mins[n]=min;

}
}
}


