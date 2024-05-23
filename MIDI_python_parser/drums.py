import mido
from mido import Message, MidiFile, MidiTrack

drum_pitch_duration_data = [
    ((36,), 0.125, 127),  # Bass Drum 1
    ((38, 44), 0.25, 110),  # Snare Drum 1 + Pedal Hi-hat
    ((38,), 0.125, 115),  # Snare Drum 1
    ((36,), 0.1875, 127),  # Bass Drum 1
    ((40,), 0.125, 120),  # Snare Drum 2
    ((38, 44), 0.25, 127),  # Snare Drum 1 + Pedal Hi-hat
    ((51,), 0.375, 115),  # Ride Cymbal 1
    ((40, 44), 0.125, 120),  # Snare Drum 2 + Pedal Hi-hat
    ((38,), 0.25, 115),  # Snare Drum 1
    ((36,), 0.375, 127),  # Bass Drum 1
    ((48, 49), 0.125, 120),  # High Tom 2 + Crash Cymbal 1
    ((36, 42), 0.1875, 127),  # Bass Drum 1 + Closed Hi-hat
    ((51,), 0.375, 115),  # Ride Cymbal 1
    ((38, 44), 0.125, 120),  # Snare Drum 1 + Pedal Hi-hat
    ((51,), 0.125, 115),  # Ride Cymbal 1
    ((40,), 0.125, 120),  # Snare Drum 2
    ((38, 44), 0.375, 127),  # Snare Drum 1 + Pedal Hi-hat
    ((36, 49), 0.25, 127),  # Bass Drum 1 + Crash Cymbal 1
    ((40, 44), 0.125, 120),  # Snare Drum 2 + Pedal Hi-hat
    ((36,), 0.25, 115),  # Bass Drum 1
    ((38,), 0.375, 127),  # Snare Drum 1
    ((51, 49), 0.125, 120),  # Ride Cymbal 1 + Crash Cymbal 1
    ((38, 44), 0.1875, 127),  # Snare Drum 1 + Pedal Hi-hat
    ((51,), 0.375, 115),  # Ride Cymbal 1
    ((36, 44), 0.125, 120),  # Bass Drum 1 + Pedal Hi-hat
    ((51,), 0.125, 115),  # Ride Cymbal 1
    ((38,), 0.125, 120),  # Snare Drum 1
    ((51, 44), 0.375, 127),  # Ride Cymbal 1 + Pedal Hi-hat
    ((38, 49), 0.25, 127),  # Snare Drum 1 + Crash Cymbal 1
]

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
