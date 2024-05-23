import mido
from mido import MidiFile, MidiTrack

# Load MIDI file
mid = MidiFile('melody.mid')

# Constants
TICKS_PER_BEAT = mid.ticks_per_beat
BEATS_PER_MINUTE = 120
SECONDS_PER_MINUTE = 60
TICKS_PER_SECOND = TICKS_PER_BEAT * BEATS_PER_MINUTE / SECONDS_PER_MINUTE

# Extract note pitch and duration data
melody_pitch_duration_data = []
current_time = 0
for track in mid.tracks:
    for msg in track:
        current_time += msg.time
        if msg.type == 'note_on':
            if msg.velocity != 0:  # Ensure it's an actual note
                duration = msg.time / TICKS_PER_SECOND
                melody_pitch_duration_data.append((msg.note, duration))
        elif msg.type == 'note_off':
            duration = msg.time / TICKS_PER_SECOND
            melody_pitch_duration_data.append((0, duration))  # Represent silence as 0 pitch

# Output the extracted data
print("Extracted Melody Pitch Duration Data:")
print(melody_pitch_duration_data)
