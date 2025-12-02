
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signatures and note lengths
time_signature = (4, 4)
note_length = 1.0 / 160  # 1 beat = 0.375 seconds (at 160 BPM)
bar_length = 4 * note_length * 4  # 4 beats per bar → 1.5 seconds per bar

# Create instruments
bass_program = Program(33, "Acoustic Bass")
piano_program = Program(0, "Acoustic Grand Piano")
drums_program = Program(0, "Acoustic Grand Piano")  # Drum kits are in percussion bank
sax_program = Program(64, "Tenor Saxophone")

bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
drums = Instrument(program=drums_program)
sax = Instrument(program=sax_program)

pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)
pm.instruments.append(sax)

# Bar 1: Drums only — kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# Time: 0.0 to 1.5 seconds (Bar 1)

# Kick on 1 and 3 (beats 0 and 2)
kick_1 = Note(36, 0.0, 0.125)
kick_3 = Note(36, 0.75, 0.125)
drums.notes.append(kick_1)
drums.notes.append(kick_3)

# Snare on 2 and 4 (beats 1 and 3)
snare_2 = Note(38, 0.375, 0.125)
snare_4 = Note(38, 1.125, 0.125)
drums.notes.append(snare_2)
drums.notes.append(snare_4)

# Hihat on every eighth note
hihat_notes = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]
for time in hihat_notes:
    hihat = Note(42, time, 0.0625)
    drums.notes.append(hihat)

# Bar 2: Bass enters with walking line in F minor, chromatic approach
# F minor = F, Gb, Ab, A, Bb, B, C, Db

# Bass line: F, Gb, Ab, A (chromatic approach to Bb)
bass_notes = [
    Note(71, 1.5, 0.375),  # F
    Note(69, 1.875, 0.375),  # Gb
    Note(67, 2.25, 0.375),  # Ab
    Note(69, 2.625, 0.375),  # A
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (comping)
# F7 = F, A, C, Eb
# Bb7 = Bb, D, F, Ab

# Bar 2: 7th chord on beat 2 (F7)
piano_notes = [
    Note(71, 2.25, 0.1875),  # F
    Note(74, 2.25, 0.1875),  # A
    Note(76, 2.25, 0.1875),  # C
    Note(71, 2.25, 0.1875),  # Eb (F7)

    # Bar 3: 7th chord on beat 4 (Bb7)
    Note(72, 3.125, 0.1875),  # Bb
    Note(76, 3.125, 0.1875),  # D
    Note(79, 3.125, 0.1875),  # F
    Note(71, 3.125, 0.1875),  # Ab
]
piano.notes.extend(piano_notes)

# Bar 2-3: Drums continue with kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# Bar 2: from 1.5 to 3.0
# Bar 3: from 3.0 to 4.5

# Apply same pattern as Bar 1
# Kick on 1 and 3 (beats 0 and 2 of the bar)
kick_1_bar2 = Note(36, 1.5, 0.125)
kick_3_bar2 = Note(36, 2.25, 0.125)
drums.notes.append(kick_1_bar2)
drums.notes.append(kick_3_bar2)

# Snare on 2 and 4
snare_2_bar2 = Note(38, 1.875, 0.125)
snare_4_bar2 = Note(38, 2.625, 0.125)
drums.notes.append(snare_2_bar2)
drums.notes.append(snare_4_bar2)

# Hihat on every eighth note
hihat_notes_bar2 = [1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125]
for time in hihat_notes_bar2:
    hihat = Note(42, time, 0.0625)
    drums.notes.append(hihat)

# Kick on 1 and 3 of Bar 3
kick_1_bar3 = Note(36, 3.0, 0.125)
kick_3_bar3 = Note(36, 3.75, 0.125)
drums.notes.append(kick_1_bar3)
drums.notes.append(kick_3_bar3)

# Snare on 2 and 4
snare_2_bar3 = Note(38, 3.375, 0.125)
snare_4_bar3 = Note(38, 4.125, 0.125)
drums.notes.append(snare_2_bar3)
drums.notes.append(snare_4_bar3)

# Hihat on every eighth note
hihat_notes_bar3 = [3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125]
for time in hihat_notes_bar3:
    hihat = Note(42, time, 0.0625)
    drums.notes.append(hihat)

# Bar 2: Sax starts on beat 2 with a short, moody motif in F minor
# F minor: F, Ab, A, Bb

# First note: F (beat 2)
note_f = Note(71, 2.25, 0.5)  # 0.5 seconds to give it some space

# Then a chromatic approach to Bb: A (beat 3), Bb (beat 4)
note_a = Note(69, 2.625, 0.25)
note_bb = Note(71, 3.0, 0.25)

sax.notes.extend([note_f, note_a, note_bb])

# Bar 3: Sax repeats the motif, but slightly delayed
# Repeat the same sequence, starting at beat 1 (3.0)
note_f2 = Note(71, 3.0, 0.5)
note_a2 = Note(69, 3.375, 0.25)
note_bb2 = Note(71, 3.75, 0.25)

sax.notes.extend([note_f2, note_a2, note_bb2])

# Bar 4: Sax holds the last note (Bb), while bass resolves and piano fades
note_bb3 = Note(71, 4.125, 0.375)
note_bb4 = Note(71, 4.5, 0.375)

sax.notes.extend([note_bb3, note_bb4])

# Write to MIDI file
pm.write("dante_russo_intro.mid")
print("MIDI file written: 'dante_russo_intro.mid'")
