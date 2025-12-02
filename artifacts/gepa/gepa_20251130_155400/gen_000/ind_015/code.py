
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet starts
# Sax: Simple motif in Dm (D F A C)
# D on 1, F on 2, A on 3, C on 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # C
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm (D F C A G Bb F D)
# Each note on beat
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Dm7 on 2 (D F A C)
# Gm7 on 4 (G Bb D F)
piano_notes = [
    # Dm7 on 2 (1.875 - 2.25)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),
    # Gm7 on 4 (2.625 - 3.0)
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Bar 3: Sax returns to finish the motif (D F A C)
# Delayed resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5),  # C
]
sax.notes.extend(sax_notes)

# Bass: Walking line (D F C A G Bb F D)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Dm7 on 2 (3.375 - 3.75)
# Gm7 on 4 (4.125 - 4.5)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Bar 4: Drums continue, sax rests, bass resolves
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Bass resolves on D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),
]
bass.notes.extend(bass_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
