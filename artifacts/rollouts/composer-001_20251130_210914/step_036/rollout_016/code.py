
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, never the same note twice.
# D7 chord: D F# A C#
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # G
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5),  # D
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=79, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=81, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=82, start=5.625, end=6.0),  # Ab
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4.
# D7: D F# A C#
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    # Comp on 2 and 4
    pretty_midi.Note(velocity=95, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=95, pitch=72, start=1.875, end=2.0),  # F#
    pretty_midi.Note(velocity=95, pitch=76, start=1.875, end=2.0),  # C#
    pretty_midi.Note(velocity=95, pitch=62, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=95, pitch=72, start=2.625, end=2.75),  # F#
    pretty_midi.Note(velocity=95, pitch=76, start=2.625, end=2.75),  # C#
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=95, pitch=62, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=3.875),  # A
    pretty_midi.Note(velocity=95, pitch=72, start=3.75, end=3.875),  # F#
    pretty_midi.Note(velocity=95, pitch=76, start=3.75, end=3.875),  # C#
    pretty_midi.Note(velocity=95, pitch=62, start=4.375, end=4.5),   # D
    pretty_midi.Note(velocity=95, pitch=67, start=4.375, end=4.5),   # A
    pretty_midi.Note(velocity=95, pitch=72, start=4.375, end=4.5),   # F#
    pretty_midi.Note(velocity=95, pitch=76, start=4.375, end=4.5),   # C#
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=95, pitch=62, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=5.25, end=5.375),  # A
    pretty_midi.Note(velocity=95, pitch=72, start=5.25, end=5.375),  # F#
    pretty_midi.Note(velocity=95, pitch=76, start=5.25, end=5.375),  # C#
    pretty_midi.Note(velocity=95, pitch=62, start=5.625, end=5.75),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=5.625, end=5.75),  # A
    pretty_midi.Note(velocity=95, pitch=72, start=5.625, end=5.75),  # F#
    pretty_midi.Note(velocity=95, pitch=76, start=5.625, end=5.75),  # C#
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# Motif: D - F# - A - C# (D7), then D - B - F# - D (chromatic approach to B)
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=76, start=1.875, end=2.0),   # C#
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=110, pitch=71, start=3.125, end=3.25),  # B
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.375),  # F#
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5),   # D
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.625, end=4.75),  # F#
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=76, start=4.875, end=5.0),   # C#
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.125),  # D
    pretty_midi.Note(velocity=110, pitch=71, start=5.125, end=5.25),  # B
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.375),  # F#
    pretty_midi.Note(velocity=110, pitch=62, start=5.375, end=5.5),   # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
