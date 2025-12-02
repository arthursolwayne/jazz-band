
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
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625), # D#
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # E

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.125), # D#
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=63, start=5.25, end=5.625), # D#
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # E7 (D7?) - E
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # B
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # D

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # D#

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
]
piano.notes.extend(piano_notes)

# Sax (Dante): Motif in D, one short phrase, leaves it hanging
# Motif: D - F# - G - D (with a slight chromatic approach on F#)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # E (chromatic approach to F#)
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),  # D

    # Repeat the motif a half step up
    pretty_midi.Note(velocity=110, pitch=63, start=3.0, end=3.375),  # D#
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=63, start=4.125, end=4.5),  # D#

    # Final phrase, resolving with a twist
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Add hihat fills in bar 2
drum_notes += [
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

# Add snare fills in bar 3
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
]

# Add kick and hihat in bar 4
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]

drums.notes.extend(drum_notes)

# Finalize
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
