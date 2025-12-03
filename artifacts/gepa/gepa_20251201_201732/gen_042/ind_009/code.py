
import pretty_midi

# Create the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5  # seconds
for bar in range(1):
    for beat in range(4):
        time = bar * bar_length + beat * 0.375
        if beat in [0, 2]:  # Kick on 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat in [1, 3]:  # Snare on 2 and 4
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F minor
# F2-G2-Ab2-A2-Bb2-B2-C3 (MIDI 53-55-56-57-58-59-60)
# Root and fifth with chromatic approaches
bass_notes = [
    (53, 1.5),   # F2
    (55, 1.875), # G2
    (54, 2.25),  # F#2 (chromatic approach)
    (57, 2.625), # A2
    (59, 2.875), # Bb2
    (57, 3.25),  # A2
    (60, 3.625), # C3
    (58, 4.0),   # Bb2
    (60, 4.375), # C3
    (62, 4.75),  # D3
    (60, 5.125), # C3
    (58, 5.5),   # Bb2
    (57, 5.875), # A2
    (60, 6.25),  # C3
]

for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolving on the last
# Bar 2: F7 (F, A, C, E)
# Bar 3: Gm7 (G, Bb, D, F)
# Bar 4: C7 (C, E, G, Bb)
# Comp on 2 and 4

# Bar 2
note = pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75)  # F (C4)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75)  # A (E4)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.75)  # C (G4)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=78, start=1.5, end=1.75)  # E (A4)
piano.notes.append(note)

# Bar 3
note = pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25)  # G (E3)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25)  # Bb (F3)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25)  # D (A3)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.25)  # F (Bb3)
piano.notes.append(note)

# Bar 4
note = pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75)  # C (C3)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75)  # E (E3)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75)  # G (G3)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75)  # Bb (Bb3)
piano.notes.append(note)

# Little Ray: Full kit again, same pattern
for bar in range(2, 4):  # Bars 2-4
    for beat in range(4):
        time = bar * bar_length + beat * 0.375
        if beat in [0, 2]:  # Kick on 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat in [1, 3]:  # Snare on 2 and 4
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Dante: Tenor sax motif — one short theme that sings
# F - Ab - Bb - C (MIDI 53, 55, 58, 60)
# Start it, leave it hanging, then come back and finish it

# First phrase: F - Ab - Bb - C
note = pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.625)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=55, start=1.625, end=1.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=58, start=1.75, end=1.875)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0)
sax.notes.append(note)

# Second phrase: F - Bb - C (repeat and resolve)
note = pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=58, start=2.375, end=2.5)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.625)
sax.notes.append(note)

# Leave a short pause
note = pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=2.75)
sax.notes.append(note)

# Final resolve
note = pretty_midi.Note(velocity=100, pitch=53, start=2.75, end=2.875)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=58, start=2.875, end=3.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.125)
sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
