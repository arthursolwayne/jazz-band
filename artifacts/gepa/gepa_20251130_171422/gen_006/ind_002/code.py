
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante on tenor sax
bass = pretty_midi.Instrument(program=33)      # Marcus on bass
piano = pretty_midi.Instrument(program=0)      # Diane on piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray on drums

# Drums: kick=36, snare=38, hihat=42
# Time signatures: 4/4, 1 bar = 1.5 seconds

# -------------------
# DRUMS: Little Ray
# -------------------

# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        # Kick on 1 and 3
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Snare on 2 and 4
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# -------------------
# BASS: Marcus
# -------------------

# Walking line in Dm (D, F, G, C), chromatic approaches, never the same note
# Bar 1: D, F#, G, C
# Bar 2: F, G#, A, D
# Bar 3: G, A#, B, E
# Bar 4: A, B#, C#, F

bass_notes = [
    (0, 3, 0.25),   # D (bar 1 beat 1)
    (0, 6, 0.25),   # F#
    (0, 7, 0.25),   # G
    (0, 10, 0.25),  # C

    (1.5, 5, 0.25), # F (bar 2 beat 1)
    (1.5, 8, 0.25), # G#
    (1.5, 9, 0.25), # A
    (1.5, 2, 0.25), # D

    (3.0, 7, 0.25), # G (bar 3 beat 1)
    (3.0, 10, 0.25),# A#
    (3.0, 11, 0.25),# B
    (3.0, 4, 0.25), # E

    (4.5, 9, 0.25), # A (bar 4 beat 1)
    (4.5, 11, 0.25),# B#
    (4.5, 12, 0.25),# C#
    (4.5, 6, 0.25)  # D (chromatic approach to F)
]

for start, pitch, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# -------------------
# PIANO: Diane
# -------------------

# Comping on 2 and 4 with 7th chords, emotional and driving
# Dm7: D, F, A, C
# F7: F, A, C, E
# Gm7: G, Bb, D, F
# C7: C, E, G, Bb

piano_notes = [
    # Bar 1: Dm7 on beat 2
    (0.75, 3, 0.25),  # D
    (0.75, 5, 0.25),  # F
    (0.75, 10, 0.25), # A
    (0.75, 11, 0.25), # C

    # Bar 2: F7 on beat 4
    (2.25, 5, 0.25),  # F
    (2.25, 10, 0.25), # A
    (2.25, 11, 0.25), # C
    (2.25, 13, 0.25), # E

    # Bar 3: Gm7 on beat 2
    (3.75, 7, 0.25),  # G
    (3.75, 8, 0.25),  # Bb
    (3.75, 10, 0.25), # D
    (3.75, 11, 0.25), # F

    # Bar 4: C7 on beat 4
    (5.25, 11, 0.25), # C
    (5.25, 13, 0.25), # E
    (5.25, 15, 0.25), # G
    (5.25, 16, 0.25)  # Bb
]

for start, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# -------------------
# SAX: Dante
# -------------------

# Motif: D - F - G - C (Dm7), then leave it hanging on F
# Repeat with a slight variation

sax_notes = [
    (0, 3, 0.25),   # D
    (0.375, 5, 0.25), # F
    (0.75, 7, 0.25),  # G
    (1.125, 11, 0.25),# C

    (1.5, 5, 0.25),   # F (repeat with variation)
    (1.875, 7, 0.25), # G
    (2.25, 11, 0.25), # C
    (2.625, 5, 0.25), # F (hang on F)
]

for start, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Save the MIDI file
midi.write("dante_intro.mid")
