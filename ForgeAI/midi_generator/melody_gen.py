import mido
from mido import Message, MidiFile, MidiTrack
import ast

def string_to_tuple_list(data_string):
    try:
        # Find the start and end of the list in the string
        start = data_string.find('[')
        end = data_string.rfind(']') + 1

        # Extract the list part of the string
        list_string = data_string[start:end]
        print(f"Extracted list string: {list_string}")  # Debug statement

        # Use ast.literal_eval to safely convert the string to an actual list
        actual_list = ast.literal_eval(list_string)

        return actual_list
    except (SyntaxError, ValueError) as e:
        print(f"Error parsing the string: {e}")
        return None

# Add some rests (silences)
def create_melody(melody_pitch_duration_data_str, name):
    melody_pitch_duration_data = string_to_tuple_list(melody_pitch_duration_data_str)
    if melody_pitch_duration_data is None:
        print("Failed to parse melody_pitch_duration_data_str")
        return

    rest_duration = 0.25
    melody_pitch_duration_data.extend([(0, rest_duration)] * 4)
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
    mid.save(str(name) + '.mid')
    print(f"MIDI file '{name}.mid' created successfully.")