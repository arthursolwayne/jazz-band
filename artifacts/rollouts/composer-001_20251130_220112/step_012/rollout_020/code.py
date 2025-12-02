
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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
# Sax: D (D4) to F# (F#4), then back to D (D4) as a motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),
]

sax.notes.extend(sax_notes)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=90, pitch=43, start=1.75, end=2.0),  # Eb3
    pretty_midi.Note(velocity=90, pitch=45, start=2.0, end=2.25),  # F3
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.5),  # G3
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 (D4, F#4, A4, C#5) on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=66, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=2.0),
    # D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=66, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.75),
]

piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif but with a chromatic twist
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=63, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),
]

sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.25),  # G3
    pretty_midi.Note(velocity=90, pitch=49, start=3.25, end=3.5),  # A3
    pretty_midi.Note(velocity=90, pitch=50, start=3.5, end=3.75),  # Bb3
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.0),  # B3
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=66, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),
    # D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=66, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=72, start=4.0, end=4.25),
]

piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif with a slight variation, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),
]

sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.75),  # B3
    pretty_midi.Note(velocity=90, pitch=54, start=4.75, end=5.0),  # C4
    pretty_midi.Note(velocity=90, pitch=55, start=5.0, end=5.25),  # C#4
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.5),  # D4
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=66, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=5.0),
    # D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=66, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=72, start=5.5, end=5.75),
]

piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
# Bar 3 (3.0 - 4.5s)
for i in range(3):
    offset = 3.0 + i * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=offset, end=offset + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=offset + 1.125, end=offset + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=offset + 0.75, end=offset + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=offset + 1.875, end=offset + 2.0)
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=offset, end=offset + 0.375)
    pretty_midi.Note(velocity=90, pitch=42, start=offset + 0.375, end=offset + 0.75)
    pretty_midi.Note(velocity=90, pitch=42, start=offset + 0.75, end=offset + 1.125)
    pretty_midi.Note(velocity=90, pitch=42, start=offset + 1.125, end=offset + 1.5)
    pretty_midi.Note(velocity=90, pitch=42, start=offset + 1.5, end=offset + 1.875)
    pretty_midi.Note(velocity=90, pitch=42, start=offset + 1.875, end=offset + 2.25)
    pretty_midi.Note(velocity=90, pitch=42, start=offset + 2.25, end=offset + 2.625)
    pretty_midi.Note(velocity=90, pitch=42, start=offset + 2.625, end=offset + 3.0)

# Bar 4 (4.5 - 6.0s)
for i in range(3):
    offset = 4.5 + i * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=offset, end=offset + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=offset + 1.125, end=offset + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=offset + 0.75, end=offset + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=offset + 1.875, end=offset + 2.0)
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=offset, end=offset + 0.375)
    pretty_midi.Note(velocity=90, pitch=42, start=offset + 0.375, end=offset + 0.75)
    pretty_midi.Note(velocity=90, pitch=42, start=offset + 0.75, end=offset + 1.125)
    pretty_midi.Note(velocity=90, pitch=42, start=offset + 1.125, end=offset + 1.5)
    pretty_midi.Note(velocity=90, pitch=42, start=offset + 1.5, end=offset + 1.875)
    pretty_midi.Note(velocity=90, pitch=42, start=offset + 1.875, end=offset + 2.25)
    pretty_midi.Note(velocity=90, pitch=42, start=offset + 2.25, end=offset + 2.625)
    pretty_midi.Note(velocity=90, pitch=42, start=offset + 2.625, end=offset + 3.0)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
