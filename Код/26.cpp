#include<iostream>
#include<fstream>
#include<vector>


int main() {
    bool** matrix = new bool*[10000];
    for (int i = 0; i < 10000; i++) {
        matrix[i] = new bool[10000];

        for (int j = 0; j < 10000; j++) {
            matrix[i][j] = false;
        }    
    }

    std::ifstream fi("./txt_files/26_46984.txt");
    
    int N;
    fi >> N;
    for (int i = 0; i < N; i++) {
        int x;
        int y;
        fi >> y >> x;
        matrix[y -1][x -1] = true;
    }

    int maxCount = 0;
    int maxRowNumber = 0;
    //34 34
    for (int y = 0; y < 10000; y++) {
        int count = 0;
        for (int x = 0; x < 10000; x++) {
            if (matrix[y][x]) {
                count += 1;
                if (count > maxCount) {
                    maxCount = count;
                    maxRowNumber = y;
                }
            }
            else count = 0;
        
        }  
    }   
    //34 34
    //

    std::cout << maxCount << " " << maxRowNumber + 1 << '\n';   
}  