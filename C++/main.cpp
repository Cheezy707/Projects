#include <iostream>

int main(){
    std::string name{};
    std::cout << "what's your name? ";
    std::cin >> name;
    std::cout << "hello " << name << std::endl ;
    return 0;
}