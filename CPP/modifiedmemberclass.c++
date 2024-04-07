#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <unordered_map>
#include <limits>
using namespace std;

class Member {
public:
    string name;
    string id;
    string club;
    

    // Default constructor
    Member() : name(""), id(""), club("") {}

    // Parameterized constructor
    Member(const string& name, const string& id, const string& club)
        : name(name), id(id), club(club) {}

unordered_map<string, Member> buildHashTable(const string& myfile, const string& key) {
    ifstream file(myfile);
    unordered_map<string, Member> hashtable;

    if (!file.is_open()) {
        cout << "File doesn't exist" << endl;
        return hashtable;
    }

    string line;
    while (getline(file, line)) {
        istringstream iss(line);
        string name, id, club;

        getline(iss, name, ',');
        getline(iss, id, ',');
        getline(iss, club);

        Member student{name, id, club};
        string k = (key == "id") ? id : (key == "club") ? club : name;

        hashtable[k] = student;
    }

    file.close();
    return hashtable;
}
void printHashTable(const unordered_map<string, Member>& hashtable) {
    for (const auto& pair : hashtable) {
        cout << "Key: " << pair.first 
             << " | Name: " << pair.second.name 
             << ", ID: " << pair.second.id 
             << ", Club: " << pair.second.club << endl;
    }
}

    unordered_map<string,Member>nametable=buildHashTable("C:\\Users\\DELL\\Desktop\\C++_files\\Records.csv","name");
    unordered_map<string,Member>idtable=buildHashTable("C:\\Users\\DELL\\Desktop\\C++_files\\Records.csv","id");
   void searchbyName() {
    //input buffer ko clear karne kelie and press enter to input
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string key;
    cout << "Enter name of the member: ";
    getline(cin, key); //getline so that spaces in the name can be ignored
   
    auto it = nametable.find(key);
    if (it != nametable.end()) {
        cout << "Member found!" << endl;
        cout << "Name: " << it->second.name << endl;
        cout << "ID: " << it->second.id << endl;
        cout << "Club: " << it->second.club << endl;
    } else {
        cout << "Member not found :(" << endl;
    }
}
void searchbyID() {
   
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string key;
    cout << "Enter id of the member: ";
    getline(cin, key); 
    
    auto it = idtable.find(key);
    if (it != idtable.end()) {
        cout << "Member found!" << endl;
        cout << "Name: " << it->second.name << endl;
        cout << "ID: " << it->second.id << endl;
        cout << "Club: " << it->second.club << endl;
    } else {
        cout << "Member not found :(" << endl;
    }
}

    // Delete member function
    void deleteMemberByName() {
        string password;
        cout << "Enter password (consists of six digits): ";
        cin >> password;
        if (password != "123456") {
            cout << "Incorrect password. Access denied." << endl;
            return;
        }

        ifstream inFile("Records.csv");
        ofstream tempFile("temp.csv");
        string memberName;
        cout << "Enter the name of the member to be deleted: ";
        cin >> memberName;
        if (inFile.is_open() && tempFile.is_open()) {
            string line;
            while (getline(inFile, line)) {
                istringstream iss(line);
                string n, i, c;
                getline(iss, n, ',');
                getline(iss, i, ',');
                getline(iss, c);
                // Check if the name contains the memberName as a substring
                if (n.find(memberName) == string::npos) {
                    tempFile << line << endl;
                }
            }
            inFile.close();
            tempFile.close();
            remove("Records.csv");
            rename("temp.csv", "Records.csv");
            cout << "Member deleted successfully." << endl;
        } else {
            cerr << "Failed to open CSV file." << endl;
        }
        cout<<"Member deleted successfully"<<endl;
        return;
    }

    // Insert member function
   void insert() {
        
        string password;
        cout << "Enter password (consists of 6 digits): ";
        cin >> password;


        if (password != "123456") {
            cout << "Incorrect password. Access denied." << endl;
            return;
        }

        
        cout << "Enter name of the member: ";
        cin.ignore(); 
        getline(cin, name);
        cout << "Enter ID of the member: ";
        getline(cin, id);
        cout << "Enter club of the member: ";
        getline(cin, club);

        
       ofstream file("Records.csv",ios::app);
        if (!file.is_open()) {
            cerr << "Failed to open CSV file." << endl;
            return;
        }

       
        file << name << "," << id <<","<<club<<endl;
        file.close();

        cout << "Member added successfully." <<endl;
    }

    friend void printHashTable(const unordered_map<string, Member>& hashtable);

};

vector<string> returnKey(unordered_map<string,Member>&hashtable){
    vector<string> v;
    for(const auto& pair: hashtable){
        v.push_back(pair.first);
    }
    return v;
}

int main()
{
    Member M1;
    

    printHashTable(M1.nametable);
}
