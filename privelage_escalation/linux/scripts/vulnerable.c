#include <unistd.h>

void main() {

    // set user and group context for user `jenkins_agent`
    gid_t groups[] = {1001,1004,1005};
    setgroups(3, groups);
    setgid(1001);
    setuid(1001);

    // execute arbitrary binary
    system("thm");
}
