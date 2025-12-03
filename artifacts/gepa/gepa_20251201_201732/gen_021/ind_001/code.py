
import pretty_midi
from pretty_midi import Note, Instrument, TimeSignature, KeySignature

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature (4/4)
time_signature = TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes.append(time_signature)

# Set key signature (D minor)
key_signature = KeySignature(key_number=1, time=0)
midi.key_signature_changes.append(key_signature)

# Define instruments
bass_program = 33  # Acoustic Bass
piano_program = 0  # Acoustic Grand Piano
drums_program = 0  # Drums
sax_program = 64  # Tenor Saxophone

# Create instruments
bass_instrument = Instrument(program=bass_program)
piano_instrument = Instrument(program=piano_program)
drum_instrument = Instrument(program=drums_program)
sax_instrument = Instrument(program=sax_program)

# Function to create a note
def note(note_number, start, end, velocity=100):
    return Note(note_number, start, end, velocity)

# Define timing for 160 BPM (6 seconds for 4 bars)
# 1 bar = 1.5 seconds
# 1 beat = 0.375 seconds
# Quarter note = 0.375s, eighth note = 0.1875s

# Bar 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1 (0.0 to 1.5s)
kick_1 = note(36, 0.0, 0.1875)
snare_2 = note(38, 0.375, 0.5625)
hihat_eighths = [note(42, 0.0, 0.1875),
                 note(42, 0.1875, 0.375),
                 note(42, 0.375, 0.5625),
                 note(42, 0.5625, 0.75),
                 note(42, 0.75, 0.9375),
                 note(42, 0.9375, 1.125),
                 note(42, 1.125, 1.3125),
                 note(42, 1.3125, 1.5)]

kick_3 = note(36, 1.125, 1.3125)

drum_instrument.notes.extend([kick_1, kick_3, snare_2] + hihat_eighths)
drum_instrument.is_drum = True

# Bar 2: Everyone comes in. Sax starts the melody.

# Bass line (Dm, walking line: D - Eb - F - G - A - Bb - C - D)
# Roots and fifths, with chromatic approach
# Note numbers: D2 (D2 is MIDI 38), Eb2 (39), F2 (41), G2 (43), A2 (45), Bb2 (46), C3 (48), D3 (50)

bar2_start = 1.5
bass_notes = [
    note(38, bar2_start, bar2_start + 0.375),  # D2
    note(39, bar2_start + 0.375, bar2_start + 0.75),  # Eb2 (chromatic approach)
    note(43, bar2_start + 0.75, bar2_start + 1.125),  # G2 (fifth of Dm)
    note(45, bar2_start + 1.125, bar2_start + 1.5),  # A2
]

bass_instrument.notes.extend(bass_notes)

# Piano comp: Open voicings, resolve on the last beat of each bar.

# Bar 2: Dm7 (D, F, A, C)
# D (MIDI 62), F (65), A (69), C (60)
piano_notes_bar2 = [
    note(62, bar2_start, bar2_start + 0.375),
    note(65, bar2_start, bar2_start + 0.375),
    note(69, bar2_start, bar2_start + 0.375),
    note(60, bar2_start, bar2_start + 0.375),
    note(62, bar2_start + 0.375, bar2_start + 0.75),
    note(65, bar2_start + 0.375, bar2_start + 0.75),
    note(69, bar2_start + 0.375, bar2_start + 0.75),
    note(60, bar2_start + 0.375, bar2_start + 0.75),
    note(62, bar2_start + 0.75, bar2_start + 1.125),
    note(65, bar2_start + 0.75, bar2_start + 1.125),
    note(69, bar2_start + 0.75, bar2_start + 1.125),
    note(60, bar2_start + 0.75, bar2_start + 1.125),
    note(62, bar2_start + 1.125, bar2_start + 1.5),
    note(65, bar2_start + 1.125, bar2_start + 1.5),
    note(69, bar2_start + 1.125, bar2_start + 1.5),
    note(60, bar2_start + 1.125, bar2_start + 1.5)
]

piano_instrument.notes.extend(piano_notes_bar2)

# Saxophone melody: A mysterious, simple phrase with space and unique rhythm
# Bar 2: Dm scale (D, Eb, F, G, A, Bb, C)
# We use a short motif: D (62) - E (64) - G (67) - rest - D (62) - Bb (66) - C (67) - rest

sax_notes_bar2 = [
    note(62, bar2_start, bar2_start + 0.25),  # D
    note(64, bar2_start + 0.25, bar2_start + 0.5),  # E
    note(67, bar2_start + 0.5, bar2_start + 0.75),  # G
    # Rest for the next eighth
    note(62, bar2_start + 1.0, bar2_start + 1.25),  # D
    note(66, bar2_start + 1.25, bar2_start + 1.5),  # Bb
]

sax_instrument.notes.extend(sax_notes_bar2)

# Bar 3: Dm7 (same voicings but resolved to Gm7 at the end of the bar)
bar3_start = 1.5

piano_notes_bar3 = [
    note(62, bar3_start, bar3_start + 0.375),
    note(65, bar3_start, bar3_start + 0.375),
    note(69, bar3_start, bar3_start + 0.375),
    note(60, bar3_start, bar3_start + 0.375),
    note(62, bar3_start + 0.375, bar3_start + 0.75),
    note(65, bar3_start + 0.375, bar3_start + 0.75),
    note(69, bar3_start + 0.375, bar3_start + 0.75),
    note(60, bar3_start + 0.375, bar3_start + 0.75),
    note(62, bar3_start + 0.75, bar3_start + 1.125),
    note(65, bar3_start + 0.75, bar3_start + 1.125),
    note(69, bar3_start + 0.75, bar3_start + 1.125),
    note(60, bar3_start + 0.75, bar3_start + 1.125),
    note(64, bar3_start + 1.125, bar3_start + 1.5),  # G
    note(67, bar3_start + 1.125, bar3_start + 1.5),  # B
    note(69, bar3_start + 1.125, bar3_start + 1.5),  # D
    note(67, bar3_start + 1.125, bar3_start + 1.5),  # B (again for Gm7)
]

piano_instrument.notes.extend(piano_notes_bar3)

# Bass line (Gm7) with chromatic approach
# G (MIDI 67), Bb (69), D (72), F (74), G (67)
# Roots and fifths with chromatic motion
bar3_start = 1.5
bass_notes_bar3 = [
    note(67, bar3_start, bar3_start + 0.375),  # G2
    note(69, bar3_start + 0.375, bar3_start + 0.75),  # Bb2 (chromatic approach)
    note(72, bar3_start + 0.75, bar3_start + 1.125),  # D3 (fifth of Gm)
    note(74, bar3_start + 1.125, bar3_start + 1.5),  # F3
]

bass_instrument.notes.extend(bass_notes_bar3)

# Saxophone (Bar 3): Repeat the motif or variation
# This time we end on a question — rest on final beat
sax_notes_bar3 = [
    note(62, bar3_start, bar3_start + 0.25),  # D
    note(64, bar3_start + 0.25, bar3_start + 0.5),  # E
    note(67, bar3_start + 0.5, bar3_start + 0.75),  # G
    # Rest again
    note(62, bar3_start + 1.0, bar3_start + 1.25),  # D
    note(66, bar3_start + 1.25, bar3_start + 1.5),  # Bb
]

sax_instrument.notes.extend(sax_notes_bar3)

# Bar 4: Dm7 again, resolved on the last beat
bar4_start = 3.0
piano_notes_bar4 = [
    note(62, bar4_start, bar4_start + 0.375),
    note(65, bar4_start, bar4_start + 0.375),
    note(69, bar4_start, bar4_start + 0.375),
    note(60, bar4_start, bar4_start + 0.375),
    note(62, bar4_start + 0.375, bar4_start + 0.75),
    note(65, bar4_start + 0.375, bar4_start + 0.75),
    note(69, bar4_start + 0.375, bar4_start + 0.75),
    note(60, bar4_start + 0.375, bar4_start + 0.75),
    note(62, bar4_start + 0.75, bar4_start + 1.125),
    note(65, bar4_start + 0.75, bar4_start + 1.125),
    note(69, bar4_start + 0.75, bar4_start + 1.125),
    note(60, bar4_start + 0.75, bar4_start + 1.125),
    note(62, bar4_start + 1.125, bar4_start + 1.5),  # D
    note(65, bar4_start + 1.125, bar4_start + 1.5),  # F
    note(69, bar4_start + 1.125, bar4_start + 1.5),  # A
    note(60, bar4_start + 1.125, bar4_start + 1.5),  # C
]

piano_instrument.notes.extend(piano_notes_bar4)

# Bass line (Dm7) with chromatic approach
bass_notes_bar4 = [
    note(38, bar4_start, bar4_start + 0.375),  # D2
    note(39, bar4_start + 0.375, bar4_start + 0.75),  # Eb2
    note(43, bar4_start + 0.75, bar4_start + 1.125),  # G2
    note(45, bar4_start + 1.125, bar4_start + 1.5),  # A2
]

bass_instrument.notes.extend(bass_notes_bar4)

# Saxophone (Bar 4): End with a rest — a question, not an answer
sax_notes_bar4 = [
    note(62, bar4_start, bar4_start + 0.25),  # D
    note(64, bar4_start + 0.25, bar4_start + 0.5),  # E
    note(67, bar4_start + 0.5, bar4_start + 0.75),  # G
    # Rest on the final beat
]

sax_instrument.notes.extend(sax_notes_bar4)

# Add instruments to MIDI
midi.instruments.append(bass_instrument)
midi.instruments.append(piano_instrument)
midi.instruments.append(drum_instrument)
midi.instruments.append(sax_instrument)

# Save the MIDI file
# midi.write disabled
print("MIDI file created: 'dante_russo_intro.mid'")
