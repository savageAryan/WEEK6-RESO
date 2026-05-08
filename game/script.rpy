# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character ('MiTTens', color="#f66077")
define p = Character ("PAT-RICK", color='#f90c00')
define f = Character ('Fillicia', color='#cbe771')


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music 'audio1.mp3' loop volume 0.5
    scene background

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show scene 1

    # These display lines of dialogue.

    m "mm..."
    show scene 2
    m "digin..digin"
    show scene 3
    m '..hmm'
    show scene 4
    m "digin..digin"
    show scene 5
    m "ahhhhh!!"
    m 'Found it!!... YAY!'
    show scene 6
    p "What are you doing girl??"
    show scene 7
    p "Look at yourself!"
    show scene 8
    p 'So dirty!'
    show scene 9
    m "HEY! look dad, What I just found!"
    
    m "It looks like a buried space ship"
    show scene 10
    m "Or.."
    m "or.. is it a ...."
    show scene 11
    m " A T-rex fossil!!"
    show scene 12
    p "Yeh..yeh , now get out of that hole!"
    show scene 9
    m "No dad ,seee..it"
    show scene 12
    p "No! I don't wanna be dirty"
    p "I am a good-clean dog"
    p "And I certainty don't want to get dirty for a pile of Garbage"
    show scene 9
    m "It's not grabage.."
    show scene 10
    m "its's a treasure!!.."
    show scene 11

    m "Maybe..Maybe they make me the mayor , for finding it"
    show scene 12
    p "yeh.. That's not happening"
    show scene 13
    p "HEY.. FILLICIA... I FOUND HER.."
    show scene 14
    "(HE CALLS HER MOTHER)"
    show scene 15
    f "(Where!.. where is she?)"
    show scene 16
    f "(She's okay right?)"
    show scene 17
    p "I don't understand how to answer you sometimes"
    show scene 18
    f "OHHH! my baby, you okay?"
    f "Are you hurt!!?"
    show scene 19
    p "Apparently she was tring to find a T-rex"
    p "haha..."
    p "When I was a puppy, I also.."

    p "was.. Really keen for these treasure hunts"
    show scene 20
    p ""
    p "I really..."
    show scene 21
    p "...nn"
    
    p "really , miss my childhood"
    show scene 22
    f "Awww!!"
    f "Someone's so emotional today.."
    show scene 21
    m "Don't worry daddy!"
    m "If I become the mayor"

    m "I would.. make you the president"
    show scene 22
    f "YESS! my little girl.."
    f "You can do that tomorrow!"
    f "Right now lets get inside"
    show scene 23
    ""
    show scene 24
    ""
    
    
    m "...what's for dinner mom?..."
    f "...all your favourites..."
    m "...PIZZA!??..."
    show scene 25
    ""

    "."
    show scene 26
    ".."
    show scene 27

    menu:
        "Do you want to see"
        'YES':
            jump YES
        "NO":
            jump no
        
   

label YES:
    
    "..."
    show scene 28
    play sound "wow.mp3" volume 2.0
    'GODD DAMNnnn..'
    return
    
label no:
    show scene 29
    'Probably;0'
          
    return
