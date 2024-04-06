#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cstring> 


#include <string>
#include <chrono>
#include <unordered_map>
#include <iomanip>
#include <limits>
#include <ctime>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include<pybind11/complex.h>
#include<pybind11/functional.h>

using namespace std;

class Event {
public:
    string name;
    string datetime;
    string Venue;
    string club;



    // Default constructor
    Event() : name(""), club("") {}

    // Parameterized constructor
    Event(const string& name, const string& club)
        : name(name), club(club) {}

    void addevent(string path_event,string name, string Venue,string datetime, string club) {
        //.ignore(numeric_limits<streamsize>::max(), '\n');
        //cout << "Enter name of the event: ";
        //getline(cin, name);

        //cout << "Enter Venue of the event: ";
        //getline(cin, Venue);

        //cout << "Enter date of event (YYYY-MM-DD): ";
        //string date;
        //getline(cin, date);

        //cout << "Enter time of event (HH:MM:SS): ";
        //string time;
        //getline(cin, time);

        //datetime = date + " " + time;

        //cout << "Enter club: ";
        //getline(cin, club);

        //append the new event to Events.csv file
        ofstream eventsfile(path_event, ios::app);
        if (!eventsfile.is_open()) {
            cerr << "Failed to open CSV file." << endl;
            return;
        }


        eventsfile << name << "," << Venue << "," << datetime << "," << club << endl;

        eventsfile.close();

        cout << "Event added successfully." << endl;
    }

    void deleteExpiredEvents() {
        //Getting current time
        auto now = chrono::system_clock::now();
        time_t currentTime = chrono::system_clock::to_time_t(now);


        ifstream inFile("Events.csv");
        ofstream tempFile("temp.csv");
        if (!inFile.is_open() || !tempFile.is_open()) {
            cerr << "Failed to open CSV file." << endl;
            return;
        }

        // Read each line from the file
        string line;
        while (getline(inFile, line)) {
            istringstream iss(line);
            string name, Venue, datetime, club;

            // Parse the line
            getline(iss, name, ',');
            getline(iss, Venue, ',');
            getline(iss, datetime, ',');
            getline(iss, club);

            // Converting datetime string to time_t object
            tm eventTime = {};
            istringstream datetimeStream(datetime);
            datetimeStream >> get_time(&eventTime, "%Y-%m-%d %H:%M:%S");
            time_t eventTimestamp = mktime(&eventTime);


            if (currentTime > eventTimestamp) {
                // Skip writing this line to temp file
                continue;
            }

            tempFile << line << endl;
        }


        inFile.close();
        tempFile.close();


        remove("D://capstone//Events.csv");
        rename("D://capstone//temp.csv", "D://capstone//Events.csv");

        cout << "Expired events deleted successfully." << endl;
    }

};
vector<string> readAllClubEvents(const string& filename) {
    vector<string> clubevents;
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Failed to open file: " << filename << endl;
        return clubevents;
    }

    string line;
    while (getline(file, line)) {
        stringstream ss(line);
        string name, datetime, Venue, club;

        getline(ss, name, ',');

        clubevents.push_back(name);
    }

    file.close();
    return clubevents;
}

vector<string> readAllDate(const string& filename) {
    vector<string> dates;
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Failed to open file: " << filename << endl;
        return dates;
    }

    string line;
    while (getline(file, line)) {
        stringstream ss(line);
        string name, datetime, Venue, club;

        getline(ss, name, ',');
        getline(ss, datetime, ',');

        dates.push_back(datetime);
    }

    file.close();
    return dates;
}

vector<string> readAllClubVenues(const string& filename) {
    vector<string> venues;
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Failed to open file: " << filename << endl;
        return venues;
    }

    string line;
    while (getline(file, line)) {
        stringstream ss(line);
        string name, datetime, Venue, club;

        getline(ss, name, ',');
        getline(ss, datetime, ',');
        getline(ss, Venue, ',');
        venues.push_back(Venue);
    }

    file.close();
    return venues;
}

vector<string> readAllClubNames(const string& filename) {
    vector<string> clubNames;
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Failed to open file: " << filename << endl;
        return clubNames;
    }

    string line;
    while (getline(file, line)) {
        stringstream ss(line);
        string name, datetime, Venue, club;

        getline(ss, name, ',');
        getline(ss, datetime, ',');
        getline(ss, Venue, ',');
        getline(ss, club);

        clubNames.push_back(club);
    }

    file.close();
    return clubNames;
}

class Member;

unordered_map<string, Member> buildHashTable(const string& myfile, const string& key);
void printHashTable(const unordered_map<string, Member>& hashtable);
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

    vector<string> searchbyName(unordered_map<string, Member> &hashtable,string& key) {
        vector<string>identity(3);

        
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

    vector<string> searchbyID(unordered_map<string, Member> &hashtable,string key) {
        vector<string>id(3);

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

    void replaceMember(char* path_records, string folderpath,const string& memberName, const string& newID, const string& newClub) {
        ifstream inFile(path_records);
        ofstream tempFile(folderpath);


        char* temp_array  = &folderpath[0];
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
                }
                else {
                    tempFile << line << endl;
                }
            }
            inFile.close();
            tempFile.close();

            remove(path_records);
            rename(temp_array, path_records);
        }
        else {
            cerr << "Failed to open CSV file." << endl;
        }
    }


    void deleteMemberRequest(string path_requests, string folderpath1,string memberName) {
        cout << path_requests << endl;
        

        cout << folderpath1 << endl;
        ifstream inFile(path_requests);
        ofstream tempFile(folderpath1);
        char *records_array = &path_requests[0];
        char *temppath = &folderpath1[0];
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
            remove(records_array);
            rename(temppath, records_array);
        }
        else {
            cerr << "Failed to open CSV file." << endl;
        }

        return;
    }


    string acceptRequests(string path_records, string path_requests,string folderpath,unordered_map<string, Member>& nametable,string name, string id, string club, string password) {// = buildHashTable("D://capstone//Records.csv", "name");

        printHashTable(nametable);


        // declaring character array (+1 for null terminator) 
        char* records_array = &path_records[0];



        // copying the contents of the 
        // string to char array 




        // copying the contents of the 
        // string to char array 


        ifstream requestFile(path_requests);
        if (!requestFile.is_open()) {
            cerr << "Failed to open Requests file." << endl;
            return "Failed to open Requests file.";
        }

        //getline(requestFile, name, ',');
        string key = name;
        //getline(requestFile, id, ',');
        //getline(requestFile, club);
        string club2 = club;
        requestFile.close();

        cout << "Showing the earliest sent request:" << endl;
        cout << "Member Name: " << name << endl;
        cout << "Member ID: " << id << endl;
        cout << "Member Club: " << club << endl;

        //string ans;
        //cout << "Do you want to accept the request? ";
        //cin >> ans;

        if (1) {
            //string password;
            //cout << "Enter password to accept the request: ";
            //cin >> password;
            string expectedPassword = club + "123";
            if ((password != expectedPassword) && " " + password != expectedPassword) {
                cout << "Incorrect password. Request not accepted." << endl;
                return "Incorrect";
            }

            auto it = nametable.find(key);
            if (it != nametable.end()) {
                string name1 = it->second.name;
                cout << "Name: " << name1 << endl;

                string id1 = it->second.id;
                cout << "ID: " << id1 << endl;

                string club1 = it->second.club += "/" + club2;
                cout << "Club: " << club1 << endl;

                replaceMember(records_array,folderpath,name1, id1, club1);
            }
            else {
                ofstream recordsFile(path_records, ios::app);
                if (!recordsFile.is_open()) {
                    cerr << "Failed to open Records file." << endl;
                    return "Failed to open Records file.";
                }
                recordsFile << name << "," << id << "," << club << endl;
                recordsFile.close();
            }

            deleteMemberRequest(path_requests,folderpath,name);
            cout << "Request accepted successfully." << endl;
            return "Request accepted successfully.";
        }
        else {
            cout << "Sorry your request has been rejected :(" << endl;
            
            deleteMemberRequest(path_requests, folderpath, name);
            return "Request rejected.";
        }
        return "done!";
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

    string sendRequests(string path_requests,string name, string id, string club) {

        //cin.ignore(numeric_limits<streamsize>::max(), '\n');
        //cout << "Enter name of the member: ";
        //getline(cin, name);

        //cout << "Enter ID of the member: ";
        //getline(cin, id);
        //cout << "Enter club of the member: ";
        //getline(cin, club);


        ofstream file(path_requests, ios::app);
        if (!file.is_open()) {
            cerr << "Failed to open CSV file." << endl;
            return "Failed to open CSV file.";
        }


        file << name << "," << id << "," << club << endl;
        file.close();

        cout << "Request sent successfully." << endl;
        return "Request sent successfully.";
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
            }
            else {
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
vector<string> returnKey(unordered_map<string, Member> & hashtable) {//hashtable = buildHashTable("D://capstone//Records.csv", "name");
    vector<string> v;
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
        .def("member_accept", &Member::acceptRequests)
        .def("readName", &Member::readName)
        .def("readId", &Member::readId)
        .def("readClub", &Member::readClub)
        .def("delete_request", &Member::deleteMemberRequest)
        .def("search_by_name", &Member::searchbyName);




    py::class_<Event>(m, "Event")
		.def(py::init<>())
		.def("add_event", &Event::addevent)
		.def("delete_expired_events", &Event::deleteExpiredEvents);




    m.def("autokeys", &returnKey, R"pbdoc(
        Compute a hyperbolic tangent of a single argument expressed in radians.
    )pbdoc");

    m.def("readAllClubEvents", &readAllClubEvents, R"pbdoc(
		gives data of all evevts)pbdoc");

	m.def("readAllDate", &readAllDate, R"pbdoc(gives data of all dates)pbdoc");

    m.def("readAllClubVenues", &readAllClubVenues, R"pbdoc(gives data of all venues)pbdoc");

    m.def("readAllClubNames", &readAllClubNames, R"pbdoc(gives data of all club names)pbdoc");

    m.def("buildHashTable", &buildHashTable, R"pbdoc(
		Compute a hyperbolic tangent of a single argument expressed in radians.)pbdoc");



#ifdef VERSION_INFO 
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}
