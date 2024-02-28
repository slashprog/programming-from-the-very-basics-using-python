import java.util.Scanner;

class Table {
    public static void main(String[] args) {
        int num;
        Scanner in;

        System.out.print("Enter a number: ");
        in = new Scanner(System.in);
        num = in.nextInt();
        
        for (int i=1; i<=10; i++) {
            System.out.printf("%d x %d = %d\n", num, i, num*i);
        }
    }
}

