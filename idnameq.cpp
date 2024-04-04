#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <unordered_map>
#include <limits>
#include <vector>

using namespace std;

class Member {
private:
    string id;
    string name;
    string clubName;

public:
    // Constructor
    Member(const string& id, const string& name, const string& clubName) : id(id), name(name), clubName(clubName) {}

    // Default constructor
    Member() : id(""), name(""), clubName("") {}

    // Getter for ID
    string getId() const {
        return id;
    }

    // Getter for name
    string getName() const {
        return name;
    }

    // Getter for club name
    string getClubName() const {
        return clubName;
    }
};

class Database {
private:
    unordered_map<string, Member> nameHashTable; // Hash table to store members using name as key
    unordered_map<string, Member> idHashTable;   // Hash table to store members using ID as key

public:
    // Function to search for a member by name
    Member searchMemberByName(const string& name) {
        auto it = nameHashTable.find(name);
        if (it != nameHashTable.end()) {
            return it->second; // Return the member if found
        }
        return Member(); // Return default member if not found
    }

    // Function to search for a member by ID
    Member searchMemberByID(const string& id) {
        auto it = idHashTable.find(id);
        if (it != idHashTable.end()) {
            return it->second; // Return the member if found
        }
        return Member(); // Return default member if not found
    }

    // Function to add a member to the database
    void addMember(const string& id, const string& name, const string& clubName) {
        Member newMember(id, name, clubName);
        nameHashTable.emplace(name, newMember); // Use name as key
        idHashTable.emplace(id, newMember);     // Use ID as key
    }

    // Function to populate the database from a CSV file
    void populateFromCSV(const string& filename) {
        ifstream file(filename);
        if (!file.is_open()) {
            cerr << "Error: Unable to open file " << filename << endl;
            return;
        }

        string line;
        while (getline(file, line)) {
            stringstream ss(line);
            string name, id, clubName;
            if (getline(ss, name, ',') && getline(ss, id, ',') && getline(ss, clubName)) {
                addMember(id, name, clubName); // Pass id, name, clubName to addMember function
            } else {
                cerr << "Error: Invalid line in CSV file." << endl;
            }
        }

        file.close();
    }
};

void clear() {
    cout << "\033[2J\033[H";  // ANSI escape code to clear screen
}

void members(int c) {
    clear();
    vector<string> s{ "1.Search by Name", "2.Search by ID", "3.Add", "4.Delete","5.Back to Menu" };

    for (int i = 0; i < 5; ++i) {
        if (c == i + 1) {
            cout << "\033[47m";
            cout << s[i] << endl;
            cout << "\033[0m";
        }
        else {
            cout << s[i] << endl;
        }
    }
}

void menu(int c) {
    clear();
    vector<string> s{ "1.Members", "2.Clubs", "3.Exit" };

    for (int i = 0; i < 3; ++i) {
        if (c == i + 1) {
            cout << "\033[47m";
            cout << s[i] << endl;
            cout << "\033[0m";
        }
        else {
            cout << s[i] << endl;
        }
    }
}

int main() {
    int i = 1;
    int j = 1;
    menu(i);
    Database db;
    db.populateFromCSV("test102.csv");

    string input; // Modified variable name

    while (1) {
        char ch;
        cin >> ch;

        switch (ch) {
        case 'w':
            if (i != 1) {
                i--;
                menu(i);
            }
            break;
        case 's':
            if (i != 3) {
                i++;
                menu(i);
            }
            break;
        case 'k':
            members(1);
            while (1) {
                char ch;
                cin >> ch;

                switch (ch) {
                case 'w':
                    if (j != 1) {
                        j--;
                        members(j);
                    }
                    break;
                case 's':
                    if (j != 5) {
                        j++;
                        members(j);
                    }
                    break;
                case 'k':
                    clear();

                    if (j == 1) {
                        cout << "Enter Name to search: ";
                    } else if (j == 2) {
                        cout << "Enter ID to search: ";
                    }
                    cin >> input; // Moved the input statement here

                    {
                        Member result;
                        if (j == 1) {
                            result = db.searchMemberByName(input); // Changed the function call
                        } else if (j == 2) {
                            result = db.searchMemberByID(input); // Changed the function call
                        }

                        if (result.getId() != "") {
                            cout << "Name: " << result.getName() << endl;
                            cout << "ID: " << result.getId() << endl;
                            cout << "Club Name: " << result.getClubName() << endl;
                        } else {
                            if (j == 1) {
                                cout << "Name not found in the database." << endl;
                            } else if (j == 2) {
                                cout << "ID not found in the database." << endl;
                            }
                        }
                    }
                    break;
                case 'q':
                    menu(1);
                    break;
                default:
                    break;
                }
                if (ch == 'q') // Break the inner loop when 'q' is pressed
                    break;
            }
            break; // Added break statement here
        case 'q':
            exit(1);
            break; // Added break statement here
        default:
            break;
        }
    }

    return 0;
}
