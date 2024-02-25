#include <iostream>
#include <Windows.h>
#include <thread>
#include <chrono>

using namespace std;


void DaemonMain() {
    while (true) {
        this_thread::sleep_for(chrono::seconds(1));
    }
}


int main() {
    // Скрытие консоли
    ShowWindow(GetConsoleWindow(), SW_HIDE);
    // Создание потока для демона
    HANDLE hThread = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)DaemonMain, NULL, 0, NULL);
    
    if (hThread == NULL) {
        cerr << "Failed to create daemon thread" << endl;
        return 1;
    }
    
    // Ожидание завершения работы демона
    WaitForSingleObject(hThread, INFINITE);
}
