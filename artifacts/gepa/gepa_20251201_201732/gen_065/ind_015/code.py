
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signatures (4/4)
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
pm.time_signature_changes = [time_signature]

# Define key signature (F minor)
key_signature = pretty_midi.KeySignature(key_number=19, time=0)
pm.key_signature_changes = [key_signature]

# Define the duration of a bar in seconds (160 BPM, 4/4 time)
bar_duration = 60.0 / 160 * 4  # 6 seconds for 4 bars

# Define the start times for each bar
bar_start_times = [0, 0.75, 1.5, 2.25]  # in seconds (each bar is 1.5 seconds)

# ------------------------
# 1. Drums (Little Ray)
# ------------------------

drums = Instrument(program=Program(0), is_drum=True)
pm.instruments.append(drums)

# Kick on 1 and 3
kick_notes = [
    Note(36, 0.0, 0.25),  # Bar 1, beat 1
    Note(36, 1.5, 1.75),  # Bar 2, beat 1
    Note(36, 3.0, 3.25),  # Bar 3, beat 1
    Note(36, 4.5, 4.75),  # Bar 4, beat 1
]

# Snare on 2 and 4
snare_notes = [
    Note(38, 0.75, 0.90),  # Bar 1, beat 2
    Note(38, 1.5 + 0.75, 1.5 + 0.90),  # Bar 2, beat 2
    Note(38, 3.0 + 0.75, 3.0 + 0.90),  # Bar 3, beat 2
    Note(38, 4.5 + 0.75, 4.5 + 0.90),  # Bar 4, beat 2
]

# Hi-hat on every eighth note
for bar in range(4):
    for i in range(8):  # 8 eighths per bar
        start = bar_start_times[bar] + i * 0.375
        end = start + 0.1  # 0.1 sec duration
        hats = Note(42, start, end)
        drums.notes.append(hats)

# Add kick and snare
for note in kick_notes + snare_notes:
    drums.notes.append(note)

# ------------------------
# 2. Bass (Marcus)
# ------------------------

bass = Instrument(program=Program(33))
pm.instruments.append(bass)

# Walking bass line in Fm: F - G - Ab - A - Bb - B - C - Db
# Transpose to MIDI notes
bass_notes = [
    Note(44, 0.0, 0.375),  # F
    Note(45, 0.375, 0.75),  # G
    Note(46, 0.75, 1.125),  # Ab
    Note(47, 1.125, 1.5),  # A
    Note(48, 1.5, 1.875),  # Bb
    Note(49, 1.875, 2.25),  # B
    Note(50, 2.25, 2.625),  # C
    Note(51, 2.625, 3.0),  # Db
    Note(44, 3.0, 3.375),  # F
    Note(45, 3.375, 3.75),  # G
    Note(46, 3.75, 4.125),  # Ab
    Note(47, 4.125, 4.5),  # A
    Note(48, 4.5, 4.875),  # Bb
    Note(49, 4.875, 5.25),  # B
    Note(50, 5.25, 5.625),  # C
    Note(51, 5.625, 6.0),  # Db
]

for note in bass_notes:
    bass.notes.append(note)

# ------------------------
# 3. Piano (Diane)
# ------------------------

piano = Instrument(program=Program(0))
pm.instruments.append(piano)

# Bar 1: Fm7 (F - Ab - C - Eb)
# Bar 2: Am7 (A - C - E - G)
# Bar 3: D7 (D - F# - A - C)
# Bar 4: Gm7 (G - Bb - D - F)

# Bar 1: Fm7
note1 = Note(53, 0.0, 0.75)  # F
note2 = Note(55, 0.0, 0.75)  # Ab
note3 = Note(57, 0.0, 0.75)  # C
note4 = Note(58, 0.0, 0.75)  # Eb
piano.notes.extend([note1, note2, note3, note4])

# Bar 2: Am7
note5 = Note(57, 1.5, 2.25)  # A
note6 = Note(59, 1.5, 2.25)  # C
note7 = Note(61, 1.5, 2.25)  # E
note8 = Note(62, 1.5, 2.25)  # G
piano.notes.extend([note5, note6, note7, note8])

# Bar 3: D7
note9 = Note(62, 3.0, 3.75)  # D
note10 = Note(64, 3.0, 3.75)  # F#
note11 = Note(66, 3.0, 3.75)  # A
note12 = Note(67, 3.0, 3.75)  # C
piano.notes.extend([note9, note10, note11, note12])

# Bar 4: Gm7
note13 = Note(67, 4.5, 5.25)  # G
note14 = Note(69, 4.5, 5.25)  # Bb
note15 = Note(71, 4.5, 5.25)  # D
note16 = Note(72, 4.5, 5.25)  # F
piano.notes.extend([note13, note14, note15, note16])

# ------------------------
# 4. Tenor Sax (You)
# ------------------------

sax = Instrument(program=Program(64))
pm.instruments.append(sax)

# Your motif: Start with a whisper, leave it hanging, then resolve
# The motif: F (44) - G (45) - Ab (46) - rest
# Then resolve with F (44) at the end of the 4th bar

# Bar 1: F - G - Ab (resting on the last note)
note1 = Note(44, 0.0, 0.375)  # F
note2 = Note(45, 0.375, 0.75)  # G
note3 = Note(46, 0.75, 1.125)  # Ab
sax.notes.extend([note1, note2, note3])

# Bar 2: F - G - Ab (same motif)
note4 = Note(44, 1.5, 1.875)  # F
note5 = Note(45, 1.875, 2.25)  # G
note6 = Note(46, 2.25, 2.625)  # Ab
sax.notes.extend([note4, note5, note6])

# Bar 3: F - G - Ab (same motif)
note7 = Note(44, 3.0, 3.375)  # F
note8 = Note(45, 3.375, 3.75)  # G
note9 = Note(46, 3.75, 4.125)  # Ab
sax.notes.extend([note7, note8, note9])

# Bar 4: Resolving on F (44)
note10 = Note(44, 4.5, 5.25)  # F
sax.notes.append(note10)

# ------------------------
# Save the MIDI file
# ------------------------

pm.write("jazz_intro_wayne.midi")
