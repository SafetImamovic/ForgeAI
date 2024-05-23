from midiutil.MidiFile import MIDIFile

chords_pitch_duration_data = [
    ((60, 64, 67), 1),     # C major chord for 1 whole note duration
    ((64, 67, 71), 1),     # E minor chord for 1 whole note duration
    ((67, 71, 74), 1),     # G major chord for 1 whole note duration
    ((65, 69, 72), 1),     # F major chord for 1 whole note duration
]


midi_file = MIDIFile(1)

tempo = 120
midi_file.addTempo(0, 0, tempo)

instrument = 0  # Acoustic Grand Piano
midi_file.addProgramChange(0, 0, 0, instrument)

channel = 0
volume = 80

# Add chord notes
current_time = 0
for chord_pitches, duration in chords_pitch_duration_data:
    if isinstance(chord_pitches, int) and chord_pitches == 0:
        current_time += duration
        continue
    for pitch in chord_pitches:
        midi_file.addNote(track=0, channel=channel, pitch=pitch, time=current_time, duration=duration, volume=volume)
    current_time += duration

with open("SKRILLEX_CHORDS.mid", "wb") as output_file:
    midi_file.writeFile(output_file)
