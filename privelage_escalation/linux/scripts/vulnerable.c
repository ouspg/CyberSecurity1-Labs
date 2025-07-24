#include <unistd.h>

void main() {
    setuid(1002);
    setgid(1002);
    // TODO: Add a command to fit the challange narrative
    system("thm");
}
