import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;
 
class Main{

    static FastScanner fs=new FastScanner();
        
    public static void main(String[] args){
        Node[][] a = new Node[15][15];
        for(int i=0; i<15; i++){
            for(int j=0; j<=i; j++){
                a[i][j] = new Node(fs.nextInt());
            }
            for(int j=i+1; j<15; j++){
                a[i][j] = null;
            }
        }
        for(int i=0; i<14; i++){
            for(int j=0; j<=i; j++){
                a[i][j].left = a[i+1][j];
                a[i][j].right = a[i+1][j+1];
            }
        }
        System.out.println(solve(a[0][0]));
    }

    static int max(int a, int b){
        return (a>b) ? a : b;
    }

    static int solve(Node root){
        if(root==null) return 0;
        int l = solve(root.left);
        int r = solve(root.right);
        return max(0, root.data+max(l, r));
    }

    static class Node{
        int data;
        Node left, right;
        Node(int x){
            this.data = x;
            this.left = this.right = null;
        }
    };
        
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