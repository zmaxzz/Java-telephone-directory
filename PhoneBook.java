import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
class PhoneBook {
    private final List<Person> contacts;

    public PhoneBook() {
        contacts = new ArrayList<>();
        System.out.print("Введите номер или фамилию обьекта:");
    }

    public void addContact(Person person) {
        contacts.add(person);
        Collections.sort(contacts, (p1, p2) -> {
            int lastNameComparison = p1.getLastName().compareTo(p2.getLastName());
            if (lastNameComparison == 0) {
                return p1.getFirstName().compareTo(p2.getFirstName());
            } else {
                return lastNameComparison;
            }
        });

    }


    public boolean searchByLastName(String lastName) {
        for (Person person : contacts) {
            if (person.getLastName().equals(lastName)) {
                System.out.println(person.getFirstName() + " " + person.getLastName());
                System.out.println("Номера телефонов:");

                for (String phoneNumber : person.getPhoneNumbers()) {
                    System.out.println(phoneNumber);
                }
                return false;
            }
        }

        return false;
    }

    public void searchByPhoneNumber(String phoneNumber) {

        for (Person person : contacts) {
            if (person.getPhoneNumbers().contains(phoneNumber)) {
                System.out.println(person.getFirstName() + " " + person.getLastName());
                System.out.println("Номера телефонов:");
                for (String phone : person.getPhoneNumbers()) {
                    System.out.println(phone);
                }
                return;
            }
        }

    }



}
