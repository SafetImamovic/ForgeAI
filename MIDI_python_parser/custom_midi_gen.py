from mido import MidiFile, MidiTrack, Message, MetaMessage
import json

def json_to_midi(json_data):
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    tempo = int(60000000 / json_data["tempo"])  # Convert BPM to microseconds per beat

    track.append(MetaMessage('set_tempo', tempo=tempo))

    ticks_per_beat = midi.ticks_per_beat

    for note in json_data["notes"]:
        note_name = note["pitch"]
        duration = int(note["duration"] * ticks_per_beat)
        pitch = mido.Note(note_name).value

        track.append(Message('note_on', note=pitch, velocity=64, time=0))
        track.append(Message('note_off', note=pitch, velocity=64, time=duration))

    return midi

def main():
    json_data = {
        "name": "My Melody",
        "tempo": 120,
        "notes": [
            {"pitch": "C4", "duration": 0.5},
            {"pitch": "E4", "duration": 0.5},
            {"pitch": "G4", "duration": 0.5},
            {"pitch": "C5", "duration": 1.0},
            {"pitch": "A4", "duration": 0.5},
            {"pitch": "G4", "duration": 0.5},
            {"pitch": "E4", "duration": 1.0}
        ]
    }

    midi_file = json_to_midi(json_data)
    midi_file.save('output.mid')

if __name__ == "__main__":
    main()
