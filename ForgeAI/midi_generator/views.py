from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from .models import Chat
from payments.models import CheckoutSessionRecord
import google.generativeai as genai
import os
from . import midi_gen
from . import cloud_storage
from google.cloud import storage

genai.configure(api_key=os.environ['GENAI_API_KEY'])
model = genai.GenerativeModel(model_name='gemini-1.5-pro')



midi_prompts = ["""I need assistance in producing AI-generated text
    that I convert to music using MIDI files. Initially,
    I'll provide a description of the format I need for
    the textual representation of the music.
    Since music is a time-based art form,
    the notes follow each other in time, and
    sometimes there are no notes, that is, silences.
    The way I would like you to generate them is as
    follows:
    Each note is represented as a tuple of two
    elements:
    The pitch of the note (integer value).
    Because I will use this text representation and
    convert to MIDI the note should be a number
    from 21 (that is note A0 - 27,50 Hz) to 96 (that is
    C7 - 2093 hz) so use these numbers to represent
    the note.
    The duration of the note (float value)
    represented as:
    0.125 for an eighth note
    0.25 for a quarter note
    0.5 for a half note
    1 for a whole note
    2 for a double whole note
    But could be any number between 0 and 2,
    bocouse you know, musician are creative so why
    not 0.29 or 1.22, etc.
    With this format i need you generate a text that
    i will covert in music in this format:
    melody_pitch_duration_data = [
    (note, duration), (note, duration), (note,
    duration),
    etc,
    ]
    And when there is a silence the note should be 0
    and the duration is how long is that silence.
    A melody is a linear sequence of notes that the
    listener hears as a single entity. It is the
    foreground to the backing elements and is a
    combination of pitch and rhythm. Sequences of
    notes that comprise melody are musically
    satisfying and are often the most memorable
    part of a song.
    There are many ways to describe a melody. Here
    are a few:
    ● Pitch: The pitch of a melody is the relative
    highness or lowness of the notes. Melodies
    can be high, low, or somewhere in between.
    ● Rhythm: The rhythm of a melody is the
    pattern of long and short notes. Melodies can
    have a slow, steady rhythm, a fast,
    syncopated rhythm, or something in
    between.
    ● Intervals: Intervals are the distance between
    notes. Melodies can use a variety of
    intervals, from small steps to large leaps.
    ● Contour: The contour of a melody is the
    overall shape of the melody. Melodies can be
    ascending, descending, or something in
    between.
    ● Tonal center: The tonal center of a melody is
    the note that the melody feels like it is
    centered around. Melodies can have a strong
    tonal center, a weak tonal center, or no tonal
    center at all.
    When describing a melody, it is important to
    consider all of these factors. The pitch, rhythm,
    intervals, contour, and tonal center all
    contribute to the overall sound of the melody.
    Here are some examples of how to describe
    melodies:
    ● The melody of "Happy Birthday" is simple and
    repetitive, with a clear tonal center.
    ● The melody of "Yesterday" by The Beatles is
    more complex, with a variety of intervals and
    a changing tonal center.
    ● The melody of "Bohemian Rhapsody" by
    Queen is highly dramatic, with a wide range
    of pitches and rhythms.
    Quality melodies typically limit their range to
    about an octave-and-a-half, feature repeating
    elements like melodic intervals and rhythmic
    patterns, and consist of stepwise motion with
    occasional energetic leaps. Good melodies also
    interact meaningfully with the bass line,
    employing a mix of parallel, similar, oblique, or
    contrary motions for a dynamic, counter melodic
    effect. Finally, a standout melody tends to have
    a climactic moment, often a high note with
    significant harmonization and strong rhythmic
    placement, which then descends to a restful
    cadence.
    No matter how it is described, a melody is one of
    the most important elements of music. It is what
    gives a song its identity and makes it memorable.
    Please note that AI-generated music may not
    sound pleasing as it is randomly generated so we
    will use music theory but not random math so
    don't randomize the generation process. take
    into account musical concepts like scales,
    modes, etc.
    Now that you have a full understanding of the
    text representation, we will create some
    awesome music!
    when writing the response, do not 
    DON'T write python after the ```
    keep the midi to a maximum of 4 bars long every time just 4 bars exactly
    please make the melody be very interesting without it just going up and down
    don't make the melody just go up and down
    don't use too many distinct notes, don't make the notes be too far apart
    you can have the same note repeat mutliple times in a row like in a baseline if needed
    you can even come up with fairly simple melodies even using just 2 notes
    after the midi add some text explaining the melody
    The next message is the actual prompt: 
""", """
I need assistance in producing AI-generated text
that I convert to music using MIDI files. Initially,
I'll provide a description of the format I need for
the textual representation of the music.
Since music is a time-based art form,
the notes follow each other in time, and
sometimes there are no notes, that is, silences.
Here I need you to generate Chords, so, more
than one note each time, could be 2, 3, 4, etc.
The way I would like you to generate them is as
follows:
Each chord is represented these elements:
The pitches of the notes (integer values).
Because I will use this text representation and
convert to MIDI the note should be a number
from 21 (that is note A0 - 27,50 Hz) to 96 (that is
C7 - 2093 hz) so use these numbers to represent
the note.
The duration of the note (float value)
represented as:
0.125 for an eighth note
0.25 for a quarter note
0.5 for a half note
1 for a whole note
2 for a double whole note
But it could be any number between 0 and 2,
because you know, musicians are creative so why
not 0.29 or 1.22, etc.
With this format i need you generate a text that
i will covert in music in this format:
chords_pitch_duration_data = [
((note, note, note), duration), ((note,note),
duration), (note, duration),
etc,
]
And when there is a silence the note should be 0
and the duration is how long is that silence.
The key is Harmony is that is the vertical aspect
of music, or the combination of different pitches
sounding at the same time. Chords are the
building blocks of harmony, and they are made
up of two or more notes that are played
together.
The simplest type of chord is a two-note chord,
also known as a diatonic chord. Diatonic chords
are made up of two notes that are next to each
other on the musical scale. For example, a C
major chord is made up of the notes C and E.
Three-note chords are also known as triads.
Triads are made up of a root note, a third, and a
fifth. The root note is the lowest note in the
chord, the third is the note that is two semitones
above the root, and the fifth is the note that is
seven semitones above the root. For example, a
C major triad is made up of the notes C, E, and
G.
Four-note chords are also known as seventh
chords. Seventh chords are made up of a root
note, a third, a fifth, and a seventh. The seventh
note can be either major or minor. For example,
a C major seventh chord is made up of the notes
C, E, G, and B.
And you also have:
Sus chords: Sus chords are made up of a root
note, a third, and a fifth, but the third is
replaced with a suspended fourth or second. For
example, a Csus4 chord is made up of the notes
C, F, and G.
Add chords: Add chords are made up of a root
note, a third, a fifth, and an additional note. For
example, a Cadd9 chord is made up of the notes
C, E, G, and B.
Augmented chords: Augmented chords are made
up of a root note, a major third, and a perfect
fifth. For example, a C augmented chord is made
up of the notes C, E#, and G#.
diminished chords: Diminished chords are made
up of a root note, a minor third, and a
diminished fifth. For example, a C diminished
chord is made up of the notes C, Eb, and Gb.
Harmony is an important part of music, and it
can be used to create a variety of different
moods and emotions. For example, major chords
are often used to create a sense of happiness or
joy, while minor chords are often used to create
a sense of sadness or melancholy.
Please note that AI-generated music may not
sound pleasing as it is randomly generated so we
will use music theory but not random math so
don't randomize the generation process. take
into account musical concepts like scales,
modes, etc.
Now that you have a full understanding of the
text representation, we will create some
awesome music!
when writing the response, do not 
DON'T write python after the ```
keep the midi to a maximum of 4 bars long every time just 4 bars exactly\
add additional text explaining the chords midi
The next message is the actual prompt: 
""", """
I need assistance in producing AI-generated text
that I convert to music using drum MIDI files.
Initially, I'll provide a description of the format I
need for the textual representation of the music.
I need to generate rhythm.
Since music is a time-based art form,
the notes follow each other in time, and
sometimes there are no notes, that is, silences.
The way I would like you to generate them is as
follows:
Each note is represented with three elements:
The element of the drumset (integer value) and
The duration of the note (float value) and
The velocity (so how strong the drum element
will sound):
For drum the notes will be:
27 High Q (GM2)
28 Slap (GM2)
29 Scratch Push (GM2)
30 Scratch Pull (GM2)
31 Sticks (GM2)
32 Square Click (GM2)
33 Metronome Click (GM2)
34 Metronome Bell (GM2)
35 Bass Drum 2
36 Bass Drum 1
37 Side Stick
38 Snare Drum 1
39 Hand Clap
40 Snare Drum 2
41 Low Tom 2
42 Closed Hi-hat
43 Low Tom 1
44 Pedal Hi-hat
45 Mid Tom 2
46 Open Hi-hat
47 Mid Tom 1
48 High Tom 2
49 Crash Cymbal 1
50 High Tom 1
51 Ride Cymbal 1
52 Chinese Cymbal
53 Ride Bell
54 Tambourine
55 Splash Cymbal
56 Cowbell
57 Crash Cymbal 2
58 Vibra Slap
59 Ride Cymbal 2
60 High Bongo
61 Low Bongo
62 Mute High Conga
63 Open High Conga
64 Low Conga
65 High Timbale
66 Low Timbale
67 High Agogo
68 Low Agogo
69 Cabasa
70 Maracas
71 Short Whistle
72 Long Whistle
73 Short Guiro
74 Long Guiro
75 Claves
76 High Wood Block
77 Low Wood Block
78 Mute Cuica
79 Open Cuica
80 Mute Triangle
81 Open Triangle
82 Shaker (GM2)
83 Jingle Bell (GM2)
84 Belltree (GM2)
85 Castanets (GM2)
86 Mute Surdo (GM2)
87 Open Surdo (GM2)
The duration of the note (float value)
represented as:
0.125 for an eighth note
0.25 for a quarter note
0.5 for a half note
1 for a whole note
2 for a double whole note
But it could be any number between 0 and 2,
because you know, musicians are creative so why
not 0.29 or 1.22, etc.
And when there is a silence the note should be 0
and the duration is how long is that silence.
Feel free to use intricate durations and notes.
And the velocity is from 0 to 127
SO what i need is:
drum_pitch_duration_data = [
((note, note), duration, velocity), (note,
duration, velocity), (note,note, note), duration,
velocity),...,
etc,
]
So, in the same moment it could be one or more
than one element in the drum pattern or a
silence or just one element, or two, or more.
The time signature of a piece of music tells you
how many beats are in each measure and what
kind of note gets one beat. The most common
time signatures are 4/4 and 3/4.
In 4/4 time, there are four beats in each
measure and each beat is a quarter note. This
means that a measure of 4/4 is four quarter
notes long.
In 3/4 time, there are three beats in each
measure and each beat is a quarter note. This
means that a measure of 3/4 is three quarter
notes long.
The difference between 4/4 and 3/4 is the
number of beats in each measure. 4/4 has four
beats per measure, while 3/4 has three beats
per measure. This difference in the number of
beats can affect the feel of the music. 4/4 is
often used in music that is upbeat and energetic,
while 3/4 is often used in music that is slower
and more relaxed.
The time signature of a piece of music can also
affect the way that the drums are played. In 4/4
time, the drums are often played on the beats 1,
2, 3, and 4. In 3/4 time, the drums are often
played on the beats 1, 2, and 3.
There are many other time signatures besides
4/4 and 3/4. Here are a few examples: 2/4 (fast
upbeat), 6/8 (folk-inspired), 9/8 (Middle Eastern
or Indian inspired), 12/8 (jazz-inspired)
Now that you have a full understanding of the
text representation, we will create some
awesome drum patterns!
when writing the response, do not 
DON'T write python after the ```
keep the midi to a maximum of 4 bars long every time just 4 bars exactly
write additional text explaining the drum midi
The next message is the actual prompt: 
"""
]

def ask_gemini(message):
    response = model.generate_content(message)
    
    return response.text

def data_to_midi(data):
    start_idx = data.find("[")
    end_idx = data.find("]")

    if start_idx == -1 or end_idx == -1:
        raise ValueError("MIDI data not found in the provided text.")

    midi_data = data[start_idx: end_idx + 1]
    return midi_data

def data_to_text(data):
    start_idx = data.find("]")
    if start_idx == -1:
        return data

    text_data = data[start_idx:]
    text_data = text_data.replace("]", "")
    text_data= text_data.replace("`", "")

    return text_data.strip()

def sessions(request):
    if not request.user.is_authenticated:
        return redirect('account_login')

    try:
        record = CheckoutSessionRecord.objects.get(user=request.user)
    except CheckoutSessionRecord.DoesNotExist:
        return redirect('subscribe')
    
    if not record.has_access:
        return redirect('subscribe')
    
    
    current_file_path = os.path.abspath(__file__)

    # Get the parent directory path
    parent_directory_path = os.path.dirname(current_file_path)
    parent_parent_directory_path = os.path.dirname(parent_directory_path)
    
    chats = Chat.objects.filter(user=request.user).order_by('created_at')
    index = 0;
    
    
    if request.method == 'POST':
        index = int(request.POST.get('choice'))

        print("INDEX: ", index)
        
        message = request.POST.get('message')
        messageTest = str(midi_prompts[index]) + str(message)
        response = ask_gemini(messageTest)
        print(response)
        
        responseNoMidi = data_to_text(response)
        responseMidi = data_to_midi(response)
        
        type=''
        if index == 0:
            type='Melody'
        elif index == 1:
            type='Chords'
        elif index == 2:
            type='Drums'
        
        chat = Chat(user=request.user, message=message, response=responseNoMidi, created_at=timezone.now(), type=type)
        id = chat.save()
    
        if index == 0:
            midi_gen.create_melody(responseMidi, id)
        elif index == 1:
            midi_gen.create_chords(responseMidi, id)
        elif index == 2:
            midi_gen.create_drums(responseMidi, id)
        
        path = parent_parent_directory_path+'\\'+str(id)+'.mid'
        cloud_storage.upload_to_bucket(str(id)+'.mid', path, "midi-files-forge-ai")
        link = cloud_storage.generate_signed_url(str(id)+'.mid', "midi-files-forge-ai")
        
        instance = Chat.objects.get(id=id)
        instance.midi_link = link
        instance.save()
        
        print(link)
        print(responseMidi)
        print(responseNoMidi)
        
        return JsonResponse({'message': message, 'response': responseNoMidi, 'link': link, 'id': id, 'index': index, 'type': type})

    
    context = {'chats': chats, 'record': record}
    return render(request, 'sessions.html', context)
