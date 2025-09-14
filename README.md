Project: Warhol-inspired photo grid

Author: Logan Mulkerin
This code was produced for CSCI 3725 - Computational Creativity - at Bowdoin College.
Last code changes: 9/14/2025

Brief overview: This project produces a grid of images, in an Andy Warhol inspired neon print.

Set-up:
- I used a package called rembg to remove image backgrounds. This must be installed with 'pip install rembg'
- rembg depends on onnxruntime, which can be installed with 'pip install onnxruntime'
- To tint images, I used PIL. To display images, I used numpy. Both must be installed (if they're not already).
- All images used in generation are stored in /CC_M1/assets.
    - I used 16 images, so if you'd like to use this project to generate grids of your own, just swap out my pictures with 16 images of yourself (or whoever your subject is). Format shouldn't matter - mine are all varied.
- The grid size (images by images) is determined on line 43 of main.py, in the call to generate_grid. Feel free to alter this.
- The colors used are in transition_matrices.py. Lots of standard colors can be added!
- The bulk of code functinality lives in pick_image_and_color.py
- Run from main.py

Personal meaning:
You have probably seen Andy Warhol's famous Marilyn Monroe paintings. In them, she is portrayed repeatedly in 
different color palettes, side by side. There are several possible interpretations of these paintings, including the 
commodification of beauty, the fleeting nature of fame, and vulnerability. I've always liked the second; it feels to 
me that the repetition of the same image almost drains the life from it, despite all of the neon and bold in the 
photos. The paintings have always read to me as panicked, representing the fleeting nature of fame, and also, of life.
These are conversations I used to have with my mother, who loved analyzing all art non-academically. I was encouraged
to ask not what art objectively means, but what it looks like to me. Having lost my mom two years ago, these 
conversations are all-important.
I think part of the young adult experience is realizing that one is not all that different from their parents, within
reason. This is amplified with grief and loss. Sometimes, a sentence comes out of my mouth and I think "Oh, rats,
I'm just like my mom," and yet, there is some relief in that.
Another crucial part of the human experience is the passage of time. Wait, I'm 21? I was last in high school three
years ago? Covid started over five years ago? 2016 was almost a decade ago?
I wanted a project tying these feelings together, as I become nostalgic (this seems to happen every fall). I wanted a
project representing that "oh, I'm an adult now, and I'm just like my parents? I was a kid yesterday?" feeling, in
one snapshot. Because of the fleetingness of Andy Warhols paintings, this seemed like a perfect style.
I decided to use many photos of myself from over the years, to contrast them but also tie them together across 20
years, and a transition. They begin to blur together, I think in a way that captures the feeling I've just described.
I also carefully chose two photos of my mom, for similar reasons. They blend into the sea of neon until you look
closely at each image, much like subtle mannerisms acted out day to day that I think nothing of, until I realize
they didn't come from nowhere.
This project is not useful - it's not a T-shirt design, a golf course, or anything that could help me write a
screenplay. It's only thought-provoking.

Challenges:
Having not worked much with images, this project quite challenged me. Last week, when we generated grids of dance
moves, I had a hard time wrapping my head around image objects versus paths versus a grid of images versus a plot
versus a literal displayed image, so I knew I wanted to get some more work with photos. This project was perfect 
for that goal.
Namely, this project gave me important experience working with external libraries to modify and display images. I
think that working with a library you've never seen before and sort of experimenting until it works provides
valuable critical thinking experience that will extend far beyond just "let's see if I can remove an image background"
Going forward, it would be interesting to see if I could implement something similar to a library I used. For
example, it would be interesting to see if I could create an image background remover that perhaps works better than
the one I used (you may notice some flaws, such as one photo where a clock is left in the background, or others
where my neck and shoulders are removed).

Creativity:
In a literal sense, my project is creative. Run the code, and it creates a unique grid of images and colors that has
different appeal eah time (for example, whole columns of solid colors gives the image a different effect than 
scrambled disco-floor-style grids). I think this qualifies as creative, in that it is creating.