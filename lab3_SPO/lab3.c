#include <windows.h>
#include <string>
#include <vector>
#include <algorithm>
#include <ctime>
using namespace std;

const int MIN_PASSWORD_LENGTH = 8;
const int MAX_PASSWORD_LENGTH = 16;
const int NUM_PASSWORDS = 5;

const char g_szClassName[] = "myWindowClass";
HWND g_hWndEdit;

// Get the text currently entered in the edit control
string GetEditText()
{
    char buff[1024];
    GetWindowText(g_hWndEdit, buff, 1024);
    return buff;
}

// Generate a random password based on the entered text and the time
string GeneratePassword()
{
    // Get the current time
    time_t now = time(NULL);

    // Get the text entered in the edit control
    string editText = GetEditText();

    // Combine the text and the time
    string combined = editText + to_string(now);

    // Generate a random permutation of the combined string
    random_shuffle(combined.begin(), combined.end());

    // Truncate the string to a random length between MIN_PASSWORD_LENGTH and MAX_PASSWORD_LENGTH
    int length = rand() % (MAX_PASSWORD_LENGTH - MIN_PASSWORD_LENGTH + 1) + MIN_PASSWORD_LENGTH;
    return combined.substr(0, length);
}

// Update the edit control with the generated passwords
void UpdateEditControl()
{
    // Clear the edit control
    SetWindowText(g_hWndEdit, "");

    // Generate the passwords and add them to the edit control
    for (int i = 0; i < NUM_PASSWORDS; i++)
    {
        string password = GeneratePassword();
        SendMessage(g_hWndEdit, EM_REPLACESEL, 0, (LPARAM)password.c_str());
        SendMessage(g_hWndEdit, EM_REPLACESEL, 0, (LPARAM)"\r\n");
    }
}

LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam)
{
    switch (msg)
    {
    case WM_CREATE:
        g_hWndEdit = CreateWindowW(L"Edit", L"", WS_CHILD | WS_VISIBLE | WS_VSCROLL | ES_MULTILINE | ES_AUTOVSCROLL | ES_READONLY,
            15, 15, 300, 200, hwnd, NULL, NULL, NULL);
        CreateWindowW(L"Button", L"Generate Passwords", WS_VISIBLE | WS_CHILD,
            15, 230, 150, 25, hwnd, (HMENU)1, NULL, NULL);
        CreateWindowW(L"Button", L"Clear", WS_VISIBLE | WS_CHILD,
            165, 230, 75, 25, hwnd, (HMENU)2, NULL, NULL);
        CreateWindowW(L"Button", L"Quit", WS_VISIBLE | WS_CHILD,
            245, 230, 70, 25, hwnd, (HMENU)3, NULL, NULL);
        break;
    case WM_COMMAND:
        switch (LOWORD(wParam))
        {
        case 1: // Generate Passwords button clicked
            UpdateEditControl();
            break;
        case 2: // Clear button clicked
            SetWindowText(g_hWndEdit, "");
            break;
        case 3: // Quit button clicked
            PostQuitMessage(0);
            break;
        }
        break;
    case WM_CLOSE:
        DestroyWindow(hwnd);
        break;
    case WM_DESTROY:
        PostQuitMessage(0);
        break;
    }
