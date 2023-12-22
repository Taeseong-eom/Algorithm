import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());//테스트 케이스 수

        for (int i = 0 ; i < num ; i++){
            String str = br.readLine();

            System.out.print(str.charAt(0));
            System.out.println(str.charAt(str.length()-1));
        }
    }
}