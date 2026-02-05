#include <iostream>
#include <string>

#include <thread>
#include <chrono>


int index;

void write_step(
    int str_i,
    int slag_i,
    const std::string& str,
    const std::string& slag
) {
    std::cout << "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
    for (int j = 0; j < str_i; j++) std::cout << ' ';
    std::cout << "|";
    for (int j = 0; j < slag_i; j++) std::cout << "|";

    std::cout << '\n' << str << "\n----------------------------------------\n";
    std::cout << slag << '\n';
    for (int j = 0; j < slag_i; j++) std::cout << ' ';
    std::cout << "|\n";
    std::this_thread::sleep_for(std::chrono::milliseconds(200));
    
}



bool found(const std::string& str, const std::string& slag) {
    if (slag.size() > str.size()) return false;
    for (size_t str_i = 0; str_i + slag.size() <= str.size(); str_i++) {
        bool is_found = true;
        for (size_t slag_i = 0; slag_i < slag.size(); slag_i++) {
            //write_step(str_i, slag_i, str, slag);
            if (str[str_i + slag_i] != slag[slag_i]) {
                is_found = false;
                break;
            }
        }

        if (is_found) {
            index = str_i;
            return true;
        }
    }

    return false;
}

void replace(std::string& str, const std::string& slag_old, const std::string& slag_new) {
    //std::cout << "> Replacing " << slag_old << " with " << slag_new << '\n';
    if (found(str, slag_old)) {
        str.erase(
            str.begin() + index,
            str.begin() + (int)(index + slag_old.size())
        );
        str.insert(index, slag_new);
    }
    //std::cout << "< finished replacing\n------------\n";
    //std::cout << str << '\n';
}

int main() {
    std::string s = "1";
    for (int i = 0; i < 80; i++) {
        s += '8';
    }
    
    while (found(s, "18") || found(s, "288") || found(s, "3888")) {
        if (found(s, "18")) {
            replace(s, "18", "2");
        } else if (found(s, "288")) {
            replace(s, "288", "3");
        } else if (found(s, "3888")){
            replace(s, "3888", "1");
        }
        //std::cout << s << '\n';
    }
    

    std::cout << "RESULT IS: " << s << '\n';
    return 0;

}
