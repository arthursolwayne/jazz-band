
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Tenor motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D5
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875), # E5
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.0),   # D5
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.1875),  # D5
    pretty_midi.Note(velocity=110, pitch=65, start=2.1875, end=2.375),# F5
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.6875),   # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.6875, end=1.875), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.0),   # A2
    pretty_midi.Note(velocity=80, pitch=38, start=2.0, end=2.1875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=2.1875, end=2.375),# F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875),  # D5
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.6875),  # F#5
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.6875),  # A5
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.6875),  # C#6
]
piano.notes.extend(piano_notes)

# Bar 3: Gm7 (G-Bb-D-F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=2.375, end=2.5625), # G5
    pretty_midi.Note(velocity=90, pitch=71, start=2.375, end=2.5625), # Bb5
    pretty_midi.Note(velocity=90, pitch=69, start=2.375, end=2.5625), # D5
    pretty_midi.Note(velocity=90, pitch=72, start=2.375, end=2.5625), # F5
]
piano.notes.extend(piano_notes)

# Bar 4: Bm7 (B-D-F#-A)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=3.125, end=3.3125), # B5
    pretty_midi.Note(velocity=90, pitch=69, start=3.125, end=3.3125), # D5
    pretty_midi.Note(velocity=90, pitch=72, start=3.125, end=3.3125), # F#5
    pretty_midi.Note(velocity=90, pitch=69, start=3.125, end=3.3125), # A5
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # D5
    pretty_midi.Note(velocity=110, pitch=64, start=3.1875, end=3.375), # E5
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.5625), # D5
    pretty_midi.Note(velocity=110, pitch=62, start=3.5625, end=3.75),  # D5
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=3.9375),  # F5
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.1875),   # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.1875, end=3.375), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.5625), # A2
    pretty_midi.Note(velocity=80, pitch=38, start=3.5625, end=3.75),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=3.9375),  # F2
]
bass.notes.extend(bass_notes)

# Drums: kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),  # D5
    pretty_midi.Note(velocity=110, pitch=64, start=4.6875, end=4.875), # E5
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.0625), # D5
    pretty_midi.Note(velocity=110, pitch=62, start=5.0625, end=5.25),  # D5
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.4375),  # F5
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.6875),   # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.6875, end=4.875), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.0625), # A2
    pretty_midi.Note(velocity=80, pitch=38, start=5.0625, end=5.25),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.4375),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 4: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.6875),  # D5
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.6875),  # F#5
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.6875),  # A5
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.6875),  # C#6
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
