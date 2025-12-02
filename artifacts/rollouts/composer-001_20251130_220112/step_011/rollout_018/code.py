
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches, no repeated notes
# Dm: D F A C
# Walking line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=80, pitch=68, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=80, pitch=70, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=80, pitch=68, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=5.75, end=6.0),  # Eb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Dm7: D F A C
# F7: F A C Eb
# Bb7: Bb D F A
# G7: G B D F

# Bar 2 (1.5 - 2.0s): Dm7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0))  # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=1.75, end=2.0))  # C

# Bar 3 (2.5 - 3.0s): F7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=3.0))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=2.75, end=3.0))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=2.75, end=3.0))  # Eb

# Bar 4 (4.0 - 4.5s): Bb7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.5))  # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.25, end=4.5))  # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.5))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.5))  # A

# Bar 4 (5.0 - 5.5s): G7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5))  # G
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5))  # B
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.5))  # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.5))  # F

# Sax: Motif in Dm. Start it, leave it hanging, come back and finish it.

# Bar 2: Start motif (1.5 - 2.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # B
]

# Bar 3: Leave it hanging (2.5 - 3.0s)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75))  # A

# Bar 4: Come back and finish it (5.0 - 5.5s)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25))  # F
sax_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5))  # A
sax_notes.append(pretty_midi.Note(velocity=100, pitch=70, start=5.5, end=5.75))  # C
sax_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=5.75, end=6.0))  # D

for note in sax_notes:
    sax.notes.append(note)

# Drums: Continue for bars 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=2.0, end=2.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=4.0, end=4.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=5.0, end=5.375))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=2.375, end=2.5))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.5))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=4.375, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=5.375, end=5.5))

# Hihat on every eighth
for i in range(4, 16):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
