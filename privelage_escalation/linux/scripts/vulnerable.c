#include <unistd.h>

void main() {

    // set user and group context for user `jenkins_agent`
    gid_t groups[] = {1002,1004,1005};
    setgroups(3, groups);
    setgid(1002);
    setuid(1002);

    // execute arbitrary binary
    system("thm");
}
