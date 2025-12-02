
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: Fm
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.5),  # D
    # Bar 3: Fm
    pretty_midi.Note(velocity=90, pitch=44, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=2.75, end=3.0),  # Gb
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=41, start=3.25, end=3.5),  # D
    # Bar 4: Fm
    pretty_midi.Note(velocity=90, pitch=44, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.0),  # Gb
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=41, start=4.25, end=4.5),  # D
    # Fm7 chord on final bar
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.75),  # Gb
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=39, start=4.5, end=4.75)   # C
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=44, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=2.0, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=39, start=2.0, end=2.25),  # C
    # Bar 3: F7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=39, start=3.0, end=3.25),  # C
    # Bar 4: F7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=44, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=4.0, end=4.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=39, start=4.0, end=4.25),  # C
]
piano.notes.extend(piano_notes)

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.0),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.0, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0)
]
drums.notes.extend(drum_notes)

# Dante on sax: short motif, make it sing
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=110, pitch=61, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0),  # B
    # Bar 3: Continue motif
    pretty_midi.Note(velocity=110, pitch=60, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=110, pitch=61, start=2.75, end=3.0),  # Bb
    # Bar 4: Finish motif
    pretty_midi.Note(velocity=110, pitch=59, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.0),  # A
    # Final resolution
    pretty_midi.Note(velocity=110, pitch=57, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=110, pitch=59, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=110, pitch=57, start=4.5, end=4.75),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
