
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),  # Gb
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F7
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.6875),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=1.6875, end=1.875),  # E
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875),  # Bb
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=4.6875, end=4.875),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    kick_start = start
    kick_end = start + 0.375
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=kick_start + 1.125, end=kick_start + 1.5)
    drums.notes.append(kick1)
    drums.notes.append(kick2)

# Snare on 2 and 4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    snare_start = start + 0.75
    snare_end = start + 0.875
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=snare_start + 1.5, end=snare_start + 1.625)
    drums.notes.append(snare1)
    drums.notes.append(snare2)

# Hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    for i in range(4):
        hihat_start = start + i * 0.375
        hihat_end = hihat_start + 0.375
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
