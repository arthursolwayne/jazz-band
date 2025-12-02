
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=44, start=5.625, end=6.0),  # Ab
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=57, start=1.5, end=1.875),  # F7 (Bb)
    pretty_midi.Note(velocity=95, pitch=55, start=1.5, end=1.875),  # F7 (D)
    pretty_midi.Note(velocity=95, pitch=60, start=1.5, end=1.875),  # F7 (A)
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875),  # F7 (C)
    pretty_midi.Note(velocity=95, pitch=57, start=2.25, end=2.625),  # F7 (Bb)
    pretty_midi.Note(velocity=95, pitch=55, start=2.25, end=2.625),  # F7 (D)
    pretty_midi.Note(velocity=95, pitch=60, start=2.25, end=2.625),  # F7 (A)
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.625),  # F7 (C)
    pretty_midi.Note(velocity=95, pitch=57, start=3.75, end=4.125),  # F7 (Bb)
    pretty_midi.Note(velocity=95, pitch=55, start=3.75, end=4.125),  # F7 (D)
    pretty_midi.Note(velocity=95, pitch=60, start=3.75, end=4.125),  # F7 (A)
    pretty_midi.Note(velocity=95, pitch=62, start=3.75, end=4.125),  # F7 (C)
    pretty_midi.Note(velocity=95, pitch=57, start=5.25, end=5.625),  # F7 (Bb)
    pretty_midi.Note(velocity=95, pitch=55, start=5.25, end=5.625),  # F7 (D)
    pretty_midi.Note(velocity=95, pitch=60, start=5.25, end=5.625),  # F7 (A)
    pretty_midi.Note(velocity=95, pitch=62, start=5.25, end=5.625),  # F7 (C)
]
piano.notes.extend(piano_notes)

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.625),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.625, end=1.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=2.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.875, end=2.25), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.125),  # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.125, end=2.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.95), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.75), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=2.75, end=2.875), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.125),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.125, end=3.25), # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.25, end=3.625), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.45), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.25), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.25, end=4.375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=4.375, end=4.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.625, end=4.75), # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=5.125), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.95), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.75), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=5.75, end=5.875), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=5.875, end=6.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.125),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=6.0, end=6.375),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=6.125, end=6.25), # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=38, start=6.25, end=6.625), # Snare on 4
]
drums.notes.extend(drum_notes)

# Dante on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=5.75, end=6.0),  # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
