
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key (F major)
key = 'F'

# Time per bar in seconds (at 160 BPM)
bar_length = 60.0 / 160.0 * 4  # 6 seconds for 4 bars
note_length = bar_length / 8  # Each note is 1/8 note

# Function to convert note name to MIDI note number
def note_to_midi(note):
    note_map = {'C': 12, 'C#': 13, 'Db': 13, 'D': 14, 'D#': 15, 'Eb': 15,
                'E': 16, 'F': 17, 'F#': 18, 'Gb': 18, 'G': 19, 'G#': 20, 'Ab': 20,
                'A': 21, 'A#': 22, 'Bb': 22, 'B': 23}
    return note_map[note]

# Define your saxophone motif (F, G, A, Bb, Bb, A, G, F)
sax_notes = [note_to_midi(n + key) for n in ['F', 'G', 'A', 'Bb', 'Bb', 'A', 'G', 'F']]
sax_times = [i * note_length for i in range(len(sax_notes))]
sax_velocity = 100

# Create saxophone instrument
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)
for note, time in zip(sax_notes, sax_times):
    sax.notes.append(pretty_midi.Note(velocity=sax_velocity, pitch=note, start=time, end=time + note_length))
pm.instruments.append(sax)

# Drums (Little Ray)
drum_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
drums = pretty_midi.Instrument(program=drum_program)

# Kick on 1 & 3 of each bar
for bar in range(4):
    kick_time = bar * bar_length + 0.0  # beat 1
    kick_time2 = bar * bar_length + 0.75  # beat 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_time2, end=kick_time2 + 0.1))

# Snare on 2 & 4 of each bar
for bar in range(4):
    snare_time = bar * bar_length + 0.375  # beat 2
    snare_time2 = bar * bar_length + 1.125  # beat 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_time2, end=snare_time2 + 0.1))

# Hi-hat on every 8th note
for bar in range(4):
    for i in range(8):
        hihat_time = bar * bar_length + i * note_length
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05))
pm.instruments.append(drums)

# Bass (Marcus) — walking line with chromatic tension in F major
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)

# Walking line in F major with chromatic tension
bass_notes = [note_to_midi(n + key) for n in ['F', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F#', 'G', 'Ab', 'A', 'Bb']]
bass_times = [i * note_length for i in range(len(bass_notes))]
bass_velocity = 80

for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=bass_velocity, pitch=note, start=time, end=time + note_length))
pm.instruments.append(bass)

# Piano (Diane) — comping on 2 and 4 with 7th chords
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)

# 7th chords on 2 and 4 of each bar
chords = {
    2: [note_to_midi(n + key) for n in ['F', 'A', 'C', 'Eb']],  # F7
    4: [note_to_midi(n + key) for n in ['G', 'B', 'D', 'F']],  # G7
}

for bar in range(4):
    # On beat 2
    chord_notes = chords[2]
    time = bar * bar_length + 0.375
    for note in chord_notes:
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))
    # On beat 4
    chord_notes = chords[4]
    time = bar * bar_length + 1.125
    for note in chord_notes:
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))
pm.instruments.append(piano)

# Save the MIDI file
pm.write('jazz_intro.mid')
print("MIDI file saved as 'jazz_intro.mid'")
