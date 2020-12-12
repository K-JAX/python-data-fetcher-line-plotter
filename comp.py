import numpy as np

from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects

# WE CREATE THE TEXT THAT IS GOING TO MOVE, WE CENTER IT.

screensize = (720,460)
WHITE = (255,255,255)

txtClip = TextClip('Unemployment U.S.',color='#2064AF', font="Oswald",
                   kerning = 5, fontsize=46)
cvc = CompositeVideoClip( [txtClip.set_pos('center')],
                        size=screensize)

# THE NEXT FOUR FUNCTIONS DEFINE FOUR WAYS OF MOVING THE LETTERS

def arrive(screenpos,i):
    v = np.array([-1,0])
    d = lambda t : max(0, 3-3*t)
    return lambda time: screenpos-400*v*d(time-0.2*i)
    

# WE USE THE PLUGIN findObjects TO LOCATE AND SEPARATE EACH LETTER

letters = findObjects(cvc) # a list of ImageClips


# WE ANIMATE THE LETTERS

def moveLetters(letters, funcpos):
    # funcpos = arrive in this case
    newPosition = [ 
                    letter.set_pos( funcpos( letter.screenpos,i ) )
                    for i,letter in enumerate(letters)
                ]
    
    return  CompositeVideoClip( newPosition, size=screensize ).on_color(color=WHITE).subclip(0,10)

clips = [ 
            moveLetters(letters, funcpos)
            for funcpos in [arrive]
        ]


# WE CONCATENATE EVERYTHING AND WRITE TO A FILE

final_clip = concatenate_videoclips(clips)
final_clip.write_videofile('./coolTextEffects.mp4',fps=25,codec='mpeg4')
