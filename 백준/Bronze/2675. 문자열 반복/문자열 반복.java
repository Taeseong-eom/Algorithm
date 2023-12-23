import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[]args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input;
		while ((input = br.readLine()) != null && !(input.isEmpty())){
			StringTokenizer st = new StringTokenizer(input, " ");
			if(st.countTokens()!=2){
				continue;
			}
			int num = Integer.parseInt(st.nextToken());
			String sum = "";

			String str = st.nextToken();

			for(int i =0; i < str.length() ; i++){
				for (int j = 0 ; j < num ; j++){
					sum = sum + str.charAt(i);
				}
			}
			System.out.println(sum);

		}


	}
}
