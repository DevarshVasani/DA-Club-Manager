#include<iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <ctime>
#include <chrono>
#include <iomanip>
#include <vector>
#include <string>
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

    void addevent() {
        cin.ignore(numeric_limits<streamsize>::max(),'\n');
        cout << "Enter name of the event: ";
        getline(cin, name);

        cout << "Enter Venue of the event: ";
        getline(cin, Venue);

        cout << "Enter date of event (YYYY-MM-DD): ";
        string date;
        getline(cin, date);

        cout << "Enter time of event (HH:MM:SS): ";
        string time;
        getline(cin, time);

        datetime = date + " " + time;

        cout << "Enter club: ";
        getline(cin, club);

        //append the new event to Events.csv file
        ofstream eventsfile("Events.csv", ios::app);
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

        
        remove("Events.csv");
        rename("temp.csv", "Events.csv");

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
