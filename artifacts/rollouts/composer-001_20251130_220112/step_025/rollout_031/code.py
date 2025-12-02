
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax - start of motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),  # F#
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Bass - walking line
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=42, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=70, pitch=43, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=70, pitch=40, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=70, pitch=41, start=2.25, end=2.5),  # F#
    pretty_midi.Note(velocity=70, pitch=42, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=70, pitch=43, start=2.75, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano - comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (1.75 - 2.0)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D7
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),  # G
    # Bar 2, beat 4 (2.75 - 3.0)
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),  # D7
    pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=3.0),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),  # G
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax - repeat motif with slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # G
]
sax.notes.extend(sax_notes)

# Bass - walking line
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=42, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=70, pitch=43, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=70, pitch=40, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=70, pitch=41, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=70, pitch=42, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=70, pitch=43, start=4.25, end=4.5),  # G
]
bass.notes.extend(bass_notes)

# Piano - comp on 2 and 4
piano_notes = [
    # Bar 3, beat 2 (3.25 - 3.5)
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D7
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),  # G
    # Bar 3, beat 4 (4.25 - 4.5)
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),  # D7
    pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.5),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.5),  # G
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax - finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5),  # F#
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Bass - walking line
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=42, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=70, pitch=43, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=70, pitch=40, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=70, pitch=41, start=5.25, end=5.5),  # F#
    pretty_midi.Note(velocity=70, pitch=42, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=70, pitch=43, start=5.75, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano - comp on 2 and 4
piano_notes = [
    # Bar 4, beat 2 (4.75 - 5.0)
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D7
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0),  # G
    # Bar 4, beat 4 (5.75 - 6.0)
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0),  # D7
    pretty_midi.Note(velocity=80, pitch=60, start=5.75, end=6.0),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=5.75, end=6.0),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=5.75, end=6.0),  # G
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_start = 1.5
for bar in range(2, 5):
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat on every eighth
    for i in range(0, 4):
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875)
    bar_start += 1.5

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
