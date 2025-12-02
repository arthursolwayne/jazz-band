
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
    # Hi-hat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Dm
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # Eb
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),   # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),   # Eb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # Bb
    # Bar 3: Dm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),   # Eb
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),   # Bb
    # Bar 4: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - motif: D - Eb - F - D (melodic interval, with a hint of altered)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),    # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),    # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875),    # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),     # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.125),     # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.125, end=2.25),    # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375),    # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.375, end=2.5),     # Bb (altered)
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.625),     # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75),    # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=2.875),    # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.875, end=3.0),     # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),     # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25),    # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.375),    # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),     # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625),     # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.625, end=3.75),    # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.875),    # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.0),     # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.125),     # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.25),    # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.375),    # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.375, end=4.5),     # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),     # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.625, end=4.75),    # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=4.875),    # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0),     # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.125),     # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.125, end=5.25),    # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.375),    # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.375, end=5.5),     # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.625),     # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=5.75),    # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),      # D
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
