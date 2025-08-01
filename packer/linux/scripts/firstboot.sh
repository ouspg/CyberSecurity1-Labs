#!/bin/bash
# Performs one time setup at first boot of the VM.

banner() {
    # This function prints a banner to the terminal.
    
    if [ -x "$(command -v tput)" ]; then
        bold="$(tput bold)"
        blue="$(tput setaf 4)" 
        cyan="$(tput setaf 6)"  
        reset="$(tput sgr0)"
    fi

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
    # docker compose -f /labs/vuln_research/docker-compose.yml up -d
    docker compose -f /labs/metasploit/docker-compose.yml up -d
    docker compose -f /labs/priv_esc/docker-compose.yml up -d
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

setup() {
    # Sets up the lab environment by calling the necessary functions
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