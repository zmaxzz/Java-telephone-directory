import java.util.Scanner;
public class PhoneBookApplication {
    public static void main(String[] args) {

        PhoneBook phoneBook = new PhoneBook();
        Scanner in = new Scanner(System.in);
        Person johnDoe = new Person("John", "Doe");
        johnDoe.addPhoneNumber("123456789");
        johnDoe.addPhoneNumber("987654321");

        phoneBook.addContact(johnDoe);

        Person janeSmith = new Person("Jane", "Smith");
        janeSmith.addPhoneNumber("987654321");
        phoneBook.addContact(janeSmith);

        Person jamesJane = new Person("James","Jane");
        jamesJane.addPhoneNumber("123451234");
        phoneBook.addContact(jamesJane);

        String input = in.nextLine();


        if (phoneBook.searchByLastName(input)) {
            phoneBook.searchByLastName(input);
        } else {
            phoneBook.searchByPhoneNumber(input);
        }



    }
}