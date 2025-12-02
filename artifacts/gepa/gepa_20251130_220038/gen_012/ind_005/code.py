
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=90, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=90, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=90, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=90, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm, chromatic approaches
bass_notes = [
    (30, 1.5),  # D (root)
    (31, 1.875), # Eb (chromatic)
    (29, 2.25),  # C (3rd)
    (30, 2.625), # D (root)
    (32, 2.75),  # F (5th)
    (31, 3.125), # Eb (chromatic)
    (30, 3.5),   # D (root)
    (29, 3.875), # C (3rd)
    (30, 4.25),  # D (root)
    (31, 4.625), # Eb (chromatic)
    (29, 5.0),   # C (3rd)
    (30, 5.375), # D (root)
    (32, 5.5),   # F (5th)
    (31, 5.875), # Eb (chromatic)
    (30, 6.0),   # D (root)
]
for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Dm7: D, F, A, C
# Bar 2: Comp on beat 2
piano_notes = [
    (50, 2.25, 0.375),  # D
    (52, 2.25, 0.375),  # F
    (55, 2.25, 0.375),  # A
    (57, 2.25, 0.375),  # C
    # Bar 3: Comp on beat 2
    (50, 3.625, 0.375), # D
    (52, 3.625, 0.375), # F
    (55, 3.625, 0.375), # A
    (57, 3.625, 0.375), # C
    # Bar 4: Comp on beat 2
    (50, 5.0, 0.375),   # D
    (52, 5.0, 0.375),   # F
    (55, 5.0, 0.375),   # A
    (57, 5.0, 0.375),   # C
]
for pitch, time, duration in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# Sax: Motif in Dm, start on bar 2, leave it hanging
sax_notes = [
    (50, 2.0, 0.375),  # D
    (52, 2.375, 0.375), # F
    (55, 2.75, 0.375),  # A
    (50, 3.125, 0.375), # D
    (52, 3.5, 0.375),   # F
    (50, 3.875, 0.375), # D
    (52, 4.25, 0.375),  # F
    (55, 4.625, 0.375), # A
    (50, 5.0, 0.375),   # D
    (52, 5.375, 0.375), # F
    (50, 5.75, 0.375),  # D
    (52, 6.0, 0.375),   # F
]
for pitch, time, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Drums: Bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=90, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=90, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=90, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=90, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
