#!/bin/bash
# Performs one time setup at first boot of the VM.

exitstatus=1
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
echo "(Exit status was $exitstatus)"
echo "Your email address is: $STUDENT_EMAIL"