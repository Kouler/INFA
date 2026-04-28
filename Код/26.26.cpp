#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>  // для std::max

int main() {
    std::ifstream fi("./txt_files/26_78051.txt");
    int N;
    fi >> N;
    std::vector<int> arr(1441, 0);
    int enter, exit;
    for (int i = 0; i < N; ++i) {
        fi >> enter >> exit;
        arr[enter]++;
        arr[exit]--;
    }

    // собираем моменты изменений
    std::vector<int> changes;
    for (int i = 0; i <= 1440; ++i) {
        if (arr[i] != 0) changes.push_back(i);
    }

    // длина между границей 0 и первым изменением
    int maxLen = changes.empty() ? 1440 : changes[0] - 0;  // если ни одного изменения

    for (size_t i = 1; i < changes.size(); ++i) {
        int len = changes[i] - changes[i-1];
        if (len > maxLen) maxLen = len;
    }
    // длина от последнего изменения до 1440
    if (!changes.empty()) {
        int lastLen = 1440 - changes.back();
        if (lastLen > maxLen) maxLen = lastLen;
    }

    // предпоследнее изменение за сутки
    int preLastMinute = 0;
    if (changes.size() >= 2) {
        preLastMinute = changes[changes.size() - 2];
    } else if (changes.size() == 1) {
        // формально предпоследнего нет, можно оставить 0 или уточнить по условию
        preLastMinute = changes[0];
    }

    std::cout << maxLen << " " << preLastMinute << "\n";
    return 0;
}