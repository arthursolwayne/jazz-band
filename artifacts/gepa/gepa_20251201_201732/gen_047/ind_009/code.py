
import pretty_midi
from pretty_midi import note_number_to_name, Note, Instrument, Program

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.resolution = 480  # 480 ticks per beat

# Set tempo to 160 BPM
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0, ticks=0)]
pm.tempos = [pretty_midi.TempoChange(tempo=160.0, time=0.0)]

# Create a new track for each instrument
drums_program = pretty_midi.Instrument(program=10, is_drum=True)
bass_program = pretty_midi.Instrument(program=33)
piano_program = pretty_midi.Instrument(program=0)
sax_program = pretty_midi.Instrument(program=64)

pm.instruments = [drums_program, bass_program, piano_program, sax_program]

# BPM = 160 ⇒ beat = 0.375s ⇒ 1 bar = 6.0s
# So each beat is 480 * 0.375 = 180 ticks

# --- DRUMS: Little Ray (Bar 1) --------------------------------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: sparse, soft, eerie
# Drums start at time=0.0 (Bar 1)
# Kick on 1 and 3
kick = Note(36, 60, 0.0, 0.375)  # Kick on downbeat
drums_program.notes.append(kick)

# Hi-hats on every eighth
# Bar 1: 8 notes, starts at 0.0
for i in range(8):
    hihat = Note(42, 60, i * 0.1875, 0.1875)
    drums_program.notes.append(hihat)

# --- BASS: Marcus (Bar 2) --------------------------------------------
# Walking line: D2 (38), G2 (43), with chromatic approaches and roots/fifths
# Bar 2: start at 1.5s (bar=1.5)
# Root: F (65), fifths: C (60)
# Chromatic approaches: E♭ (61), G♭ (62)

# Bar 2, beat 1: F (65)
note = Note(65, 64, 1.5, 0.375)
bass_program.notes.append(note)

# Bar 2, beat 2: E♭ (61) - chromatic approach
note = Note(61, 64, 1.875, 0.375)
bass_program.notes.append(note)

# Bar 2, beat 3: C (60) - fifth
note = Note(60, 64, 2.25, 0.375)
bass_program.notes.append(note)

# Bar 2, beat 4: G♭ (62) - chromatic approach
note = Note(62, 64, 2.625, 0.375)
bass_program.notes.append(note)

# --- PIANO: Diane (Bar 3) --------------------------------------------
# Open voicings, different chord each bar, resolve on last
# Bar 3: Fm7 (F, A♭, C, E♭), then Fm7 → G♭7 → C7
# Chords: Fm7 (bar 3), G♭7 (bar 4), C7 (bar 4)
# Comp on beats 2 and 4

# Bar 3
# Fm7: F (65), A♭ (60), C (60), E♭ (61) — open voicing
note = Note(65, 96, 3.0, 0.1875)  # F
note2 = Note(60, 96, 3.0, 0.1875)  # A♭
note3 = Note(60, 96, 3.0, 0.1875)  # C
note4 = Note(61, 96, 3.0, 0.1875)  # E♭
piano_program.notes.append(note)
piano_program.notes.append(note2)
piano_program.notes.append(note3)
piano_program.notes.append(note4)

# Bar 3, beat 2: G♭7 (G♭, B♭, D♭, F)
note = Note(62, 96, 3.75, 0.1875)  # G♭
note2 = Note(62, 96, 3.75, 0.1875)  # B♭
note3 = Note(61, 96, 3.75, 0.1875)  # D♭
note4 = Note(65, 96, 3.75, 0.1875)  # F
piano_program.notes.append(note)
piano_program.notes.append(note2)
piano_program.notes.append(note3)
piano_program.notes.append(note4)

# Bar 3, beat 4: C7 (C, E, G, B♭)
note = Note(60, 96, 4.5, 0.1875)  # C
note2 = Note(64, 96, 4.5, 0.1875)  # E
note3 = Note(67, 96, 4.5, 0.1875)  # G
note4 = Note(62, 96, 4.5, 0.1875)  # B♭
piano_program.notes.append(note)
piano_program.notes.append(note2)
piano_program.notes.append(note3)
piano_program.notes.append(note4)

# --- SAX: Dante (Bar 4) --------------------------------------------
# One short motif — incomplete, expressive, leaves it hanging
# Bar 4: F (65), A♭ (60), G♭ (62), E♭ (61) — a question

# F (65) on beat 1
note = Note(65, 100, 4.5, 0.375)
sax_program.notes.append(note)

# A♭ (60) on beat 2
note = Note(60, 100, 4.875, 0.375)
sax_program.notes.append(note)

# G♭ (62) on beat 3
note = Note(62, 100, 5.25, 0.375)
sax_program.notes.append(note)

# E♭ (61) on beat 4 — leaves it hanging
note = Note(61, 96, 5.625, 0.375)
sax_program.notes.append(note)

# Save the MIDI file
pm.write("dante_intro.mid")
