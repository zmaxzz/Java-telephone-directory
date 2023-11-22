import java.util.*;

class Person {
    private final String firstName;
    private final String lastName;
    private final List<String> phoneNumbers;

    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.phoneNumbers = new ArrayList<>();
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public List<String> getPhoneNumbers() {
        return phoneNumbers;
    }

    public void addPhoneNumber(String phoneNumber) {
        if (phoneNumbers.size() < 3) {
            phoneNumbers.add(phoneNumber);
        } else {
            System.out.println("Невозможно добавить более 3 телефонных номеров.");
        }
    }






}
