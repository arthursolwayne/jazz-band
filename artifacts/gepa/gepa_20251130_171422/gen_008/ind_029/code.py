
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums = Instrument(program=Program.DRUMS, is_drum=True)
bass = Instrument(program=Program.BASS, name="Marcus")
piano = Instrument(program=Program.PIANO, name="Diane")
sax = Instrument(program=Program.SAXOPHONE, name="Dante")

# Add instruments to the MIDI file
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Define time in seconds per beat
BPM = 160
beats_per_bar = 4
seconds_per_beat = 60.0 / BPM
seconds_per_bar = seconds_per_beat * beats_per_bar

# Define note durations and timing
quarter_note = seconds_per_beat
eighth_note = quarter_note / 2
sixteenth_note = quarter_note / 4

# Bar 1: Drums only — set the rhythm
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3
drum_notes = [
    # Bar 1: Kick on 1 and 3
    Note(36, 0, quarter_note),  # Kick on beat 1
    Note(36, 3 * quarter_note, quarter_note),  # Kick on beat 3

    # Snare on 2 and 4
    Note(38, 1 * quarter_note, quarter_note),  # Snare on beat 2
    Note(38, 4 * quarter_note, quarter_note),  # Snare on beat 4

    # Hihat on every eighth
    Note(42, 0, eighth_note),
    Note(42, eighth_note, eighth_note),
    Note(42, 2 * eighth_note, eighth_note),
    Note(42, 3 * eighth_note, eighth_note),
    Note(42, 4 * eighth_note, eighth_note),
    Note(42, 5 * eighth_note, eighth_note),
    Note(42, 6 * eighth_note, eighth_note),
    Note(42, 7 * eighth_note, eighth_note),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Bass, Piano, Sax enter

# Bass line: Walking line in D minor, chromatic approaches
# D Dorian: D, E, F, G, A, B, C
# Chromatic approach to each note

bass_notes = [
    # Beat 1: D (root)
    Note(62, 0, quarter_note),
    # Beat 2: C (chromatic approach to D)
    Note(60, 1 * quarter_note, quarter_note),
    # Beat 3: A (5th)
    Note(67, 2 * quarter_note, quarter_note),
    # Beat 4: B (chromatic approach to C)
    Note(69, 3 * quarter_note, quarter_note),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on beats 2 and 4 (D7, G7)
# D7 = D, F#, A, C
# G7 = G, B, D, F
# Chord on beat 2: D7
# Chord on beat 4: G7

piano_notes = [
    # D7 on beat 2
    Note(62, 1 * quarter_note, quarter_note),  # D
    Note(67, 1 * quarter_note, quarter_note),  # A
    Note(69, 1 * quarter_note, quarter_note),  # B
    Note(64, 1 * quarter_note, quarter_note),  # F#

    # G7 on beat 4
    Note(67, 3 * quarter_note, quarter_note),  # G
    Note(71, 3 * quarter_note, quarter_note),  # B
    Note(69, 3 * quarter_note, quarter_note),  # D
    Note(69, 3 * quarter_note, quarter_note),  # F (same as D for 7th)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Play a short, unresolved motif — one phrase, unresolved
# D, F#, G, A, (B?), leave it hanging
# Introduce the motif on beat 2, with a quarter note on D, then move to F#, G, A

sax_notes = [
    Note(62, 1 * quarter_note, quarter_note),  # D
    Note(67, 2 * quarter_note, eighth_note),  # G
    Note(69, 2 * quarter_note + eighth_note, eighth_note),  # A
]

for note in sax_notes:
    sax.notes.append(note)

# Write the MIDI file
pm.write("dante_intro.mid")

print("MIDI file 'dante_intro.mid' has been created.")
