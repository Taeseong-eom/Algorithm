import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[]args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		String str1_1 = st.nextToken();
		String str2_1 = st.nextToken();

		StringBuilder str1_2 = new StringBuilder();
		StringBuilder str2_2 = new StringBuilder();


		for (int i = 2 ; i > -1 ; i--){
			str1_2.append(String.valueOf(str1_1.charAt(i)));
		}

		for (int i = 2 ; i > -1 ; i--){
			str2_2.append(String.valueOf(str2_1.charAt(i)));
		}
		if (Integer.parseInt(String.valueOf(str1_2)) > Integer.parseInt(String.valueOf(str2_2))){
			System.out.println(Integer.parseInt(String.valueOf(str1_2)));
		}else {
			System.out.println(Integer.parseInt(String.valueOf(str2_2)));
		}

	}
}