#!/bin/bash
# Performs one time setup at first boot of the VM.

exitstatus=1

getStudentEmail() {
    # Run the loop until a valid email is entered
    while [ $exitstatus != 0 ]
    do
        STUDENT_EMAIL=$(whiptail --inputbox "Enter your email address:" 8 39 student@studnent.oulu.fi --title "Labs Setup" 3>&1 1>&2 2>&3)
        # A trick to swap stdout and stderr.
        # Again, you can pack this inside if, but it seems really long for some 80-col terminal users.
        exitstatus=$?
        if [ $exitstatus = 1 ]; then
            whiptail --title "Labs Setup" --msgbox "This setup cannot be cancelled" 8 78
        fi

    done
}

launchDockerCompose() {
    # Start the Docker Compose services for the labs
    # docker compose -f /labs/vuln_research/docker-compose.yml up -d
    docker compose -f /labs/metasploit/docker-compose.yml up -d
    docker compose -f /labs/priv_esc/docker-compose.yml up -d
}

setup() {
    getStudentEmail

    # export the student email to the environment
    export STUDENT_EMAIL

    launchDockerCompose
}

#unbind the interrupt key
stty intr undef

setup

# restore interrupt key
stty intr ^C