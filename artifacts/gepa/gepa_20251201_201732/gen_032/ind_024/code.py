
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in F (F2, Bb2, C3, D3, F3, etc.)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25),  # Bb2
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625),  # C3
    pretty_midi.Note(velocity=80, pitch=57, start=2.625, end=3.0),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, one chord per bar, resolve on the last
piano_notes = [
    # Bar 2 - Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=55, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=58, start=1.5, end=3.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: Motif in F, one short phrase, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # E4
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),  # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.375),  # E3
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),  # F3
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125),  # G3
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),  # Bb3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, one chord per bar
piano_notes = [
    # Bar 3 - F7 (F, A, C, Eflat)
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=4.5),  # A
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=4.5),  # Eflat
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # E4
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5),  # F4
]
sax.notes.extend(sax_notes)

# Drums: same pattern
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # G3
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25),  # Bb3
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # B3
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),  # C4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on last bar
piano_notes = [
    # Bar 4 - Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=80, pitch=58, start=4.5, end=6.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # E4
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),  # F4
]
sax.notes.extend(sax_notes)

# Drums: same pattern
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
