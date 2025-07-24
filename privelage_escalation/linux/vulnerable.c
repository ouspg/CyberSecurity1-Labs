#include <unistd.h>

void main() {
    setuid(1002);
    setgid(1002);
    system("thm");  // vulnerable use of system()
}
