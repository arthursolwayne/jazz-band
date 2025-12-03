
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line in D (D2 - G2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),   # A2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D-F#-A-C#)
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C#5
    # Bar 3: Bm7 (B-D-F#-A)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # F#5
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # A4
    # Bar 4: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # G5
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # B5
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F5
]
piano.notes.extend(piano_notes)

# Sax: short motif, one phrase, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D5
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75),  # F#5
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),  # A5
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0),   # C#6
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.125),  # A5
    pretty_midi.Note(velocity=110, pitch=65, start=2.125, end=2.25),  # F#5
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.375),  # D5
    pretty_midi.Note(velocity=110, pitch=59, start=2.375, end=2.5),   # B4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: walking line (D2 - G2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75),  # B2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),   # A2
]
bass.notes.extend(bass_notes)

# Piano: open voicings
piano_notes = [
    # Bar 3: Bm7 (B-D-F#-A)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F#5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # A4
    # Bar 4: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # G5
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # B5
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # F5
    # Bar 4: Resolution
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # F#4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # C#5
]
piano.notes.extend(piano_notes)

# Sax: repeat motif, resolve
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # D5
    pretty_midi.Note(velocity=110, pitch=65, start=3.125, end=3.25),  # F#5
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.375),  # A5
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.5),   # C#6
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.625),  # A5
    pretty_midi.Note(velocity=110, pitch=65, start=3.625, end=3.75),  # F#5
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=3.875),  # D5
    pretty_midi.Note(velocity=110, pitch=59, start=3.875, end=4.0),   # B4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5),
]
drums.notes.extend(drum_notes)

# Bass: walking line (D2 - G2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # A2
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.25),  # B2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # A2
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),   # A2
]
bass.notes.extend(bass_notes)

# Piano: resolve on Dmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # C#5
]
piano.notes.extend(piano_notes)

# Sax: resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625),  # D5
    pretty_midi.Note(velocity=110, pitch=65, start=4.625, end=4.75),  # F#5
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875),  # A5
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.0),   # C#6
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.125),  # A5
    pretty_midi.Note(velocity=110, pitch=65, start=5.125, end=5.25),  # F#5
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.375),  # D5
    pretty_midi.Note(velocity=110, pitch=59, start=5.375, end=5.5),   # B4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
