#include <array>
#include <iostream>
#include <cstdlib>
#include <format>
#include <memory>

void openPythonFile() {
    int result = system("python main.py");

    if (result != 0) {
        std::cerr << "Failed to open main.py" << std::endl;
    }
}

void PythonInstall() {
    std::cout << "是否安装 Python 3.12? Y/N\n";
    char input;
    std::cin >> input;
    if (input == 'Y' || input == 'y') {
        std::string PATH;
        std::cout << "请输入安装路径\n若输入0则选择默认安装路径";
        std::cin >> PATH;
        if(PATH == "0") {
            PATH = "D:/";
        }
        std::system(std::format("powershell -Command \"wget -O {}Python_setup.exe https://www.python.org/ftp/python/3.12.7/python-3.12.7.exe\"",PATH).c_str());
        std::system(std::format("powershell -command \"Start-Process -FilePath '{}Python_setup.exe'\"",PATH).c_str());
    }
    if (input == 'N' || input == 'n') {

    }
}

int checkPythonVersion() {
    std::array<char, 128> buffer{};
    std::string result;
    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen("python --version 2>&1", "r"), pclose);

    if (!pipe) {
        std::cerr << "Failed to run command.\n";
        return false;
    }

    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data();
    }

    if(result.find("Python 3.12") != std::string::npos) {
        return 2;
    }
    else if(result.find("Python") != std::string::npos) {
        return 1;
    }
    else {
        return 0;
    }
}

int main() {
    system("chcp 65001");
    int back = checkPythonVersion();
    if(back == 2) {
        std::cout << "Python 3.12 已安装\n";
        openPythonFile();
    }
    else if(back == 1) {
        std::cerr << "Python 已安装，但不是3.12版本，建议您使用Python 3.12\n";
        PythonInstall();
    }
    else {
        std::cerr << "Python 未安装";
        PythonInstall();
    }
    return 0;
}
