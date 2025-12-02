
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches, no repeated notes
# Fm: F, Ab, D, C, Bb, Eb, G, Db
# Walking bass: F -> G -> Ab -> A -> Bb -> B -> C -> Db -> D -> Eb -> F

bass_notes = [
    (1.5, 76),  # F
    (1.75, 77),  # G
    (2.0, 77),   # Ab
    (2.25, 78),  # A
    (2.5, 76),   # Bb
    (2.75, 77),  # B
    (3.0, 72),   # C
    (3.25, 71),  # Db
    (3.5, 74),   # D
    (3.75, 73),  # Eb
    (4.0, 76),   # F
    (4.25, 77),  # G
    (4.5, 77),   # Ab
    (4.75, 78),  # A
    (5.0, 76),   # Bb
    (5.25, 77),  # B
    (5.5, 72),   # C
    (5.75, 71),  # Db
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25))

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, D, F, Ab
# Eb7 = Eb, G, Bb, D
# Ab7 = Ab, C, Eb, G

# Bar 2: Fm7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=2.0, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=79, start=2.0, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=2.0, end=2.25))

# Bar 3: Bb7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.25))

# Bar 4: Eb7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=4.0, end=4.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=4.0, end=4.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Motif: F (76) -> Ab (77) -> C (79) -> F (76)
# Start at 1.5s, end at 2.0s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=1.75, end=2.0))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=2.0, end=2.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.75))

# Hi-hat on every eighth
for i in range(0, 8):
    start = 1.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Kick on 1 and 3 of bars 2-4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.0, end=5.375))

# Snare on 2 and 4 of bars 2-4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=2.75, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.0, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.75, end=5.875))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])
