
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    # Bar 2 (1.5s - 3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # D#
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0), # D
    # Bar 3 (3.0s - 4.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375), # B
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.75), # B#
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5), # B
    # Bar 4 (4.5s - 6.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25), # D#
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0), # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5s - 3.0s)
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875), # G7 (D7: D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.875),
    # Bar 3 (3.0s - 4.5s)
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75), # G7 again
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=79, start=3.375, end=3.75),
    # Bar 4 (4.5s - 6.0s)
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.625), # G7 again
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625)
]
piano.notes.extend(piano_notes)

# Sax: Melody, one short motif, make it sing
sax_notes = [
    # Bar 2 (1.5s - 3.0s)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0), # G
    # Bar 3 (3.0s - 4.5s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5), # E
    # Bar 4 (4.5s - 6.0s)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0), # E
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2 (1.5s - 3.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375), # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875), # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125), # Snare 4
    # Bar 3 (3.0s - 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875), # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375), # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625), # Snare 4
    # Bar 4 (4.5s - 6.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375), # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875), # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125), # Snare 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
