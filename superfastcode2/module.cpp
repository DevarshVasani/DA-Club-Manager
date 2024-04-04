#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <unordered_map>
#include <limits>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include<pybind11/complex.h>
#include<pybind11/functional.h>

using namespace std;

class Member;

unordered_map<string, Member> buildHashTable(const string& myfile, const string& key);

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

    vector<string> searchbyName(string& key) {
        vector<string>identity(3);

        unordered_map<string, Member> hashtable = buildHashTable("D://capstone//Records.csv", "name");
        auto it = hashtable.find(key);
        if (it != hashtable.end()) {
            cout << "Member found!" << endl;
            cout << "Name: " << it->second.name << endl;
            cout << "ID: " << it->second.id << endl;
            cout << "Club: " << it->second.club << endl;
            identity[0] = it->second.name;
            identity[1] = it->second.id;
            identity[2] = it->second.club;
        }
        else {
            cout << "Member not found :(" << endl;
            
        }
        return identity;
    }

    vector<string> searchbyID(string key) {
        vector<string>id(3);

        unordered_map<string, Member> hashtable = buildHashTable("D://capstone//Records.csv", "id");
        auto it = hashtable.find(key);
        if (it != hashtable.end()) {
            cout << "Member found!" << endl;
            cout << "Name: " << it->second.name << endl;
            cout << "ID: " << it->second.id << endl;
            cout << "Club: " << it->second.club << endl;
            id[0] = it->second.name;
            id[1] = it->second.id;
            id[2] = it->second.club;
        }
        else {
            cout << "Member not found :(" << endl;
        }
        return id;
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

        ifstream inFile("D://capstone//Records.csv");
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
            remove("D://capstone//Records.csv");
            rename("temp.csv", "D://capstone//Records.csv");
            cout << "Member deleted successfully." << endl;
        }
        else {
            cerr << "Failed to open CSV file." << endl;
        }
        cout << "Member deleted successfully" << endl;
        return;
    }

    void acceptRequests(string name, string id, string club) {

        ifstream requestFile("D://capstone//Requests.csv");
        if (!requestFile.is_open()) {
            cerr << "Failed to open Requests file." << endl;
            return;
        }

        //getline(requestFile, name, ',');
        //getline(requestFile, id, ',');
        //getline(requestFile, club);

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
            if (password != "123456") {
                cout << "Incorrect password. Request not accepted." << endl;
                return;
            }

            ofstream recordsFile("D://capstone//Records.csv", ios::app);
            if (!recordsFile.is_open()) {
                cerr << "Failed to open Records file." << endl;
                return;
            }

            recordsFile << name << "," << id << "," << club << endl;

            recordsFile.close();

            //deleteMemberRequest(name);
            cout << "Request accepted successfully." << endl;
        }
        else {
            cout << "Sorry your request has been rejected :(" << endl;
            //deleteMemberRequest(name);
        }
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


        ofstream file("D://capstone//Records.csv", ios::app);
        if (!file.is_open()) {
            cerr << "Failed to open CSV file." << endl;
            return;
        }


        file << name << "," << id << "," << club << endl;
        file.close();

        cout << "Member added successfully." << endl;
    }

    string sendRequests(string name, string id, string club) {

        //cin.ignore(numeric_limits<streamsize>::max(), '\n');
        //cout << "Enter name of the member: ";
        //getline(cin, name);

        //cout << "Enter ID of the member: ";
        //getline(cin, id);
        //cout << "Enter club of the member: ";
        //getline(cin, club);


        ofstream file("D://capstone//Requests.csv", ios::app);
        if (!file.is_open()) {
            cerr << "Failed to open CSV file." << endl;
            return "Failed to open CSV file.";
        }


        file << name << "," << id << "," << club << endl;
        file.close();

        cout << "Request sent successfully." << endl;
        return "Request sent successfully.";
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

        Member student{ name, id, club };
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
vector<string> returnKey() {
    vector<string> v;
    unordered_map<string, Member> hashtable = buildHashTable("D://capstone//Records.csv", "name");
    for (const auto& pair : hashtable) {
        v.push_back(pair.first);
    }
    return v;
}


namespace py = pybind11;


PYBIND11_MODULE(superfastcode2, m) {   

    py::class_<Member>(m, "Member")
        .def(py::init<>())
        .def("search_by_id", &Member::searchbyID)
        .def("member_request", &Member::sendRequests)

        .def("search_by_name", &Member::searchbyName);




    m.def("autokeys", &returnKey, R"pbdoc(
        Compute a hyperbolic tangent of a single argument expressed in radians.
    )pbdoc");

#ifdef VERSION_INFO 
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}
