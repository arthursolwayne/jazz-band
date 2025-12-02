
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
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drums_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: F7, G7, A7, Bb7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=89, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=91, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=90, start=2.25, end=2.5),
]
sax.notes.extend(sax_notes)

# Bass line: F, Ab, Bb, C
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=53, start=1.5, end=1.75),
    pretty_midi.Note(velocity=70, pitch=55, start=1.75, end=2.0),
    pretty_midi.Note(velocity=70, pitch=56, start=2.0, end=2.25),
    pretty_midi.Note(velocity=70, pitch=57, start=2.25, end=2.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=57, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),
    # Bar 3: A7 on beat 2
    pretty_midi.Note(velocity=90, pitch=58, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: F7, G7, A7, Bb7 (repeat)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=89, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=91, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=90, start=3.75, end=4.0),
]
sax.notes.extend(sax_notes)

# Bass line: F, Ab, Bb, C (repeat)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=53, start=3.0, end=3.25),
    pretty_midi.Note(velocity=70, pitch=55, start=3.25, end=3.5),
    pretty_midi.Note(velocity=70, pitch=56, start=3.5, end=3.75),
    pretty_midi.Note(velocity=70, pitch=57, start=3.75, end=4.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=57, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),
    # Bar 4: Bb7 on beat 2
    pretty_midi.Note(velocity=90, pitch=57, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=61, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=66, start=4.25, end=4.5),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: F7, G7, A7, Bb7 (repeat)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=89, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=91, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=90, start=5.25, end=5.5),
]
sax.notes.extend(sax_notes)

# Bass line: F, Ab, Bb, C (repeat)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=53, start=4.5, end=4.75),
    pretty_midi.Note(velocity=70, pitch=55, start=4.75, end=5.0),
    pretty_midi.Note(velocity=70, pitch=56, start=5.0, end=5.25),
    pretty_midi.Note(velocity=70, pitch=57, start=5.25, end=5.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=57, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),
    # Bar 4: Bb7 on beat 4
    pretty_midi.Note(velocity=90, pitch=57, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=61, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=66, start=5.5, end=5.75),
]
piano.notes.extend(piano_notes)

# Drums for Bars 2-4 (1.5 - 6.0s)
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.0, end=start + 0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.3125, end=start + 1.5),
    # Add to drums
    drums.notes.extend([
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.0, end=start + 0.1875),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.1875, end=start + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.5625),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.5625, end=start + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 0.9375),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.9375, end=start + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.3125),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 1.3125, end=start + 1.5),
    ])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
