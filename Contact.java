public class Contact {
    private final String firstName;
    private final String lastName;
    private final String phoneNumber;

    // Конструктор
    public Contact(String firstName, String lastName, String phoneNumber) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.phoneNumber = phoneNumber;
    }

    // Методы доступа к полям
    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    // Переопределение метода toString() для вывода контакта
    @Override
    public String toString() {
        return firstName + " " + lastName + " - " + phoneNumber;
    }
}




}
