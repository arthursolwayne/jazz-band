
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=90, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.125),  # C#
    pretty_midi.Note(velocity=90, pitch=63, start=2.125, end=2.5),   # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.875),   # E
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=65, start=2.875, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.625),  # G
    pretty_midi.Note(velocity=90, pitch=66, start=3.625, end=4.0),   # Gb
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.375),   # E
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.375, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=4.75, end=5.125),  # C#
    pretty_midi.Note(velocity=90, pitch=63, start=5.125, end=5.5),   # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=6.0),     # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # B
    pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=64, start=2.875, end=3.25),  # E
    pretty_midi.Note(velocity=80, pitch=69, start=2.875, end=3.25),  # A
    pretty_midi.Note(velocity=80, pitch=73, start=2.875, end=3.25),  # C
    pretty_midi.Note(velocity=80, pitch=76, start=2.875, end=3.25),  # E
    pretty_midi.Note(velocity=80, pitch=71, start=2.875, end=3.25),  # B
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=62, start=4.375, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.375, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=4.375, end=4.75),  # B
    pretty_midi.Note(velocity=80, pitch=74, start=4.375, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=70, start=4.375, end=4.75),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Motif in D minor, short and emotional
sax_notes = [
    # Bar 2: Motif starts
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),   # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),   # D
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=65, start=2.875, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),   # G
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=64, start=4.375, end=4.625), # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.625, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.125), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.125, end=5.375), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.375, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),   # F
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick3])
# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    drums.notes.extend([snare2, snare4])
# Hi-hat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.125, end=start + (i + 1) * 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
