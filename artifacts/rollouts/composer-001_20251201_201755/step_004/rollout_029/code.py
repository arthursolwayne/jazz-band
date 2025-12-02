
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): Walking line (F2-G2, MIDI 40-43), roots and fifths with chromatic approaches
# Bar 2: Fm7 (F, C, Ab, D)
# Bar 3: Bb7 (Bb, F, D, Ab)
# Bar 4: Eb7 (Eb, Bb, G, Db)

# Bar 2: Fm7 - F (40), Ab (44), C (43), D (45)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=44, start=1.75, end=2.0))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=45, start=2.0, end=2.25))

# Bar 3: Bb7 - Bb (42), D (45), F (40), Ab (44)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.5))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.5))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=40, start=2.5, end=2.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=44, start=2.75, end=3.0))

# Bar 4: Eb7 - Eb (43), G (46), Bb (42), Db (43)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.5))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=3.5, end=3.75))

# Piano (Diane): Open voicings, different chord each bar, resolve on the last

# Bar 2: Fm7 - F, Ab, C, D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=2.0))

# Bar 3: Bb7 - Bb, D, F, Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5))

# Bar 4: Eb7 - Eb, G, Bb, Db
piano.notes.append(pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=2.5, end=3.0))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Melody - F (65), Ab (67), Bb (67), D (70)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=70, start=2.25, end=2.5))

# Bar 3: Repeat the motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=70, start=3.25, end=3.5))

# Bar 4: Repeat the motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=70, start=4.25, end=4.5))

# Drums for bars 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.875, end=4.0))

# Hi-hat on every eighth
for i in range(4, 12):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
