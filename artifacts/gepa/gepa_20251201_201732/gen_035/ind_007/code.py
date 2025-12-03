
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass - walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=75, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # F
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),  # G
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Diane on piano - open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (Fmaj7) - 1.5 - 3.0s
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),  # F
    # Bar 3 (F7) - 3.0 - 4.5s
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25),  # F
    # Bar 4 (Fmaj7 with a chromatic approach) - 4.5 - 6.0s
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.5),  # F
]
piano.notes.extend(piano_notes)

# Dante on sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.5, end=2.75),  # G
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # D
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=5.75, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Bar 2 (1.5 - 3.0s)
for i in range(4):
    start = 1.5 + i * 0.375
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375) if i % 2 == 0 else None
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75) if i % 2 == 1 else None
    for j in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + j * 0.1875, end=start + j * 0.1875 + 0.1875)

# Bar 3 (3.0 - 4.5s)
for i in range(4):
    start = 3.0 + i * 0.375
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375) if i % 2 == 0 else None
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75) if i % 2 == 1 else None
    for j in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + j * 0.1875, end=start + j * 0.1875 + 0.1875)

# Bar 4 (4.5 - 6.0s)
for i in range(4):
    start = 4.5 + i * 0.375
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375) if i % 2 == 0 else None
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75) if i % 2 == 1 else None
    for j in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + j * 0.1875, end=start + j * 0.1875 + 0.1875)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
