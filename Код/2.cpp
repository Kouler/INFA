#include <iostream>

int main() {    
    for (int w = 0; w < 2; w++) {
        for (int x = 0; x < 2; x++) {
            for (int y = 0; y < 2; y++) {
                for (int z = 0; z < 2; z++) {
                    if (
                        ((x == (w || y)) || ((w <= z) && (y <= w))) == 0
                    )
                        std::cout << w << ' ' << x << ' ' << y << ' ' << z << '\n';
                }
            }
        }
    }
    std::cout << "\n\n\nx\ty\tz\n";

    
        for (int x = 0; x < 2; x++) {
            for (int y = 0; y < 2; y++) {
                for (int z = 0; z < 2; z++) {
                    if (
                        ((x == z) || (x<=(y && z))) == 0
                    )
                        std::cout << x << '\t' << y << '\t' << z << '\n';
                }
            }
        }
}
