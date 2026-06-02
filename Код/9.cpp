#include <iostream>
#include <fstream>
#include <vector>

int main() {
    std::ifstream fi("ods_files/9(1).txt");
    const int ARRAY_LENGTH = 6;

    if (!fi.is_open()) {
        std::cout << "Не удалось открыть файл\n";
        return 1;
    }

    std::vector<int> arr(ARRAY_LENGTH);
    int total_count = 0;

    // Построчное чтение: пока можно прочитать первый элемент строки
    while (fi >> arr[0]) {
        for (int i = 1; i < ARRAY_LENGTH; ++i)
            fi >> arr[i];

        bool has_repeatable = false;
        int interesting_count = 0;

        // Проверка повторяемости чисел в строке — подсчёт вхождений каждого
        for (int i = 0; i < ARRAY_LENGTH; ++i) {
            // Считаем, сколько раз arr[i] встречается в строке
            int count = 0;
            for (int j = 0; j < ARRAY_LENGTH; ++j)
                if (arr[j] == arr[i]) ++count;

            if (count > 1)
                has_repeatable = true;   // в строке есть повторяющиеся числа

            bool unique = (count == 1);   // число встречается ровно один раз

            // Проверка наличия меньшего соседа
            bool has_smaller_neighbor = false;
            if (i > 0 && arr[i - 1] < arr[i])
                has_smaller_neighbor = true;
            if (i < ARRAY_LENGTH - 1 && arr[i + 1] < arr[i])
                has_smaller_neighbor = true;

            if (unique && has_smaller_neighbor)
                ++interesting_count;
        }

        if (has_repeatable && interesting_count >= 3)
            ++total_count;
    }

    std::cout << total_count << std::endl;
    fi.close();
    return 0;
}