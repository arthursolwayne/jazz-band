
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line (Marcus)
bass_notes = [
    # Fm7 chord - F, Ab, C, D
    # Walking bass line: F, Gb, G, Ab, A, Bb, B, C
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=63, start=2.625, end=3.0),   # Ab
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),   # F
    pretty_midi.Note(velocity=80, pitch=76, start=1.875, end=2.25),   # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.25),   # C
    pretty_midi.Note(velocity=80, pitch=73, start=1.875, end=2.25),   # D
    # Bar 3: Fm7 on beat 2
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),   # F
    pretty_midi.Note(velocity=80, pitch=76, start=3.375, end=3.75),   # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75),   # C
    pretty_midi.Note(velocity=80, pitch=73, start=3.375, end=3.75),   # D
    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),   # F
    pretty_midi.Note(velocity=80, pitch=76, start=4.875, end=5.25),   # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25),   # C
    pretty_midi.Note(velocity=80, pitch=73, start=4.875, end=5.25),   # D
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante) - one short motif, leave it hanging
sax_notes = [
    # Start with a phrase: F, Ab, Bb, C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.65),    # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.65, end=1.8),    # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=1.8, end=1.95),    # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.95, end=2.1),    # C
    # Then repeat same phrase but ending on D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.4),    # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.4, end=2.55),    # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.55, end=2.7),    # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.7, end=3.0),     # D
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line (Marcus)
bass_notes = [
    # Fm7 chord - F, Ab, C, D
    # Walking bass line: D, Eb, E, F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: Fm7 on beat 2
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),   # F
    pretty_midi.Note(velocity=80, pitch=76, start=3.375, end=3.75),   # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75),   # C
    pretty_midi.Note(velocity=80, pitch=73, start=3.375, end=3.75),   # D
    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),   # F
    pretty_midi.Note(velocity=80, pitch=76, start=4.875, end=5.25),   # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25),   # C
    pretty_midi.Note(velocity=80, pitch=73, start=4.875, end=5.25),   # D
]
for note in piano_notes:
    piano.notes.append(note)

# Drums (Little Ray)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    # Fm7 chord - F, Ab, C, D
    # Walking bass line: C, D, Eb, F
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),   # F
    pretty_midi.Note(velocity=80, pitch=76, start=4.875, end=5.25),   # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25),   # C
    pretty_midi.Note(velocity=80, pitch=73, start=4.875, end=5.25),   # D
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante) - finish the motif with a resolution to F
sax_notes = [
    # Resolving to F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
