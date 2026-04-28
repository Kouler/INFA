#include<iostream>
#include<fstream>
#include<vector>
#include <algorithm>

int main() {
    std::ifstream fi("./txt_files/26_58493.txt");

    int N;
    fi >> N;
    //std::cout << N;
    struct VehicleMove {
        int start;
        int end;
        bool is_car;
        VehicleMove() : start(0), end(0), is_car(false) {}
        bool operator< (const VehicleMove& other) const {
            return this->start < other.start;
        }
    };

    std::vector<VehicleMove> arr(N);
    
    for (int i = 0; i < N; i++) {
        char C;
        fi >> arr[i].start >> arr[i].end >> C;
        arr[i].end += arr[i].start;
        if (C == 'A') arr[i].is_car = true;
    }

    std::sort(arr.begin(), arr.end());
    
    std::ofstream sorted("./txt_files/sorted.txt");
    for (auto el : arr) {
        sorted << el.start << ' ' << el.end << ' ' << (el.is_car ? "Car" : "Van") << '\n';
    }

    int HER_POIMI_SKOLKO_VREMYA = 100000;

    std::vector<int> C_arr(HER_POIMI_SKOLKO_VREMYA);
    std::vector<int> V_arr(HER_POIMI_SKOLKO_VREMYA);
    
    int C_count = 80;
    int V_count = 20;
    
    int cars_parked = 0;
    int vehicles_not_parked = 0;
    //--------


    int arr_index = 0;
    for (int i = 0; i < 1441; i++) {
        C_count += C_arr[i];
        V_count += V_arr[i];
        if (arr_index < arr.size() && arr[arr_index].start == i) {
            std::cout << "[" << arr_index << "] C_count: " << C_count << ", V_count: " << V_count << "   [time: " << i << "]" << '\n';
            VehicleMove vehicle = arr[arr_index];
            arr_index+= 1;
            if (vehicle.is_car && C_count > 0) {
                C_arr[vehicle.end]++;
                C_count--;
                cars_parked++;
                continue;
            }

            if (V_count > 0) {
                if (vehicle.is_car) cars_parked++;
                V_arr[vehicle.end]++;
                V_count--;
            }
            else {
                vehicles_not_parked++;
            }
        }
    }

    //--------
    std::cout << "Parked: " << cars_parked << ", vehicles banned: " << vehicles_not_parked;

}





void task_46984() {
    bool** matrix = new bool*[10000];
    for (int i = 0; i < 10000; i++) {
        matrix[i] = new bool[10000];

        for (int j = 0; j < 10000; j++) {
            matrix[i][j] = 0;
        }    
    }
    

    std::ifstream fi("./txt_files/26_46984.txt");
    
    
    int N;
    fi >> N;
    for (int i = 0; i < N; i++) {
        int y;
        int x;
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
    

    std::cout << maxCount << " " << maxRowNumber + 1 << '\n';   
}

void task78051() {
    std::ifstream fi("./txt_files/26_78051.txt");
    
    
    int Number;
    fi >> Number;
    
    std::vector<int> arr(1441);


    
    int entered, exited;
    for (int i = 0; i < Number; i++) {
        fi >> entered >> exited;
        arr[entered]++;
        arr[exited+1]--;

    }
    int maxCount = 0;
    int count = 0;
    int backwardChangedCount = 0;
    int preLastMinute = 0;
    for (int i = arr.size() - 1; i >= 0; i--) {
        if (arr[i] == 0) { 
            count++;
            if (maxCount < count +1) {
                maxCount = count +1;
            }
        }
        else {
            count = 0;
            backwardChangedCount++;
        }

        if (backwardChangedCount == 2) {
            preLastMinute = i;
        }
    
    }
    std::cout << maxCount << " " << preLastMinute << "\n";
}
/*

8 1268
6 1072
37 107

max = 8

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ..., 1378, ..., 1438, 1439, 1440]
    +  -  -  -  -  -  -  -  +  -   ...   +   ...      +     -     +

*/
