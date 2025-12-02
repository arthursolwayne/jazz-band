
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: D (D4) -> F# (F#4) -> B (B4) -> D (D5)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=66, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.1875),
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.6875),  # D3
    pretty_midi.Note(velocity=90, pitch=47, start=1.6875, end=1.875),  # E3
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.0),    # F#3
    pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.1875),  # G3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),
    pretty_midi.Note(velocity=85, pitch=66, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0),
    pretty_midi.Note(velocity=75, pitch=72, start=1.875, end=2.0),
    # Bar 2, beat 4: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=85, pitch=66, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=75, pitch=72, start=2.625, end=2.8125),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif: D (D4) -> F# (F#4) -> B (B4) -> D (D5)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=66, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=71, start=3.5625, end=3.75),
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.1875),  # A3
    pretty_midi.Note(velocity=90, pitch=53, start=3.1875, end=3.375),  # Bb3
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.5625),  # B3
    pretty_midi.Note(velocity=90, pitch=57, start=3.5625, end=3.75),  # C#4
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=90, pitch=62, start=3.875, end=4.0),
    pretty_midi.Note(velocity=85, pitch=66, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=69, start=3.875, end=4.0),
    pretty_midi.Note(velocity=75, pitch=72, start=3.875, end=4.0),
    # Bar 3, beat 4: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=90, pitch=62, start=4.625, end=4.8125),
    pretty_midi.Note(velocity=85, pitch=66, start=4.625, end=4.8125),
    pretty_midi.Note(velocity=80, pitch=69, start=4.625, end=4.8125),
    pretty_midi.Note(velocity=75, pitch=72, start=4.625, end=4.8125),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif: D (D4) -> F# (F#4) -> B (B4) -> D (D5)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=66, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=71, start=5.0625, end=5.25),
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.6875),  # D4
    pretty_midi.Note(velocity=90, pitch=60, start=4.6875, end=4.875),  # E4
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0625),  # F#4
    pretty_midi.Note(velocity=90, pitch=64, start=5.0625, end=5.25),  # G4
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=90, pitch=62, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=85, pitch=66, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=80, pitch=69, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=75, pitch=72, start=5.375, end=5.5625),
    # Bar 4, beat 4: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=90, pitch=62, start=6.125, end=6.3125),
    pretty_midi.Note(velocity=85, pitch=66, start=6.125, end=6.3125),
    pretty_midi.Note(velocity=80, pitch=69, start=6.125, end=6.3125),
    pretty_midi.Note(velocity=75, pitch=72, start=6.125, end=6.3125),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.1875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.1875),  # Snare on 4
]
# Hihat every eighth
for i in range(8):
    start = 1.5 + (i * 0.1875)
    end = start + 0.1875
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.5625, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.3125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.6875),  # Snare on 4
]
# Hihat every eighth
for i in range(8):
    start = 3.0 + (i * 0.1875)
    end = start + 0.1875
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=5.0625, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.8125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.1875),  # Snare on 4
]
# Hihat every eighth
for i in range(8):
    start = 4.5 + (i * 0.1875)
    end = start + 0.1875
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
