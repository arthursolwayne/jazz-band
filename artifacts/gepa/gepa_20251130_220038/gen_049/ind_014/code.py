
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on beat 0 and 2
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Snare on beat 1 and 3
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=110, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Hi-hats on every eighth
    for i in range(8):
        note = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.05)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.5 + 0.375)),    # D
    (pretty_midi.Note(velocity=80, pitch=65, start=1.5 + 0.375, end=1.5 + 0.75)), # Eb
    (pretty_midi.Note(velocity=80, pitch=62, start=1.5 + 0.75, end=1.5 + 1.125)), # C
    (pretty_midi.Note(velocity=80, pitch=60, start=1.5 + 1.125, end=1.5 + 1.5)),  # Bb
    (pretty_midi.Note(velocity=80, pitch=62, start=1.5 + 1.5, end=1.5 + 1.875)),  # C
    (pretty_midi.Note(velocity=80, pitch=65, start=1.5 + 1.875, end=1.5 + 2.25)), # Eb
    (pretty_midi.Note(velocity=80, pitch=64, start=1.5 + 2.25, end=1.5 + 2.625)), # D
    (pretty_midi.Note(velocity=80, pitch=60, start=1.5 + 2.625, end=1.5 + 3.0)),  # Bb
    (pretty_midi.Note(velocity=80, pitch=62, start=1.5 + 3.0, end=1.5 + 3.375)),  # C
    (pretty_midi.Note(velocity=80, pitch=65, start=1.5 + 3.375, end=1.5 + 3.75)), # Eb
    (pretty_midi.Note(velocity=80, pitch=64, start=1.5 + 3.75, end=1.5 + 4.125)), # D
    (pretty_midi.Note(velocity=80, pitch=60, start=1.5 + 4.125, end=1.5 + 4.5)),  # Bb
    (pretty_midi.Note(velocity=80, pitch=62, start=1.5 + 4.5, end=1.5 + 4.875)),  # C
    (pretty_midi.Note(velocity=80, pitch=65, start=1.5 + 4.875, end=1.5 + 5.25)), # Eb
    (pretty_midi.Note(velocity=80, pitch=64, start=1.5 + 5.25, end=1.5 + 5.625)), # D
    (pretty_midi.Note(velocity=80, pitch=60, start=1.5 + 5.625, end=1.5 + 6.0)),  # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 1 (2nd beat of bar 2) - D7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 0.75, end=1.5 + 0.75 + 0.375), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 0.75, end=1.5 + 0.75 + 0.375), # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 0.75, end=1.5 + 0.75 + 0.375), # B
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 0.75, end=1.5 + 0.75 + 0.375), # C
    # Bar 2, beat 3 (4th beat of bar 2) - D7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 1.125, end=1.5 + 1.125 + 0.375), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 1.125, end=1.5 + 1.125 + 0.375), # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 1.125, end=1.5 + 1.125 + 0.375), # B
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 1.125, end=1.5 + 1.125 + 0.375), # C
    # Bar 3, beat 1 (2nd beat of bar 3) - D7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 2.625, end=1.5 + 2.625 + 0.375), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 2.625, end=1.5 + 2.625 + 0.375), # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 2.625, end=1.5 + 2.625 + 0.375), # B
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 2.625, end=1.5 + 2.625 + 0.375), # C
    # Bar 3, beat 3 (4th beat of bar 3) - D7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375), # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375), # B
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375), # C
    # Bar 4, beat 1 (2nd beat of bar 4) - D7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 4.875, end=1.5 + 4.875 + 0.375), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 4.875, end=1.5 + 4.875 + 0.375), # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 4.875, end=1.5 + 4.875 + 0.375), # B
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 4.875, end=1.5 + 4.875 + 0.375), # C
    # Bar 4, beat 3 (4th beat of bar 4) - D7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 5.25, end=1.5 + 5.25 + 0.375), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 5.25, end=1.5 + 5.25 + 0.375), # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 5.25, end=1.5 + 5.25 + 0.375), # B
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 5.25, end=1.5 + 5.25 + 0.375), # C
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante) - Motif
# Start on D (62), then F (65), then Bb (60), then D (62)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + 0.15), # D
    pretty_midi.Note(velocity=110, pitch=65, start=1.5 + 0.375, end=1.5 + 0.375 + 0.15), # F
    pretty_midi.Note(velocity=110, pitch=60, start=1.5 + 0.75, end=1.5 + 0.75 + 0.15), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=1.5 + 1.5, end=1.5 + 1.5 + 0.15), # D
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on beat 0 and 2
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Snare on beat 1 and 3
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=110, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Hi-hats on every eighth
    for i in range(8):
        note = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.05)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
