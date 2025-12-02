
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
    # Hi-hats on every eighth note
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Everybody in
# Key: F major
# Chord progression: Fmaj7 -> Bb7 -> Em7 -> Am7
# Diane's chords
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # F (C4)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # A (E4)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # B (F#4)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # C (A4)
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # Bb (G3)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # D (A3)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # E (B3)
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25), # F (C4)
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # E (D3)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # G (F3)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # A (G3)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # B (A3)
    # Bar 4 resolution
    pretty_midi.Note(velocity=100, pitch=58, start=2.625, end=3.0), # F (E3)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0), # A (F3)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0), # C (B3)
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0), # D (C4)
]
piano.notes.extend(piano_notes)

# Marcus's walking bass line: F -> Bb -> E -> A
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875), # F (D2)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # Bb (E2)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # E (F2)
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),  # A (G2)
    # Chromatic approach to F
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.5 + 0.125), # Eb (D#2)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5 + 0.125, end=1.5 + 0.25), # F (D2)
]
bass.notes.extend(bass_notes)

# Dante's sax motif (Bar 2: start, Bar 4: finish)
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=68, start=1.5, end=1.625), # G (F#4)
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75), # E (D4)
    pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=1.875), # G (F#4)
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.0), # B (A4)
    pretty_midi.Note(velocity=110, pitch=68, start=2.0, end=2.125), # G (F#4)
    pretty_midi.Note(velocity=110, pitch=65, start=2.125, end=2.25), # E (D4)
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=68, start=2.625, end=2.75), # G (F#4)
    pretty_midi.Note(velocity=110, pitch=65, start=2.75, end=2.875), # E (D4)
    pretty_midi.Note(velocity=110, pitch=62, start=2.875, end=3.0),  # D (C4)
]
sax.notes.extend(sax_notes)

# Bar 3 and 4: Drums
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)

drums.notes.extend([
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
])

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
