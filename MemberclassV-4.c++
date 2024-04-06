#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <unordered_map>
#include <limits>
#include <iterator>
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

   vector<string> searchbyName(unordered_map<string, Member>& hashtable,string&key) {
    vector<string>identity(3);
    auto it = hashtable.find(key);
    if (it != hashtable.end()) {
        cout << "Member found!" << endl;
        cout << "Name: " << it->second.name << endl;
        cout << "ID: " << it->second.id << endl;
        cout << "Club: " << it->second.club << endl;
        identity[0]=it->second.name;
        identity[1]=it->second.id;
        identity[2]=it->second.club;
    } else {
        cout << "Member not found :(" << endl;
    }
    return identity;
}

vector<string> searchbyID(unordered_map<string, Member>& hashtable,string&key) {
    vector<string>id(3);
    auto it = hashtable.find(key);
    if (it != hashtable.end()) {
        cout << "Member found!" << endl;
        cout << "Name: " << it->second.name << endl;
        cout << "ID: " << it->second.id << endl;
        cout << "Club: " << it->second.club << endl;
        id[0]=it->second.name;
        id[1]=it->second.id;
        id[2]=it->second.club;
    } else {
        cout << "Member not found :(" << endl;
    }
    return id;
}
void search(unordered_map<string,Member>namet,unordered_map<string,Member>idt){
    cin.ignore(numeric_limits<streamsize>::max(),'\n');
    string key;
    cout<<"Enter identity of the member(name or id): ";

    getline(cin,key);

   
    if(key[0]>='2' && key[0]<='9') searchbyID(idt,key);
    else searchbyName(namet,key);
    return;
}
    void deleteMemberRequest(string memberName) {

        ifstream inFile("Requests.csv");
        ofstream tempFile("temp.csv");
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
            remove("Requests.csv");
            rename("temp.csv", "Requests.csv");
        } else {
            cerr << "Failed to open CSV file." << endl;
        }
       
        return;
    }

   void sendRequests() {

        cin.ignore(numeric_limits<streamsize>::max(),'\n');
        cout << "Enter name of the member: ";
        getline(cin, name);

        cout << "Enter ID of the member: ";
        getline(cin, id);
        cout << "Enter club of the member: ";
        getline(cin, club);

        
       ofstream file("Requests.csv",ios::app);
        if (!file.is_open()) {
            cerr << "Failed to open CSV file." << endl;
            return;
        }

       
        file << name << "," << id <<","<<club<<endl;
        file.close();

        cout << "Request sent successfully." <<endl;
    }

void deleteMemberByName(string memberName) {
        
        ifstream inFile("Records.csv");
        ofstream tempFile("temp.csv");
        
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
        } else {
            cerr << "Failed to open CSV file." << endl;
        }
        return;
    }
void replaceMember(const string& memberName, const string& newID, const string& newClub) {
    ifstream inFile("Records.csv");
    ofstream tempFile("temp.csv");

    if (inFile.is_open() && tempFile.is_open()) {
        string line;
        while (getline(inFile, line)) {
            istringstream iss(line);
            string name, id, club;
            getline(iss, name, ',');
            getline(iss, id, ',');
            getline(iss, club);

            if (name == memberName) {
                tempFile << memberName << "," << newID << "," << newClub << endl;
            } else {
                tempFile << line << endl;
            }
        }
        inFile.close();
        tempFile.close();

        remove("Records.csv");
        rename("temp.csv", "Records.csv");
    } else {
        cerr << "Failed to open CSV file." << endl;
    }
}

void acceptRequests(unordered_map<string, Member>& nametable) {
    ifstream requestFile("Requests.csv");
    if (!requestFile.is_open()) {
        cerr << "Failed to open Requests file." << endl;
        return;
    }

    string name, id, club;
    getline(requestFile, name, ',');
    string key = name;
    getline(requestFile, id, ',');
    getline(requestFile, club);
    string club2 = club;
    requestFile.close();

    cout << "Showing the earliest sent request:" << endl;
    cout << "Member Name: " << name << endl;
    cout << "Member ID: " << id << endl;
    cout << "Member Club: " << club << endl;

    string ans;
    cout << "Do you want to accept the request? ";
    cin >> ans;

    if (ans == "Yes" || ans == "yes") {
        string password;
        cout << "Enter password to accept the request: ";
        cin >> password;
        string expectedPassword= club+"123";
        if (password != expectedPassword) {
            cout << "Incorrect password. Request not accepted." << endl;
            return;
        }

        auto it = nametable.find(key);
        if (it != nametable.end()) {
            string name1 = it->second.name;
            string id1 = it->second.id;
            string club1 = it->second.club += "/" + club2;
            
            replaceMember(name1, id1, club1);
        } else {
            ofstream recordsFile("Records.csv", ios::app);
            if (!recordsFile.is_open()) {
                cerr << "Failed to open Records file." << endl;
                return;
            }
            recordsFile << name << "," << id << "," << club << endl;
            recordsFile.close();
        }

        deleteMemberRequest(name);
        cout << "Request accepted successfully." << endl;
    } else {
        cout << "Sorry your request has been rejected :(" << endl;
        deleteMemberRequest(name);
    }
}


    vector<string> readName(const string& filename) {
    vector<string> names;
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Failed to open file: " << filename << endl;
        return names; 
    }

    string line;
    
    while (getline(file, line)) {
        stringstream ss(line);
        string name, id, club;
        if (getline(ss, name, ',')) { 
            names.push_back(name);
        } else {
            cerr << "Error: Unable to read name from line: " << line << endl;
            
        }
    }

    file.close();
    return names;
}
vector<string> readId(const string& filename) {
    vector<string> ids;
    ifstream file(filename);
    //edge case if the file is empty
    if (!file.is_open()) {
        cerr << "Failed to open file: " << filename << endl;
        return ids; 
    }

     string line;
    
    while (getline(file, line)) {
        stringstream ss(line);
        string name, id, club;
        getline(ss, name, ',');
        getline(ss, id, ',');
        ids.push_back(id);
    }


    file.close();
    return ids;
}
vector<string> readClub(const string& filename) {
   vector<string> clubs;
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Failed to open file: " << filename << endl;
        return clubs;
    }

    string line;
    
    while (getline(file, line)) {
        stringstream ss(line);
        string name, id, club;
        getline(ss, name, ',');
        getline(ss, id, ',');
        getline(ss, club);
        clubs.push_back(club);
    }

    file.close();
    return clubs;
}
};

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

vector<string> returnKey(unordered_map<string,Member>&hashtable){
    vector<string> v;
    for(const auto& pair: hashtable){
        v.push_back(pair.first);
    }
    return v;
}
