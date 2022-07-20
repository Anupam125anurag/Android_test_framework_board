*** Settings ***
#Suite Setup    Initialize Metadata
Library     ../library/base_lib.py
Library     ../library/multimedia_lib.py

Test Setup   START_TEST
Test Teardown  END_TEST

*** Keyword ***


*** Test Cases ***
Test 001 - Play an audio music
    [tags]    Sanity
    #launch music player
    #${result}     LAUNCH_APP     ${appname}
    ${result}     LAUNCH_MUSIC
    ${result}     PLAY_MUSIC
    run keyword if  ${result}==False    Fail   Playing_Music_Failed    ELSE    LOG    PASS

Test 002 - Navigate audio
    [tags]    Sanity
    #${result}     LAUNCH_APP     ${appname}
    ${result}     LAUNCH_MUSIC
    ${result}     NAVIGATE_MUSIC
    run keyword if  ${result}==False    Fail   Navigate_Music_Failed    ELSE    LOG    PASS




