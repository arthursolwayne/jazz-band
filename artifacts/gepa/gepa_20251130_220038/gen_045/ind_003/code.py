
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeating notes
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=41, start=1.75, end=2.0),   # E
    pretty_midi.Note(velocity=100, pitch=40, start=2.0, end=2.25),   # D
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.5),   # F#
    pretty_midi.Note(velocity=100, pitch=44, start=2.5, end=2.75),   # G
    pretty_midi.Note(velocity=100, pitch=42, start=2.75, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.25),   # E
    pretty_midi.Note(velocity=100, pitch=40, start=3.25, end=3.5),   # D
    pretty_midi.Note(velocity=100, pitch=43, start=3.5, end=3.75),   # F#
    pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.0),   # G
    pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.25),   # F
    pretty_midi.Note(velocity=100, pitch=41, start=4.25, end=4.5),   # E
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=100, pitch=43, start=4.75, end=5.0),   # F#
    pretty_midi.Note(velocity=100, pitch=44, start=5.0, end=5.25),   # G
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.5),   # F
    pretty_midi.Note(velocity=100, pitch=41, start=5.5, end=5.75),   # E
    pretty_midi.Note(velocity=100, pitch=40, start=5.75, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # F7 - F (62)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),   # F7 - Bb (67)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),   # F7 - D (69)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),   # F7 - F (71)

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),   # F7 on 2
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),   # F7 on 2
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),   # F7 on 2
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),   # F7 on 2

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),   # F7 on 2
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),   # F7 on 2
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),   # F7 on 2
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),   # F7 on 2
]
piano.notes.extend(piano_notes)

# Dante: Sax solo, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75), # A
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=1.875), # Ab
    pretty_midi.Note(velocity=110, pitch=63, start=1.875, end=2.0),  # G

    # Bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=2.125, end=2.25), # A
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.375), # Ab
    pretty_midi.Note(velocity=110, pitch=63, start=2.375, end=2.5),  # G

    # Bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=2.75), # A
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=2.875), # Ab
    pretty_midi.Note(velocity=110, pitch=63, start=2.875, end=3.0),  # G

    # Wait, let the silence speak
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=3.125, end=3.25), # A
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.375), # Ab
    pretty_midi.Note(velocity=110, pitch=63, start=3.375, end=3.5),  # G

    # Build, cry, finish
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=3.625, end=3.75), # A
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=3.875), # Ab
    pretty_midi.Note(velocity=110, pitch=63, start=3.875, end=4.0),  # G

    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.125),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.25), # A
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.375), # Ab
    pretty_midi.Note(velocity=110, pitch=63, start=4.375, end=4.5),  # G

    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=4.625, end=4.75), # A
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=4.875), # Ab
    pretty_midi.Note(velocity=110, pitch=63, start=4.875, end=5.0),  # G

    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=5.125, end=5.25), # A
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.375), # Ab
    pretty_midi.Note(velocity=110, pitch=63, start=5.375, end=5.5),  # G

    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.625),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=5.75), # A
    pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=5.875), # Ab
    pretty_midi.Note(velocity=110, pitch=63, start=5.875, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Add the drum fills for bars 2-4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.375),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.375),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.375, end=2.75), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.75),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=3.125), # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=3.125),  # Hihat on 4

    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.875),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.875, end=4.25), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.25),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.25, end=4.625), # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.625),  # Hihat on 4

    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.375),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.375),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.375, end=5.75), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.75),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.75, end=6.0),   # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=6.0),    # Hihat on 4
])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
