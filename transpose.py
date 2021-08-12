#Code from the "Transpose midi with python for computational creativity in the domain of music" article by Nick Kelly
#Source URL: http://nickkellyresearch.com/python-script-transpose-midi-files-c-minor/

#converts all midi files in the current folder

import glob
import os
import music21

#converting everything into the key of C major or A minor

# major/minor conversions including sharps
majors = dict(['A-', 4),('G#', 4),('A', 3),('A#', 2),('B-', 2),('B', 1),('C', 0),('C#', -1),('D-', -1),('D', -2),('D#', -3),('E-', -3),('E', -4),('F', -5),('F#', 6),('G-', 6),('G', 5)])
minors = dict([('G#', 1), ('A-', 1),('A', 0),('A#', -1),('B-', -1),('B', -2),('C', -3),('C#', -4),('D-', -4),('D', -5),('D#', 6),('E-', 6),('E', 5),('F', 4),('F#', 3),('G-', 3),('G', 2)])

#os.chdir("./")
for file in glob.glob("*.mid"):
    score = music21.converter.parse(file)
    key = score.analyze('key')
#    print key.tonic.name, key.mode
    if key.mode == "major":
        halfSteps = majors[key.tonic.name]
        newFileName = "C_" + file
        
    elif key.mode == "minor":
        halfSteps = minors[key.tonic.name]
        newFileName = "Am_" + file
    newscore = score.transpose(halfSteps)
    key = newscore.analyze('key')
    #print key.tonic.name, key.mode
    #newscore.write('midi',newFileName)
    returm newscore
