
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm, chromatic approaches, no repeated notes
# Fm: F, Ab, D, C
# Walking bass line: F, Gb, Ab, G, A, Bb, B, C, D, Eb, E, F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=63, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=61, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=59, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),  # F
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bars 2-4: two chords per bar, on beats 2 and 4
# Bar 2: Fm7 on 2, Fm7 on 4
# Bar 3: Fm7 on 2, Fm7 on 4
# Bar 4: Fm7 on 2, Fm7 on 4
piano_notes = [
    # Bar 2 - 2
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=61, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.625),  # Eb
    # Bar 2 - 4
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=61, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=3.0, end=3.375),  # Eb
    # Bar 3 - 2
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=61, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.125),  # Eb
    # Bar 3 - 4
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=61, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.875),  # Eb
    # Bar 4 - 2
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=61, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.625),  # Eb
    # Bar 4 - 4
    pretty_midi.Note(velocity=80, pitch=64, start=6.0, end=6.375),  # F
    pretty_midi.Note(velocity=80, pitch=61, start=6.0, end=6.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=60, start=6.0, end=6.375),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=6.0, end=6.375),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Motif in Fm, one short phrase
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F, Ab, A, Bb
# Start at bar 2, on beat 1
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
