
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: Dm7 - D, F, G, C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),    # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # Bb
    # Bar 3: Am7 - A, C, D, G
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),    # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # F
    # Bar 4: Dm7 - D, F, G, C
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),    # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),   # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),    # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),    # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),    # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),    # G
    # Bar 3: Am7
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),    # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),    # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),    # C
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),    # G
    # Bar 4: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),    # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),    # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),    # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),    # G
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.

# Bar 2: Start motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6875),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0625), # D
]

# Bar 3: Leave it hanging
sax_notes.append(pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.1875))  # G

# Bar 4: Come back and finish it
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.6875),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=4.6875, end=4.875), # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.0625, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.4375),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.4375, end=5.625), # D
])

sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 2
for i in range(4):
    start = 1.5 + i * 0.375
    if i == 0 or i == 2:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    elif i == 1 or i == 3:
        drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875))

# Bar 3
for i in range(4):
    start = 3.0 + i * 0.375
    if i == 0 or i == 2:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    elif i == 1 or i == 3:
        drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875))

# Bar 4
for i in range(4):
    start = 4.5 + i * 0.375
    if i == 0 or i == 2:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    elif i == 1 or i == 3:
        drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
