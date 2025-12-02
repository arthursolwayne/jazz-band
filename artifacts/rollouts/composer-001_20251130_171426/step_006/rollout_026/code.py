
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
    # Kick on 1 and 3 (0.0, 1.125)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.25),
    # Snare on 2 and 4 (0.75, 1.875)
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth (0.0, 0.375, 0.75, 1.125, 1.5, 1.875)
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (D4), F# (F#4), G (G4), B (B4) - suspending on B at the end of bar 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.25),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0)   # B4
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=80, pitch=41, start=1.75, end=2.0),  # Eb3
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.25),  # E3
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.5),  # F3
    pretty_midi.Note(velocity=80, pitch=45, start=2.5, end=2.75),  # G3
    pretty_midi.Note(velocity=80, pitch=47, start=2.75, end=3.0),  # A3
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.25),  # Bb3
    pretty_midi.Note(velocity=80, pitch=49, start=3.25, end=3.5),  # B3
    pretty_midi.Note(velocity=80, pitch=50, start=3.5, end=3.75),  # C4
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=80, pitch=53, start=4.0, end=4.25),  # Eb4
    pretty_midi.Note(velocity=80, pitch=54, start=4.25, end=4.5),  # E4
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=80, pitch=57, start=4.75, end=5.0),  # G4
    pretty_midi.Note(velocity=80, pitch=59, start=5.0, end=5.25),  # A4
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.5),  # Bb4
    pretty_midi.Note(velocity=80, pitch=61, start=5.5, end=5.75),  # B4
    pretty_midi.Note(velocity=80, pitch=62, start=5.75, end=6.0)   # C5
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4.
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=66, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.5),
    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25)
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
