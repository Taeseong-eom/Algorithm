import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[]args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		int[] arr = new int[26];
		for (int i = 0 ; i < 26; i++){
			arr[i] = -1;
		}
		for (int i = 0 ; i < str.length(); i++){
			// 97 = a
			if(str.charAt(i)>=97&str.charAt(i)<=122&arr[(str.charAt(i)-97)]==-1){
				arr[str.charAt(i) - 97] = i;
			}
		}
		for (int i = 0 ; i < 26;i++){
			System.out.print(arr[i] + " ");
		}
	}
}
