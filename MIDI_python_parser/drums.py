import mido
from mido import Message, MidiFile, MidiTrack

# Create a new MIDI file
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

ticks_per_beat = mid.ticks_per_beat  # Default is 480
ticks_per_note = int(ticks_per_beat * 0.25)  # Assuming tempo is 120 bpm, this is the number of ticks for a quarter note

for note in drum_pitch_duration_data:
    if isinstance(note[0], tuple):  # If more than one note at the same time
        for n in note[0]:
            track.append(Message('note_on', note=n, velocity=note[2], time=0))
        track.append(Message('note_off', note=n, velocity=note[2], time=int(note[1]*ticks_per_note)))
    else:
        track.append(Message('note_on', note=note[0], velocity=note[2], time=0))
        track.append(Message('note_off', note=note[0], velocity=note[2], time=int(note[1]*ticks_per_note)))

# Save the MIDI file
mid.save('artb.mid')
