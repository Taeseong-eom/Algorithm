import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] arr = new char[1000];

        String str = br.readLine();
        for (int i =0 ; str.length() > i ; i++){
            arr[i] = str.charAt(i);
        }
        int num = Integer.parseInt(br.readLine());
        System.out.print(arr[num-1]);
    }
}