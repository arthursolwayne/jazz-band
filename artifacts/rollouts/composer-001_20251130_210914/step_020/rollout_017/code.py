
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    # Dm7 walking bass: D - C - Bb - C - D - Eb - D - C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=2.75, end=3.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.75, end=6.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Dm7 on 1: D, F, A, C
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=95, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.75),
    # Dm7 on 3: D, F, A, C
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=95, pitch=65, start=3.0, end=3.25),
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.25),
    # Dm7 on 5: D, F, A, C
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=95, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.75),
    # Dm7 on 7: D, F, A, C
    pretty_midi.Note(velocity=95, pitch=62, start=6.0, end=6.25),
    pretty_midi.Note(velocity=95, pitch=65, start=6.0, end=6.25),
    pretty_midi.Note(velocity=95, pitch=67, start=6.0, end=6.25),
    pretty_midi.Note(velocity=95, pitch=69, start=6.0, end=6.25),
]
for note in piano_notes:
    piano.notes.append(note)

# You: Tenor sax, one short motif, start it, leave it hanging, come back and finish it.
sax_notes = [
    # Motif: D - Eb - C - D (hanging on C)
    pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=105, pitch=63, start=1.625, end=1.75),
    pretty_midi.Note(velocity=105, pitch=60, start=1.75, end=1.875),
    # Return and finish the motif
    pretty_midi.Note(velocity=105, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=105, pitch=63, start=3.125, end=3.25),
    pretty_midi.Note(velocity=105, pitch=60, start=3.25, end=3.375),
    pretty_midi.Note(velocity=105, pitch=62, start=3.375, end=3.5),
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_intro.mid')
