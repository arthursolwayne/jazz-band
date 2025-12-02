
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus (bass): Walking line, chromatic approaches, never the same note twice. Dm7 -> G7 -> Cm7 -> F7
# Dm7: D F A C
# G7: G B D F
# Cm7: C Eb G Bb
# F7: F A C Eb

# Bar 2: Dm7
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),   # C
]

# Bar 3: G7
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5),   # F
])

# Bar 4: Cm7
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),   # Bb
])

for note in bass_notes:
    bass.notes.append(note)

# Diane (piano): 7th chords, comp on 2 and 4. Dm7 -> G7 -> Cm7 -> F7
# Bar 2: Dm7 (comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25),  # D
]

# Bar 3: G7 (comp on 2 and 4)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),  # F
])

# Bar 4: Cm7 (comp on 2 and 4)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),  # C
])

for note in piano_notes:
    piano.notes.append(note)

# Dante (sax): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Melody starts with a sparse motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),    # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125),   # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.625),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=2.875),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),   # A
]

for note in sax_notes:
    sax.notes.append(note)

# Add dynamics to sax and piano
for note in sax.notes:
    note.velocity = 100 if note.start % 0.375 < 0.15 else 90

for note in piano.notes:
    note.velocity = 80

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
