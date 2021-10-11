# VLC para reproducir audios mp3
import vlc
# Para elegir respuesta random
import random
#Carpeta de speeches
speeches_dir = 'speeches/'
open_dir = speeches_dir + 'open/'
errors_dir = speeches_dir + 'errors/'
salutations_dir = speeches_dir + 'salutations/'
instructions_dir = speeches_dir + 'instructions/'

#La clase que contiene cada speech
class speech:
    def speak(file):
        return vlc.MediaPlayer(file)
    def speak_random(list):
        return vlc.MediaPlayer(random.choice(list))

    # Introducing David
    intro = speak('speeches/introducing.mp3')

    # Waiting for the wake up word
    wait_to_wake_list = [
        f'{instructions_dir}waitToWake.mp3',
        f'{instructions_dir}waitToWake1.mp3',
        f'{instructions_dir}waitToWake2.mp3',
        f'{instructions_dir}waitToWake3.mp3',
        f'{instructions_dir}waitToWake4.mp3',
        f'{instructions_dir}waitToWake5.mp3'
        ]  
    wait_to_wake = speak_random(wait_to_wake_list)

    ## Waiting Command ##
    waiting_prompt_list = [
        f'{instructions_dir}waitingPrompt.mp3',
        f'{instructions_dir}waitingPrompt1.mp3',
        f'{instructions_dir}waitingPrompt2.mp3',
        f'{instructions_dir}waitingPrompt3.mp3',
        f'{instructions_dir}waitingPrompt4.mp3'
    ]
    waiting_prompt = speak_random(waiting_prompt_list)

    ## OPENING STUFF ###
    opening_list = [
        f'{open_dir}opening.mp3',
        f'{open_dir}opening1.mp3',
        f'{open_dir}opening2.mp3',
        f'{open_dir}opening3.mp3'
    ]
    opening = speak_random(opening_list)
    open_youtube = f'{open_dir}open_youtube.mp3'
    open_facebook = f'{open_dir}open_facebook.mp3'

    ## ERRORS ##
    listening_error_list = [
        f'{errors_dir}listeningError.mp3',
        f'{errors_dir}listeningError1.mp3',
        f'{errors_dir}listeningError2.mp3',
        f'{errors_dir}listeningError3.mp3',
        f'{errors_dir}listeningError4.mp3'
    ]
    listening_error = speak_random(listening_error_list)
    cant_do_it_list = [
        f'{errors_dir}cantDoIt.mp3',
        f'{errors_dir}cantDoIt1.mp3',
        f'{errors_dir}cantDoIt2.mp3',
    ]
    cant_do_it = speak_random(cant_do_it_list)

    ## CURRENT FEELINGS ##
    ok_list = [
        f'{salutations_dir}feelings/ok.mp3',
        f'{salutations_dir}feelings/ok1.mp3',
        f'{salutations_dir}feelings/ok2.mp3',
        f'{salutations_dir}feelings/ok3.mp3',
        f'{salutations_dir}feelings/ok4.mp3',
        f'{salutations_dir}feelings/ok5.mp3',
        f'{salutations_dir}feelings/ok6.mp3',
    ]
    current_feeling = speak_random(ok_list)