#!/bin/bash
# Performs one time setup at first boot of the VM.

bold="$(tput bold)"
blue="$(tput setaf 4)" 
cyan="$(tput setaf 6)"
green="$(tput setaf 2)"
yellow="$(tput setaf 3)"
reset="$(tput sgr0)"

# setting enivronment variables to be used during setup
export LOG_LEVEL="INFO"
export SECRET="<secret here>"

banner() {
    # This function prints a banner to the terminal.
    
    bold="$(tput bold)"
    blue="$(tput setaf 4)" 
    cyan="$(tput setaf 6)"  
    reset="$(tput sgr0)"

    art="${bold}${blue}           
  __               __    __                   __       __          
 |  |--.---.-.----|  |--|__.-----.-----.     |  .---.-|  |--.-----.
 |     |  _  |  __|    <|  |     |  _  |     |  |  _  |  _  |__ --|
 |__|__|___._|____|__|__|__|__|__|___  |_____|__|___._|_____|_____|
                                 |_____|______|                    

    ${reset}${cyan}          labs for IC00AJ64-3002 Course${reset}            "                                                      

    echo "$art"

}

getStudentEmail() {
    # This function prompts the user to enter their email address.
    exitstatus=1
    # Run the loop until a valid email is entered
    while [ $exitstatus != 0 ]
    do
        STUDENT_EMAIL=$(whiptail --inputbox "Enter your email address:" 8 39 student@student.oulu.fi --title "Labs Setup" 3>&1 1>&2 2>&3)
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
    echo "Setting up the lab environment..."

    docker compose -f /labs/vuln_research/docker-compose.yml up -d &> /dev/null
    if [ $? -eq 0 ]; then
        echo "${bold}${green}[  OK  ]${reset}   Vulnerability Research lab is up and running!"
    fi

    # docker compose -f /labs/metasploit/docker-compose.yml up -d &> /dev/null
    # if [ $? -eq 0 ]; then
    #     echo "${bold}${green}[  OK  ]${reset}   Metasploit lab is up and running!"
    # fi

    docker compose -f /labs/priv_esc/docker-compose.yml up -d &> /dev/null
    if [ $? -eq 0 ]; then
        echo "${bold}${green}[  OK  ]${reset}   Privilege Escalation lab is up and running!"
    fi

    docker compose -f /labs/web/docker-compose.yml up -d &> /dev/null
    if [ $? -eq 0 ]; then
        echo "${bold}${green}[  OK  ]${reset}   Web Hacking lab is up and running!"
    fi

    # docker compose -f /labs/burp_suite/docker-compose.yml up -d &> /dev/null
    # if [ $? -eq 0 ]; then
    #     echo "${bold}${green}[  OK  ]${reset}   Burp Suite Lab is up and running!"
    # fi
}

generatAndInjectFlags() {
    # Generates  and injects dynamic flags for the labs
    source /opt/venv/bin/activate
    python3 -m app.main --email $STUDENT_EMAIL
    echo "${bold}${green}[  OK  ]${reset}   Burp Suite Lab is up and running!"
    echo "${bold}${green}[  OK  ]${reset}   Metasploit lab is up and running!"
    echo "${bold}${green}[  OK  ]${reset}   Network Security lab is up and running!"


}

cleanup() {
    # This function performs the cleanup operations after the setup is complete.
    echo "Performing cleanup operations..."

    # Disable and remove the service to prevent it from running again
    #TODO: use variables for the service names
    systemctl disable firstboot.service &> /dev/null

    # remove the firstboot script
    $rm "$0"

    # remove the flag generator app
    rm -rf usr/lib/python3.12/app

    echo "${bold}${green}[  OK  ]${reset}   Cleanup completed successfully."
    read -p "Press [Enter] to continue..." -r
}

setup() {
    # Sets up the lab environment by calling the necessary functions

    clear
    getStudentEmail

    clear
    banner

    echo "Student email set to: ${bold}${yellow}${STUDENT_EMAIL}${reset}"

    # export the student email to the environment
    export STUDENT_EMAIL

    launchDockerCompose

    generatAndInjectFlags

    cleanup
}
#unbind the interrupt key
stty intr undef

setup

# restore interrupt key
stty intr ^C