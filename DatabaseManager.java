import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class DatabaseManager {
    private Connection connection;

    // Конструктор
    public DatabaseManager() {
        // Подключение к базе данных
        try {
            connection= DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/phone", "root123", "root123");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Метод для добавления контакта в базу данных
    public void addContact(Contact contact) {
        try (PreparedStatement statement = connection.prepareStatement(
                "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (?, ?, ?)")) {
            statement.setString(1, contact.getFirstName());
            statement.setString(2, contact.getLastName());
            statement.setString(3, contact.getPhoneNumber());

            statement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }


    // Метод для поиска контактов по фамилии в базе данных
    public List<Contact> searchContactsByLastName(String lastName) {
        List<Contact> contacts = new ArrayList<>();

        try (PreparedStatement statement = connection.prepareStatement(
                "SELECT  *  FROM contacts WHERE last_name = ? ORDER BY last_name ASC, first_name ASC")) {
            statement.setString(1, lastName);

            ResultSet resultSet = statement.executeQuery();

            while (resultSet.next()) {
                Contact contact = new Contact(resultSet.getString("first_name"), resultSet.getString("last_name"), resultSet.getString("phone_number"));
                contacts.add(contact);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return contacts;
    }
    private void insertContact(Contact contact) {
        try (PreparedStatement statement = connection.prepareStatement("INSERT INTO contacts (first_name, last_name, phone_number) VALUES (?, ?, ?)")) {
            statement.setString(1, contact.getFirstName());
            statement.setString(2, contact.getLastName());
            statement.setString(3, contact.getPhoneNumber());

            statement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Метод для поиска контактов по номеру телефона в базе данных
    public List<Contact> searchContactsByPhoneNumber(String phoneNumber) {
        List<Contact> contacts = new ArrayList<>();

        try (PreparedStatement statement = connection.prepareStatement(
                "SELECT * FROM contacts WHERE phone_number = ? ORDER BY last_name ASC, first_name ASC")) {
            statement.setString(1, phoneNumber);

            ResultSet resultSet = statement.executeQuery();

            while (resultSet.next()) {
                Contact contact = new Contact(resultSet.getString("first_name"), resultSet.getString("last_name"), resultSet.getString("phone_number"));
                contacts.add(contact);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return contacts;
    }
}
