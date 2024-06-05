import java.util.Scanner;
public class LeapYear {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            if ((n % 4 == 0 && n % 100 != 0) || n % 400 == 0) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }
    }
}