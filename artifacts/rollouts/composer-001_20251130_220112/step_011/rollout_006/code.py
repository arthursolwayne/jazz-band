
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.0, end=0.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),   # D (root)
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb (chromatic)
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),  # C (bass note)
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),   # D (root)

    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),   # F (third)
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.75),  # Eb (chromatic)
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),  # C (bass note)
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # D (root)

    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),   # D (root)
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25),  # Eb (chromatic)
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),  # C (bass note)
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),   # D (root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=70, start=1.5, end=1.875),  # F7 (Bb) on 1
    pretty_midi.Note(velocity=95, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=77, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=65, start=1.875, end=2.25),  # Dm7 on 2
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=70, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=72, start=1.875, end=2.25),

    # Bar 3
    pretty_midi.Note(velocity=95, pitch=70, start=2.25, end=2.625),  # F7 (Bb) on 1
    pretty_midi.Note(velocity=95, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=95, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=95, pitch=77, start=2.25, end=2.625),
    pretty_midi.Note(velocity=95, pitch=65, start=2.625, end=3.0),   # Dm7 on 2
    pretty_midi.Note(velocity=95, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=95, pitch=70, start=2.625, end=3.0),
    pretty_midi.Note(velocity=95, pitch=72, start=2.625, end=3.0),

    # Bar 4
    pretty_midi.Note(velocity=95, pitch=70, start=3.0, end=3.375),   # F7 (Bb) on 1
    pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=77, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=65, start=3.375, end=3.75),  # Dm7 on 2
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=70, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=70, start=4.125, end=4.5),   # F7 (Bb) on 3
    pretty_midi.Note(velocity=95, pitch=72, start=4.125, end=4.5),
    pretty_midi.Note(velocity=95, pitch=74, start=4.125, end=4.5),
    pretty_midi.Note(velocity=95, pitch=77, start=4.125, end=4.5),
    pretty_midi.Note(velocity=95, pitch=65, start=4.5, end=4.875),   # Dm7 on 4
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=70, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Short motif, sing it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.125, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375), # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.75), # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=2.875), # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.875, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.25), # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.625),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.625, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=3.875), # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.0),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start, end=bar_start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)

    drums.notes.append(kick1)
    drums.notes.append(snare2)
    drums.notes.append(hihat1)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)
    drums.notes.append(hihat4)
    drums.notes.append(kick3)
    drums.notes.append(snare4)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
