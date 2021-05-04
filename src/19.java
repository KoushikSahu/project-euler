import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;
 
class Main{

    static FastScanner fs=new FastScanner();
        
    public static void main(String[] args){
        GregorianCalendar cal = new GregorianCalendar(1901, 0, 1);
        int ans = 0;
        while(cal.get(Calendar.YEAR)!=2001 || cal.get(Calendar.MONTH)!=0 || cal.get(Calendar.DAY_OF_MONTH)!=1){
            int day_of_week = cal.get(Calendar.DAY_OF_WEEK);
            int day_of_month = cal.get(Calendar.DAY_OF_MONTH);
            if(day_of_week==1 && day_of_month==1) ans++;
            cal.add(Calendar.DAY_OF_MONTH, 1);
        }
        System.out.println(ans);
    }
        
    static class FastScanner {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer("");
                            
        public String next() {
            while (!st.hasMoreTokens())
                try {
                    st=new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            return st.nextToken();
        }

        public String nextLine(){
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
                                        
        public int nextInt() {
            return Integer.parseInt(next());
        }
                                                
        public int[] readArray(int n) {
            int[] a=new int[n];
            for (int i=0; i<n; i++) a[i]=nextInt();
            return a;
        }
                                                        
        public long nextLong() {
            return Long.parseLong(next());
        }
                                                                
        public long[] readLongArray(int n) {
            long[] a=new long[n];
            for (int i=0; i<n; i++) a[i]=nextLong();
            return a;
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }
    }
     
}