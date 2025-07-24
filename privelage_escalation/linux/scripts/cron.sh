#!/bin/bash
BACKUPTIME=`date +%Y-%m-%d_%H:%M:%S`
DESTINATION="/home/dummyuser/backup_$BACKUPTIME.tar.gz"
SOURCEFOLDER="/home/dummyuser/Documents/commercial/prices.xlsx"
tar -cpzf $DESTINATION $SOURCEFOLDER