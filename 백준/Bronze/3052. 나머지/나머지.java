import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[]args) throws IOException {
		/*BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while ((str=br.readLine()) != null){
		int a = Integer.parseInt(str);
		 */
		boolean arr[] = new boolean[42]; // 기본적으로 false로 설정되어 있음.
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		for (int i = 0 ; i < 10 ; i++){
			arr[(Integer.parseInt(br.readLine())) % 42] = true;
		}
		int count = 0;
		for (int i = 0 ; i < 42 ; i++){
			if(arr[i] == true){
				count++;
			}
		}
		System.out.print(count);



	}
}
