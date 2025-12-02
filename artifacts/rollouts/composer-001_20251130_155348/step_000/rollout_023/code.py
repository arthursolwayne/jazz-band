
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - chromatic walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=73, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625), # C#
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # E
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # E
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # E
]
piano.notes.extend(piano_notes)

# Saxophone - short motif starting on D, ascending with chromaticism, then resolve
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=105, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=105, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=105, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=105, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=105, pitch=64, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=105, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=105, pitch=67, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=105, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=105, pitch=71, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=105, pitch=72, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=105, pitch=74, start=5.625, end=6.0),   # D
]
sax.notes.extend(sax_notes)

# Drums in bars 2-4
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Add hi-hats every eighth note for all bars 2-4
for i in range(1.5, 6.0, 0.375):
    if i % 1.5 == 0:
        continue  # Skip on 1 and 3 to let kick/snare play
    pretty_midi.Note(velocity=100, pitch=42, start=i, end=i + 0.375)

drums.notes.extend([pretty_midi.Note(velocity=100, pitch=42, start=i, end=i + 0.375) for i in range(1.5, 6.0, 0.375) if i % 1.5 != 0])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
