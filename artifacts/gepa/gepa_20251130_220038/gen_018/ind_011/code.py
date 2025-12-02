
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2: Fm7 -> Bb7
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.625), # Gb
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # E
    # Bar 3: Bb7 -> Eb7
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # A
    # Bar 4: Eb7 -> Fm7
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=48, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=100, pitch=46, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: F7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25),  # D
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75),  # Db
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # F
    # Bar 4: Eb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25),  # Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - G - Fb (Gb) - E
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=44, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=46, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=45, start=1.75, end=1.875),  # Gb
    pretty_midi.Note(velocity=110, pitch=43, start=1.875, end=2.0),   # E
    # Repeat the motif shifted up a half step
    pretty_midi.Note(velocity=110, pitch=45, start=2.5, end=2.625),  # Gb
    pretty_midi.Note(velocity=110, pitch=47, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=110, pitch=46, start=2.75, end=2.875),  # Ab
    pretty_midi.Note(velocity=110, pitch=44, start=2.875, end=3.0),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Add drum fill in bar 3
# Kick on 1 and 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
