
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
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

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),  # Gb
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),   # Ab
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
# Bar 2: Cm7 (Fm key center)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=60, start=1.5, end=1.875),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),   # Eb
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.875),   # G
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),   # Bb
    # Bar 3: F7 (changing to F7)
    pretty_midi.Note(velocity=95, pitch=65, start=2.625, end=2.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.875),  # G
    pretty_midi.Note(velocity=85, pitch=71, start=2.625, end=2.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=2.875),  # B
    # Bar 4: Bbm7 (back to Fm key center)
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.75),     # Bb
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.75),     # D
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=4.75),     # F
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.75),     # Bb
]
piano.notes.extend(piano_notes)

# Sax: Your melody - short motif, singable, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # Bb
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: continue the pattern
for i in range(1.5, 6.0, 0.375):
    if i % 1.0 == 0.0:
        # Kick on 1 and 3
        pretty_midi.Note(velocity=100, pitch=36, start=i, end=i+0.375)
    if (i % 1.0) == 0.75:
        # Snare on 2 and 4
        pretty_midi.Note(velocity=110, pitch=38, start=i, end=i+0.125)
    if i % 0.5 == 0.0:
        # Hi-hat on every eighth
        pretty_midi.Note(velocity=90, pitch=42, start=i, end=i+0.375)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
