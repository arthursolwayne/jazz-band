
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

# Drums - Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# 1. Bass line - Marcus (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),  # C#
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=73, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# 2. Piano - Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # D7 - F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # D7 - A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # D7 - C
    # Bar 3 (2.25 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=2.875),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.875),  # D7 - F
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=2.875),  # D7 - A
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=2.875),  # D7 - C
    # Bar 4 (3.0 - 3.75s)
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.625),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.625),  # D7 - F
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.625),  # D7 - A
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.625),  # D7 - C
    # Bar 4 (3.75 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.375),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.375),  # D7 - F
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.375),  # D7 - A
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.375),  # D7 - C
    # Bar 4 (4.5 - 5.25s)
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.125),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.125),  # D7 - F
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.125),  # D7 - A
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.125),  # D7 - C
]

for note in piano_notes:
    piano.notes.append(note)

# 3. Drums - Little Ray (Bar 2-4)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2, 5):
    start = i * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on each eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.875, end=start + 2.25)

# 4. Sax - Dante (Melody, 1 short motif, make it sing)
# Start with Bb (Dm7 chord), then move to F and a chromatic line
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # Bb -> B
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875),  # B -> C
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0),   # C -> Ab
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.125),  # Ab -> B
    pretty_midi.Note(velocity=110, pitch=69, start=2.125, end=2.25), # B -> C
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.375), # C -> Bb
    pretty_midi.Note(velocity=110, pitch=65, start=2.375, end=2.5),  # Bb -> Ab
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.625),  # Ab -> G
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=2.75), # G -> Bb
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=2.875), # Bb -> C
    pretty_midi.Note(velocity=110, pitch=67, start=2.875, end=3.0),  # C -> B
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.125),  # B -> C
    pretty_midi.Note(velocity=110, pitch=65, start=3.125, end=3.25), # C -> Ab
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.375), # Ab -> G
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.5),  # G -> Bb
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.625),  # Bb -> C
    pretty_midi.Note(velocity=110, pitch=67, start=3.625, end=3.75), # C -> B
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=3.875), # B -> C
    pretty_midi.Note(velocity=110, pitch=65, start=3.875, end=4.0),  # C -> Ab
    pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.125),  # Ab -> G
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.25), # G -> Bb
    pretty_midi.Note(velocity=110, pitch=69, start=4.25, end=4.375), # Bb -> C
    pretty_midi.Note(velocity=110, pitch=67, start=4.375, end=4.5),  # C -> B
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.625),  # B -> C
    pretty_midi.Note(velocity=110, pitch=65, start=4.625, end=4.75), # C -> Ab
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=4.875), # Ab -> G
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.0),  # G -> Bb
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.125),  # Bb -> C
    pretty_midi.Note(velocity=110, pitch=67, start=5.125, end=5.25), # C -> B
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.375), # B -> C
    pretty_midi.Note(velocity=110, pitch=65, start=5.375, end=5.5),  # C -> Ab
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.625),  # Ab -> G
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=5.75), # G -> Bb
    pretty_midi.Note(velocity=110, pitch=69, start=5.75, end=5.875), # Bb -> C
    pretty_midi.Note(velocity=110, pitch=67, start=5.875, end=6.0),  # C -> B
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
