
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=65, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=65, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0)
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.75),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),  # C
    # Bar 3 (2.0 - 2.5)
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.5),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.5),  # C
    # Bar 4 (2.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=70, start=2.75, end=3.0),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=2.75, end=3.0),  # C
    # Bar 4 (3.0 - 3.5)
    pretty_midi.Note(velocity=100, pitch=70, start=3.5, end=3.75),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.75),  # C
    # Bar 4 (4.0 - 4.5)
    pretty_midi.Note(velocity=100, pitch=70, start=4.25, end=4.5),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.25, end=4.5),  # C
    # Bar 4 (4.5 - 5.0)
    pretty_midi.Note(velocity=100, pitch=70, start=4.75, end=5.0),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=5.0),  # C
    # Bar 4 (5.0 - 5.5)
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.5),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.5),  # C
    # Bar 4 (5.5 - 6.0)
    pretty_midi.Note(velocity=100, pitch=70, start=5.75, end=6.0),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=72, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=5.75, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.75, end=6.0),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 -> G7 -> Cmaj7 -> F7 (comping) then Sax line on Dm7
sax_notes = [
    # Bar 2 (1.5 - 2.0)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),  # A
    # Bar 3 (2.0 - 2.5)
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.125, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.375, end=2.5),  # F
    # Bar 4 (2.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.875, end=3.0),  # Bb
    # Bar 4 (3.0 - 3.5)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),  # D
    # Bar 4 (4.5 - 5.0)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0),  # A
    # Bar 4 (5.0 - 5.5)
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.125),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.125, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.375, end=5.5),  # F
    # Bar 4 (5.5 - 6.0)
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=5.875),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.875, end=6.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Additional drums for bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
