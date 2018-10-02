#!/bin/bash

FILE=cours.md
if [ -f $FILE ]; then
    \rm $FILE
fi

# generation des chapitres independants
source generateChapter.sh 1
source generateChapter.sh 2
source generateChapter.sh 3

## generation du fichier complet.
LISTE=$(ls 000_title.md 00_title.md 0*_0*.md 98_liens.md)
echo $LISTE
cat $LISTE > cours.md
