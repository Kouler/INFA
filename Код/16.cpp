#include <iostream>

int F(int n) {
    return n ? F(n / 10) + (n % 10) : 0;
}

int main() {
    int count = 0;

    std::cout << F(554);

    int percent = (1134567010 - 237567892) / 100;
    int out = 0;
    /*
    for (int i = 237567892; i < 1134567010; i++)  {
        if (i % percent == 0) {
            std::cout << out << "%\n";
            out+= 1;
        }
        if (F(i) > F(i+1)) 
            count+= 1;
    }

    std::cout << "Res: " << count << '\n';
    */
    


}