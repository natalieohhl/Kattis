import java.util.*;

public class Main {
    
    static Scanner keyboard = new Scanner(System.in);
    
    
    public static void main(String[] args) {
        
    //declare and initialize working storage
    String name;
    int count=0;
    name = keyboard.nextLine();

    if (name.equals("Later!")){
    System.out.print("Alligator!");
    }
      else{

        for (int i = 1; i < name.length(); i++) {
            if (name.charAt(i) == 'e') {
                count++;
            }
        }
        
        System.out.print('h');
        for (int j=0; j<count*2; j++){
        System.out.print("e");}
        System.out.print("y");

      }
    }
}
