#!/bin/bash
# Performs one time setup at first boot of the VM.

bold="$(tput bold)"
blue="$(tput setaf 4)" 
cyan="$(tput setaf 6)"
green="$(tput setaf 2)"
yellow="$(tput setaf 3)"
reset="$(tput sgr0)"

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
    echo "Setting up the lab environment..."

    docker compose -f /labs/vuln_research/docker-compose.yml up -d &> /dev/null
    if [ $? -eq 0 ]; then
        echo "${bold}${green}[  OK  ]${reset}   Vulnerability Research lab is up and running!"
    fi

    docker compose -f /labs/metasploit/docker-compose.yml up -d &> /dev/null
    if [ $? -eq 0 ]; then
        echo "${bold}${green}[  OK  ]${reset}   Metasploit lab is up and running!"
    fi

    docker compose -f /labs/priv_esc/docker-compose.yml up -d &> /dev/null
    if [ $? -eq 0 ]; then
        echo "${bold}${green}[  OK  ]${reset}   Privilege Escalation lab is up and running!"
    fi
}

generateFlags() {
    # Generates dynamic flags for the labs
    # This could be done by creating files, setting environment variables, etc.
    # For now, it just echoes message
    echo "Generating flags..."

}

injectFlags() {
    # Injects the generated flags into the lab environment
    # This could be done by copying files, setting environment variables, etc.
    # For now, it just echoes a message
    echo "Flags injected successfully."
}

cleanup() {
    # This function performs the cleanup operations after the setup is complete.
    echo "Performing cleanup operations..."

    # Disable and remove the service to prevent it from running again
    #TODO: use variables for the service names
    systemctl disable firstboot.service &> /dev/null
    # $rm "$0"

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

    cleanup
}
#unbind the interrupt key
stty intr undef

setup

# restore interrupt key
stty intr ^C