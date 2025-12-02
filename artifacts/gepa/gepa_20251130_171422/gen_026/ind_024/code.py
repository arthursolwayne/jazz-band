
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.875),   # F (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # Gb (chromatic)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # A (3rd)
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=3.0),   # Bb (4th)
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),   # B (chromatic)
    pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.75),  # D (5th)
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125),  # Eb (6th)
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),   # G (7th)
    pretty_midi.Note(velocity=90, pitch=51, start=4.5, end=4.875),   # Ab (chromatic)
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),  # Bb (octave)
    pretty_midi.Note(velocity=90, pitch=54, start=5.25, end=5.625),  # B (chromatic)
    pretty_midi.Note(velocity=90, pitch=56, start=5.625, end=6.0),   # D (octave + 5th)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=53, start=1.5, end=2.25),  # Bb7: Bb, D, F, Ab
    pretty_midi.Note(velocity=85, pitch=50, start=1.5, end=2.25),
    pretty_midi.Note(velocity=85, pitch=48, start=1.5, end=2.25),
    pretty_midi.Note(velocity=85, pitch=45, start=1.5, end=2.25),
    pretty_midi.Note(velocity=85, pitch=53, start=3.0, end=3.75),
    pretty_midi.Note(velocity=85, pitch=50, start=3.0, end=3.75),
    pretty_midi.Note(velocity=85, pitch=48, start=3.0, end=3.75),
    pretty_midi.Note(velocity=85, pitch=45, start=3.0, end=3.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Sparse, expressive melody
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),  # G (melody starts)
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # G (echo)
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625),  # G (resolution)
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('fm_jazz_intro.mid')
