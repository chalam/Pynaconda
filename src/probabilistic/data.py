jabber_text = """
`Twas brillig, and the slithy toves
  Did gyre and gimble in the wabe:
All mimsy were the borogoves,
  And the mome raths outgrabe.

"Beware the Jabberwock, my son!
  The jaws that bite, the claws that catch!
Beware the Jubjub bird, and shun
  The frumious Bandersnatch!"
He took his vorpal sword in hand:
  Long time the manxome foe he sought --
So rested he by the Tumtum tree,
  And stood awhile in thought.
And, as in uffish thought he stood,
  The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
  And burbled as it came!
One, two! One, two! And through and through
  The vorpal blade went snicker-snack!
He left it dead, and with its head
  He went galumphing back.
"And, has thou slain the Jabberwock?
  Come to my arms, my beamish boy!
O frabjous day! Callooh! Callay!'
  He chortled in his joy.

`Twas brillig, and the slithy toves
  Did gyre and gimble in the wabe;
All mimsy were the borogoves,
  And the mome raths outgrabe.
"""


parker_text = """
My answers are inadequate
To those demanding day and date
And ever set a tiny shock
Through strangers asking what's o'clock;
Whose days are spent in whittling rhyme-
What's time to her, or she to Time?
"""

import re

def clean_words (text):
    return filter(lambda x: len(x) > 0, re.sub("[^A-Za-z]", " ", text).split(" "))


jabber_words = list(clean_words(jabber_text.lower()))

parker_words = list(clean_words(parker_text.lower()))

jabber_uniq = sorted(set(jabber_words))

if __name__ == '__main__':
    print('jabber_words ', jabber_words)

    print('parker_words ', parker_words)

    print('jabber_uniq ', jabber_uniq)