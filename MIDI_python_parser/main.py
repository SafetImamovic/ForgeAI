import mido
from mido import Message, MidiFile, MidiTrack

melody_pitch_duration_data = [
    (72, 0.25), (75, 0.125), (79, 0.125), (84, 0.25),  # Bar 1
    (79, 0.25), (75, 0.25), (77, 0.25), (80, 0.25),   # Bar 2
    (84, 0.5), (79, 0.25), (75, 0.125), (77, 0.125),  # Bar 3
    (80, 0.5), (0, 0.25), (84, 0.25)                  # Bar 4
]


# Add some rests (silences)
rest_duration = 0.25
melody_pitch_duration_data.extend([(0, rest_duration)] * 4)

# Constants
TICKS_PER_BEAT = 480  # Standard for most DAWs
BEATS_PER_MINUTE = 120  # Tempo
SECONDS_PER_MINUTE = 60
TICKS_PER_SECOND = TICKS_PER_BEAT * BEATS_PER_MINUTE / SECONDS_PER_MINUTE

# Create a new MIDI file
mid = MidiFile(ticks_per_beat=TICKS_PER_BEAT)

# Create a new track
track = MidiTrack()

# Append the track to the MIDI file
mid.tracks.append(track)

# Convert your data into MIDI events
for note, duration in melody_pitch_duration_data:
    # If there's a silence, don't make a note event
    if note != 0:
        # Add a note on event
        track.append(Message('note_on', note=note, velocity=64, time=0))

    # Wait for the duration of the note/silence
    # We multiply by TICKS_PER_SECOND because duration is in seconds
    track.append(Message('note_off', note=note, velocity=64, time=int(duration * TICKS_PER_SECOND)))

# Save the MIDI file
mid.save('SKRILLEX.mid')
