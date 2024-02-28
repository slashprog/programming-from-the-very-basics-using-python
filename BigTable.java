import java.math.*;

public class BigTable {
    public static void main(String[] args) {
        System.out.print("Enter a number: ");
        String input = System.console().readLine();
        BigInteger num = new BigInteger(input);

        for (int count=1; count<=10; count++) {
            BigInteger result = 
                  num.multiply(new BigInteger(Integer.toString(count)));
            System.out.print(num.toString());
            System.out.print(" x ");
            System.out.print(count);
            System.out.print(" = ");
            System.out.print(result.toString());
            System.out.print("\n");
        }
    }
}
