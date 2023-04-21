import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] dp = new int[n][3];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 3; j++) {
                dp[i][j] = sc.nextInt();
            }
        }
        for (int i = 1; i < n; i++) {
            dp[i][0] = Math.min(dp[i][0] + dp[i-1][1], dp[i][0] + dp[i-1][2]);
            dp[i][1] = Math.min(dp[i][1] + dp[i - 1][0], dp[i][1] + dp[i - 1][2]);
            dp[i][2] = Math.min(dp[i][2] + dp[i - 1][0], dp[i][2] + dp[i - 1][1]);
        }
        System.out.println(Math.min(Math.min(dp[n-1][0], dp[n-1][1]), dp[n-1][2]));
    }
}

