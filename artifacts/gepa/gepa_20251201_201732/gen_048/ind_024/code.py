
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet
# Bar 2 (1.5 - 3.0s)
# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # D2 (Fm root)
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25),  # F2 (Fm 3rd)
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.625),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # D2 (Fm root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # D5
]
piano.notes.extend(piano_notes)

# Bar 3 (3.0 - 4.5s)
# Bb7 (Bb, D, F, A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=100, pitch=56, start=3.0, end=3.375),  # A5
]
piano.notes.extend(piano_notes)

# Bar 4 (4.5 - 6.0s)
# Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),  # Eb5
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # G5
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # Bb4
]
piano.notes.extend(piano_notes)

# Drums continue with same pattern
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
]
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Cm7 (melody notes: C, Eb, G, Bb)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Eb5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G5
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # Bb5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # B5 (chromatic)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C5 (return)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
