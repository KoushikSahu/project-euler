import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;
 
/*
    Author: Koushik Sahu
    Created: 08 September 2020 Tue 23:02:35
*/

class Problem31 {

    static FastScanner fs=new FastScanner();
        
    static int[] denomination = {200, 100, 50, 20, 10, 5, 2, 1};
    static long[][] dp = new long[201][201];
    static int n = 200;

    public static void main(String[] args){
        for(int i=0; i<201; i++){
            for(int j=0; j<201; j++){
                dp[i][j] = -1;
            }
        }
        long ans = solve(n, denomination.length);
        System.out.println(ans);
        // long[] dp = new long[201];
        // dp[0] = 1;
        // for(int i=0; i<denomination.length; i++){
        //     for(int j=1; j<=200; j++){
        //         if(j>=denomination[i]) dp[j] += dp[j-denomination[i]];
        //     }
        // }
        // System.out.println(dp[200]);
    }

    static long solve(int rem, int len){
        if(rem==0) return 1;
        if(len==0) return 0;
        if(dp[rem][len]!=-1) return dp[rem][len];
        long ans = 0;
        if(rem>=denomination[len-1]) ans += solve(rem, len-1)+solve(rem-denomination[len-1], len);
        return dp[rem][len] = ans;
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