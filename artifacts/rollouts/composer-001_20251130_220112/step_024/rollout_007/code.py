
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in D (D F A B)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # B
    # Chromatic approach to D
    pretty_midi.Note(velocity=80, pitch=61, start=3.0, end=3.125),  # C#
    pretty_midi.Note(velocity=90, pitch=62, start=3.125, end=3.375) # D
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4, D7 (D F# A C)
piano_notes = [
    # Bar 2, beat 2: D7 (D F# A C)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),  # C
    # Bar 2, beat 4: D7 (D F# A C)
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # F#
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),   # C
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax motif (D F A), start on 1, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625)  # A
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in D (D F A B)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),  # B
    # Chromatic approach to D
    pretty_midi.Note(velocity=80, pitch=61, start=4.5, end=4.625),  # C#
    pretty_midi.Note(velocity=90, pitch=62, start=4.625, end=4.875) # D
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4, D7 (D F# A C)
piano_notes = [
    # Bar 3, beat 2: D7 (D F# A C)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),  # C
    # Bar 3, beat 4: D7 (D F# A C)
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),   # F#
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),   # C
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax motif (D F A), return to finish
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125)  # A
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in D (D F A B)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # B
    # Chromatic approach to D
    pretty_midi.Note(velocity=80, pitch=61, start=6.0, end=6.125),  # C#
    pretty_midi.Note(velocity=90, pitch=62, start=6.125, end=6.375) # D
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4, D7 (D F# A C)
piano_notes = [
    # Bar 4, beat 2: D7 (D F# A C)
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),  # C
    # Bar 4, beat 4: D7 (D F# A C)
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),   # F#
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),   # C
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax motif (D F A), complete
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625)  # A
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
