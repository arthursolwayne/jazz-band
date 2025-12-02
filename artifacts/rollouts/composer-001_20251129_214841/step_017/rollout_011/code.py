
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)
# Saxophone: motif in C minor, 4 notes, spaced with rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=2.625, end=3.0),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # D4
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # C4
]

sax.notes.extend(sax_notes)

# Bass: walking line in C minor, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # C3
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # C#3
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625), # D3
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),  # D#3
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),  # E3
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75), # F3
    pretty_midi.Note(velocity=80, pitch=54, start=3.75, end=4.125), # F#3
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5),  # G3
    pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.875),  # A3
    pretty_midi.Note(velocity=80, pitch=58, start=4.875, end=5.25), # A#3
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.625), # B3
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0),  # C4
]

bass.notes.extend(bass_notes)

# Piano: comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2, beat 2
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.625),  # C4
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),  # E4
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),  # B4
    # Bar 2, beat 4
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),  # C4
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),  # E4
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),  # B4
    # Bar 3, beat 2
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),   # C4
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),   # E4
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),   # G4
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),   # B4
    # Bar 3, beat 4
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0),  # C4
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),  # E4
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),  # G4
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),  # B4
]

piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
