import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.*;

/**
 * Created by Alejandro on 2016/07/26.
 */
public class MaxPair {
   static Long getTheMaximumPairwise(int[] numbers){
       Long result = Long.valueOf(0);
       int n = numbers.length;
       System.out.println("Arrayth: " + numbers.length);

       for(int i = 0; i < n; ++i){
           System.out.println("iteration" +i);

           for(int j = i + 1; j < n; ++j){
               System.out.println("i: " + i);
               System.out.println("iteration" + j);
             if(Long.valueOf(numbers[i]) * numbers[j] > result){
                 System.out.println("resulsor: " + result + " i : " + i + " j : " + j + " number[i]: " + numbers[i] + " number[j]: " + numbers[j]);
                 result = Long.valueOf(numbers[i]) * numbers[j];
                 System.out.println("printresult: " + result);
             }
           }
       }
   return result;
}
public static void main(String[]args){
    FastScanner scanner = new FastScanner(System.in);
    int n = scanner.nextInt();
    int[] numbers = new int[n];   // I create the array I passed to the method
    for(int i=0; i<n; i++){
        numbers[i] = scanner.nextInt();  //I create the array that receive the numbers
    }
    System.out.println(Long.valueOf(getTheMaximumPairwise(numbers)));  //I call the method inside a system.out.println
}
    static class FastScanner{
        BufferedReader br;
        StringTokenizer st;

        FastScanner(InputStream stream){
            try{
                br = new BufferedReader(new InputStreamReader(stream));
            } catch(Exception e) {
                e.printStackTrace();
            }
        }
        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }

}