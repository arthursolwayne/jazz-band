
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
# Bass: F2 (D2 is C, G2 is D, but we're in Fm, so start on F2)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F2 on 1
    pretty_midi.Note(velocity=80, pitch=55, start=1.875, end=2.25),  # Ab2 on 2
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # D2 on 3
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),  # F2 on 4
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # Ab
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # Ab
])
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
])
piano.notes.extend(piano_notes)

# Sax: one short motif, start it, leave it hanging, come back and finish it
# Motif: F, Ab, Bb, F (but not in scale, just F, Ab, Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=57, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=2.25, end=2.5),  # F
]
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=53, start=2.75, end=3.0),  # F (finishing the motif)
])
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
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

# Bar 4: Bass continues (3.0 - 4.5s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # F2 on 1
    pretty_midi.Note(velocity=80, pitch=55, start=3.375, end=3.75),  # Ab2 on 2
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125),  # D2 on 3
    pretty_midi.Note(velocity=80, pitch=53, start=4.125, end=4.5),  # F2 on 4
]
bass.notes.extend(bass_notes)

# Bar 4: Piano continues (3.0 - 4.5s)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Ab
]
piano.notes.extend(piano_notes)

# Bar 4: Drums (3.0 - 4.5s)
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

# Bar 4: Sax continues (3.0 - 4.5s)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.25),  # F (finishing the motif)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
