
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    # Kick on 1 and 3 (0.0, 0.75, 1.5, 2.25, etc.)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    # Hi-hats on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=77, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=80, pitch=79, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=81, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625), # D

    # Bar 3: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125), # D

    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625), # D
]
piano.notes.extend(piano_notes)

# Sax: Your moment
# Motif: D, Bb, B, D (start on bar 2 beat 1)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=77, start=4.125, end=4.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: continue for bars 2-4
for bar in range(2, 4):
    start = 1.5 + (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5),
    # Hi-hats on every eighth note
    for i in range(4):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
