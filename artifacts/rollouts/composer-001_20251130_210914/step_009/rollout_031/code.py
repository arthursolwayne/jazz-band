
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=39, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=41, start=1.75, end=1.875),  # Gb
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0),  # Ab
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=41, start=2.125, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=100, pitch=39, start=2.375, end=2.5),  # Eb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=40, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=39, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=41, start=2.75, end=2.875),  # Gb
    pretty_midi.Note(velocity=100, pitch=42, start=2.875, end=3.0),  # Ab
    # Bar 5
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=41, start=3.125, end=3.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=40, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=39, start=3.375, end=3.5),  # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=46, start=1.5, end=1.625),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.625),  # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.625),  # F7 - Eb
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.625),  # F7 - Ab
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=46, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.375),  # Ab
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=46, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=2.5, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=2.5, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=2.625),  # Ab
    # Bar 5
    pretty_midi.Note(velocity=100, pitch=46, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=3.25, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=3.25, end=3.375),  # Ab
]
piano.notes.extend(piano_notes)

# Dante: Motif, one short phrase, starts and ends on F, with a rest in the middle
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=2.5, end=2.75),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('wayne_intro.mid')
