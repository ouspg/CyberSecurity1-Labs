#include <unistd.h>

void main() {
    gid_t groups[] = {1002,1004,1005};
    setgroups(2, groups);
    setgid(1002);
    setuid(1002);
    // TODO: Add a command to fit the challange narrative
    system("thm");
}
