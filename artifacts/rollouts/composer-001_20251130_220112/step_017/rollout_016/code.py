
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

# Bass line (Marcus) - walking line in Fm with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),  # Gb
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=61, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),  # Gb
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F7
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=70, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=70, pitch=72, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=70, pitch=74, start=2.25, end=2.625), # Eb
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=70, pitch=67, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=70, pitch=72, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=70, pitch=74, start=3.75, end=4.125), # Eb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=70, pitch=67, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=70, pitch=72, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=70, pitch=74, start=5.25, end=5.625), # Eb
]
piano.notes.extend(piano_notes)

# Sax (Dante) - short motif starting at bar 2, leave it hanging, come back to finish
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # A
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # A
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0), # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start_time = bar * 1.5
    end_time = start_time + 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=end_time)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * 0.1875, end=start_time + (i + 1) * 0.1875)

drums.notes.extend([n for n in drum_notes if n.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
