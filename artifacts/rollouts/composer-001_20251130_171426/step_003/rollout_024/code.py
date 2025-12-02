
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

# Bass: Walking line in Fm, chromatic approaches, no repeating notes
# Fm: F, Ab, Db, Eb
# Walking line: F, Gb, Ab, G, A, Bb, Db, C, Eb, D, F, E, Gb, F

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.0),   # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.125),   # A
    pretty_midi.Note(velocity=80, pitch=67, start=2.125, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.375),  # Db
    pretty_midi.Note(velocity=80, pitch=65, start=2.375, end=2.5),   # C
    pretty_midi.Note(velocity=80, pitch=66, start=2.5, end=2.625),   # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=2.875, end=3.0),   # E
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.125),   # Gb
    pretty_midi.Note(velocity=80, pitch=65, start=3.125, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=3.375, end=3.5),   # G
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=3.625),   # Ab
    pretty_midi.Note(velocity=80, pitch=68, start=3.625, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=3.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=3.875, end=4.0),   # Db
    pretty_midi.Note(velocity=80, pitch=65, start=4.0, end=4.125),   # C
    pretty_midi.Note(velocity=80, pitch=66, start=4.125, end=4.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.375),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=4.375, end=4.5),   # F
    pretty_midi.Note(velocity=80, pitch=66, start=4.5, end=4.625),   # E
    pretty_midi.Note(velocity=80, pitch=64, start=4.625, end=4.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),    # F
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7: F, Ab, C, Eb (F7: F, Ab, Bb, Db)
# Bars 2-4: Fm7, Bb7, Eb7, Ab7

# Bar 2: Fm7 on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=85, pitch=69, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=85, pitch=66, start=1.75, end=2.0),  # Eb
]

# Bar 3: Bb7 on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=85, pitch=62, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=85, pitch=64, start=2.75, end=3.0),  # Db
    pretty_midi.Note(velocity=85, pitch=67, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=85, pitch=66, start=2.75, end=3.0),  # Ab
])

# Bar 4: Eb7 on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=85, pitch=59, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=85, pitch=61, start=3.75, end=4.0),  # Gb
    pretty_midi.Note(velocity=85, pitch=64, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=85, pitch=62, start=3.75, end=4.0),  # Db
])

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Motif: F, Ab, Bb, F (Fm with a chromatic passing tone)
# Play on 1 & 3 of bar 2, then 1 & 3 of bar 4

# Bar 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0),   # F
]

# Bar 3: Rest
# Bar 4
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=4.625, end=4.75),  # Gb
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.0),   # F
])

sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

for bar in range(2, 5):
    start_bar = bar * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_bar + 0.0, end=start_bar + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_bar + 1.125, end=start_bar + 1.5))
    
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start_bar + 0.75, end=start_bar + 0.875))
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start_bar + 1.875, end=start_bar + 2.0))
    
    # Hi-hat on every eighth
    for i in range(0, 4):
        start = start_bar + i * 0.375
        end = start + 0.125
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
