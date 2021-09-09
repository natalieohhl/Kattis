import java.util.Scanner;

public class Main {
    
    static Scanner keyboard = new Scanner(System.in);
    public static void main(String[] args) {
        
    //declare and initialize working storage
    String word;

    word = keyboard.nextLine();

        for (int i = 0; i <2; i++) {
            System.out.print(word+ " ");
        }
        System.out.print(word);
    }
}
