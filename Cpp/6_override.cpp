#include <iostream>
#include <string>


class Doctor {
public:
    std::string name;
    int age;

    Doctor(const std::string& name, int age) : name(name), age(age) {}
    virtual void work() = 0; // Pure virtual function
};


class HospitalDoctor : public Doctor {
public:
    std::string department;

    HospitalDoctor(const std::string& name, int age, const std::string& department)
        : Doctor(name, age), department(department) {}

    void work() override {
        std::cout << "I work in the " << department << " department." << std::endl;
    }
};


class GeneralPractitioner : public Doctor {
public:
    std::string clinicName;

    GeneralPractitioner(const std::string& name, int age, const std::string& clinicName)
        : Doctor(name, age), clinicName(clinicName) {}

    void work() override {
        std::cout << "I work at " << clinicName << " clinic." << std::endl;
    }
};


class Consultant : public HospitalDoctor {
public:
    std::string specialty;

    Consultant(const std::string& name, int age, const std::string& department, const std::string& specialty)
        : HospitalDoctor(name, age, department), specialty(specialty) {}

    void work() override {
        std::cout << "I work as a consultant in the " << department << " department specializing in " << specialty << "." << std::endl;
    }
};


class TeamDoctor : public HospitalDoctor {
public:
    std::string teamName;

    TeamDoctor(const std::string& name, int age, const std::string& department, const std::string& teamName)
        : HospitalDoctor(name, age, department), teamName(teamName) {}

    void work() override {
        std::cout << "I work as a team doctor for " << teamName << "." << std::endl;
    }
};


class TraineeDoctor : public TeamDoctor {
public:
    int yearsOfTraining;

    TraineeDoctor(const std::string& name, int age, const std::string& department, const std::string& teamName, int yearsOfTraining)
        : TeamDoctor(name, age, department, teamName), yearsOfTraining(yearsOfTraining) {}

    void work() override {
        std::cout << "I am a trainee doctor with " << yearsOfTraining << " years of training in the " << department << " department, team " << teamName << "." << std::endl;
    }
};


class QualifiedDoctor : public TeamDoctor {
public:
    int yearsOfExperience;

    QualifiedDoctor(const std::string& name, int age, const std::string& department, const std::string& teamName, int yearsOfExperience)
        : TeamDoctor(name, age, department, teamName), yearsOfExperience(yearsOfExperience) {}

    void work() override {
        std::cout << "I am a qualified doctor with " << yearsOfExperience << " years of experience in the " << department << " department, team " << teamName << "." << std::endl;
    }
};

int main() {
    HospitalDoctor hd("Dr. Smith", 45, "Cardiology");
    GeneralPractitioner gp("Dr. Jones", 50, "Healthy Life");
    Consultant con("Dr. Brown", 55, "Neurology", "Brain Surgery");
    TeamDoctor td("Dr. White", 40, "Orthopedics", "Trauma Team");
    TraineeDoctor trd("Dr. Green", 30, "Orthopedics", "Trauma Team", 2);
    QualifiedDoctor qd("Dr. Black", 48, "Orthopedics", "Trauma Team", 15);

    std::cout << "HospitalDoctor: ";
    hd.work();
    std::cout << "GeneralPractitioner: ";
    gp.work();
    std::cout << "Consultant: ";
    con.work();
    std::cout << "TeamDoctor: ";
    td.work();
    std::cout << "TraineeDoctor: ";
    trd.work();
    std::cout << "QualifiedDoctor: ";
    qd.work();

    return 0;
}
