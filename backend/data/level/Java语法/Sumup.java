import java.util.Scanner;
public class Sumup {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            int n = sc.nextInt();
            System.out.println((n + 1) * n / 2);
        }
    }
}