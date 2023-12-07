import java.util.List;
import java.util.Scanner;

public class Phonebook {
    private final DatabaseManager databaseManager;
    private final Scanner scanner;

    // Конструктор
    public Phonebook() {
        databaseManager = new DatabaseManager();
        scanner = new Scanner(System.in);
    }

    // Метод для добавления нового контакта
    public void addContact() {
        System.out.print("Введите имя: ");
        String firstName = scanner.nextLine();

        System.out.print("Введите фамилию: ");
        String lastName = scanner.nextLine();

        System.out.print("Введите номер телефона: ");
        String phoneNumber = scanner.nextLine();

        Contact contact = new Contact(firstName, lastName, phoneNumber);
        databaseManager.addContact(contact);

        System.out.println("Контакт добавлен!");
    }


    // Метод для поиска контактов по фамилии
    public void searchContactsByLastName() {
        System.out.print("Введите фамилию для поиска: ");
        String lastName = scanner.nextLine();

        List<Contact> contacts = databaseManager.searchContactsByLastName(lastName.toUpperCase());

        if (contacts.isEmpty()) {
            System.out.println("Контакты не найдены!");
        } else {
            System.out.println("Найденные контакты:");

            for (Contact contact : contacts) {
                System.out.println(contact);
            }
        }
    }

    // Метод для поиска контактов по номеру телефона
    public void searchContactsByPhoneNumber() {
        System.out.print("Введите номер телефона для поиска: ");
        String phoneNumber = scanner.nextLine();

        List<Contact> contacts = databaseManager.searchContactsByPhoneNumber(phoneNumber);

        if (contacts.isEmpty()) {
            System.out.println("Контакты не найдены!");
        } else {
            System.out.println("Найденные контакты:");

            for (Contact contact : contacts) {
                System.out.println(contact);
            }
        }
    }

    // Метод для выполнения операций с контактами
    public void run() {
        boolean exit = false;

        while (!exit) {
            System.out.println("Меню:");
            System.out.println("1. Добавить контакт");

            System.out.println("2. Поиск контактов по фамилии");
            System.out.println("3. Поиск контактов по номеру телефона");
            System.out.println("4. Выйти");

            System.out.print("Введите номер операции: ");
            int choice = scanner.nextInt();

            scanner.nextLine();

            switch (choice) {
                case 1:
                    addContact();
                    break;

                case 2:
                    searchContactsByLastName();
                    break;
                case 3:
                    searchContactsByPhoneNumber();
                    break;
                case 4:
                    exit = true;
                    break;
                default:
                    System.out.println("Недопустимый номер операции!");
            }

            System.out.println();
        }

        scanner.close();
    }

    // Метод main для запуска программы
    public static void main(String[] args) {
        Phonebook phonebook = new Phonebook();
        phonebook.run();
    }
}
