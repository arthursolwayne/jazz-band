
import pretty_midi
from pretty_midi import Note, Instrument

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Define the key: Dm (Dorian mode would be natural, but we're using Dm7 for jazz feel)
# Root note: D (MIDI 62)
# Dm7: D, F, A, C (MIDI 62, 64, 67, 69)

# Define instruments
drums = Instrument(program=0, is_drum=True, name='Drums')
bass = Instrument(program=33, name='Bass')
piano = Instrument(program=0, name='Piano')
sax = Instrument(program=64, name='Saxophone')

pm.instruments = [drums, bass, piano, sax]

# Define duration per bar (6 seconds for 4 bars)
bar_duration = 6.0 / 4
beat_duration = bar_duration / 4

# --- DRUMS: Little Ray (Bar 1) ---------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: Only hihat and kick

# Kick on 1
drums.notes.append(Note(35, 62, 0.0, 0.375))  # Kick on beat 1
# Kick on 3
drums.notes.append(Note(35, 62, 1.125, 0.375))  # Kick on beat 3

# Hihat on every eighth
for i in range(8):
    dr_start = i * (beat_duration / 2)
    dr_end = dr_start + (beat_duration / 2)
    drums.notes.append(Note(42, 80, dr_start, dr_end))  # Hihat

# --- BASS: Marcus (Bars 1-4) ---------------------
# Walking line: D2-G2 (MIDI 38-43), roots and fifths with chromatic approaches
# Bar 1: D2 (MIDI 38) + chromatic approach to F2 (MIDI 41)
# Bar 2: F2 (MIDI 41) + chromatic approach to A2 (MIDI 45)
# Bar 3: A2 (MIDI 45) + chromatic approach to C3 (MIDI 48)
# Bar 4: C3 (MIDI 48) + chromatic approach to D3 (MIDI 50)

# Bar 1
bass.notes.append(Note(38, 38, 0.0, 0.25))  # D2, quarter note
bass.notes.append(Note(40, 40, 0.0, 0.25))  # Chromatic approach to F2

# Bar 2
bass.notes.append(Note(41, 41, 1.5, 0.25))  # F2
bass.notes.append(Note(43, 43, 1.5, 0.25))  # Chromatic approach to A2

# Bar 3
bass.notes.append(Note(45, 45, 3.0, 0.25))  # A2
bass.notes.append(Note(47, 47, 3.0, 0.25))  # Chromatic approach to C3

# Bar 4
bass.notes.append(Note(48, 48, 4.5, 0.25))  # C3
bass.notes.append(Note(50, 50, 4.5, 0.25))  # Chromatic approach to D3

# --- PIANO: Diane (Bars 2-4) ---------------------
# Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C) @ MIDI 62, 64, 67, 69
# Bar 3: Gm7 (G, Bb, D, F) @ MIDI 67, 69, 72, 64
# Bar 4: C7 (C, E, B, G) @ MIDI 60, 64, 71, 67

# Bar 2: Dm7 (Play on beat 2 and 4)
piano.notes.append(Note(62, 62, 1.5, 0.5))  # D
piano.notes.append(Note(64, 64, 1.5, 0.5))  # F
piano.notes.append(Note(67, 67, 1.5, 0.5))  # A
piano.notes.append(Note(69, 69, 1.5, 0.5))  # C

# Bar 3: Gm7 (Play on beat 2 and 4)
piano.notes.append(Note(67, 67, 3.0, 0.5))  # G
piano.notes.append(Note(69, 69, 3.0, 0.5))  # Bb
piano.notes.append(Note(72, 72, 3.0, 0.5))  # D
piano.notes.append(Note(64, 64, 3.0, 0.5))  # F

# Bar 4: C7 (Play on beat 2 and 4)
piano.notes.append(Note(60, 60, 4.5, 0.5))  # C
piano.notes.append(Note(64, 64, 4.5, 0.5))  # E
piano.notes.append(Note(71, 71, 4.5, 0.5))  # B
piano.notes.append(Note(67, 67, 4.5, 0.5))  # G

# --- SAX: Dante (Bars 2-4) ---------------------
# Short motif – start, leave it hanging, come back and finish
# Melody: D (62), E (64), F (65), F# (66) – but break it up

# Bar 2: D (62), E (64), F (65)
sax.notes.append(Note(62, 62, 1.5, 0.25))  # D
sax.notes.append(Note(64, 64, 1.5, 0.25))  # E
sax.notes.append(Note(65, 65, 1.5, 0.25))  # F

# Bar 3: Rest – leave it hanging
# Bar 4: F# (66), G (67), D (62) – resolves back to D
sax.notes.append(Note(66, 66, 4.5, 0.25))  # F#
sax.notes.append(Note(67, 67, 4.5, 0.25))  # G
sax.notes.append(Note(62, 62, 4.5, 0.25))  # D

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file created: 'dante_intro.mid'")
