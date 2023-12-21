import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[]args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine()); //과목개수
		Double arr[] = new Double[num];
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		for (int i = 0 ; i < num ; i++){
			arr[i] = Double.parseDouble(st.nextToken());
		}
		double sum = 0;
		Arrays.sort(arr);// 오름차순 정렬
		for(int i = 0 ; i < num ; i++){
			arr[i] = (arr[i]/arr[num-1])*100;
			sum = sum + arr[i];
		}
		System.out.println(sum/num);

	}
}
