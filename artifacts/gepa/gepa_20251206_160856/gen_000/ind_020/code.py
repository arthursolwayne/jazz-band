
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in D (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),   # G2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # C#5
]
piano.notes.extend(piano_notes)

# Sax: short motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5),   # G2
]
bass.notes.extend(bass_notes)

# Piano: Bm7 (B-D-F#-A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # F#5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # A5
]
piano.notes.extend(piano_notes)

# Sax: continue motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # F4
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # F4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # A2
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0),   # G2
]
bass.notes.extend(bass_notes)

# Piano: G7 (G-B-D-F#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.25),  # F#5
]
piano.notes.extend(piano_notes)

# Sax: finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # F4
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.5),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75),  # F4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
