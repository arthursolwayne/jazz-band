
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F3
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25), # Gb3
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625), # G3
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),  # Ab3
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # Bb3
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75), # C4
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125), # D4
    pretty_midi.Note(velocity=100, pitch=58, start=4.125, end=4.5),  # Eb4
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # F4
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.625), # Gb4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # G4
]
bass.notes.extend(bass_notes)

# Piano - Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.875),  # E4 (F7 chord)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C5
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375),  # E4 (F7 chord)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # C5
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),  # E4 (F7 chord)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # C5
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4 (fill the bar)
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.875, end=start + 2.25)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 2.25, end=start + 2.625)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 2.625, end=start + 3.0)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 3.0, end=start + 3.375)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 3.375, end=start + 3.75)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 3.75, end=start + 4.125)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 4.125, end=start + 4.5)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 4.5, end=start + 4.875)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 4.875, end=start + 5.25)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 5.25, end=start + 5.625)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 5.625, end=start + 6.0)
drums.notes.extend(drum_notes)

# Sax solo - Dante's motif (start at bar 2)
# Motif: F - G - Eb - D (melodic minor)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25), # G4
    pretty_midi.Note(velocity=110, pitch=61, start=2.25, end=2.625), # Eb4
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),  # D4
    # Let it hang
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.75),  # D4
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125),  # D4
    # End with a resolution
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # Gb4
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25), # F4
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625), # D4
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),  # F4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
