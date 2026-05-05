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

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    m "mm..."
    m "digin..digin"
    m '..hmm'
    m "digin..digin"
    m "ahhhhh!!"
    m 'Found it!!... YAY!'
    p "What are you doing girl??"
    p "Look at yourself!"
    p 'So dirty!'
    m "HEY! look dad, What I just found!"
    m "It looks like a buried space shop"
    m "Or.."
    m "or.. is it a ...."
    m " A T-rex fossil!!"
    p "Yeh..yeh , now get out of that hole!"
    m "No dad ,seee..it"
    p "No! I don't wanna be dirty"
    p "I am a good-clean dog"
    p "And I certainty don't want to get dirty for a pile of Garbage"
    m "It's not grabage.."
    m "its's a treasure!,,"
    m "Maybe..Maybe they make me the mayor , for finding it"
    p "yeh.. That's not happening"
    p "HEY.. FILLICIA... I FOUND HER.."
    "(HE CALLS HER MOTHER)"
    f "Where!.. where is she?"
    f "She's okay right?"
    p "I don't understand how to answer you sometimes"
    f "OHHH! my baby, you okay"
    f "Are you hurt!!?"
    p "Apparently she was tring to find a T-rex"
    p "haha..."
    p "When I was a puppy, I also.."

    p "was.. Really keen for these treasure hunts"
    p ""
    p "I really..."
    p "...nn"
    p "really , miss my childhood"
    f "Awww!!"
    f "Someone's so emotional today.."
    m "Don't worry daddy!"
    m "If I become the mayor"

    m "I would.. make you the president"
    f "YESS! my little girl.."
    f "You can do that tomorrow!"
    f "Right now lets get inside"
    ""
    ""
    
    m "...what's for dinner mom?..."
    f "...all your favourites..."
    m "...PIZZA!??..."

    ""
    "."
    ".."
    "..."
    




  
    # This ends the game.

    return
