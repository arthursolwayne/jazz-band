
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.6875),  # Fm7: F, Ab, Bb, D
    pretty_midi.Note(velocity=100, pitch=61, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),   # D
    pretty_midi.Note(velocity=100, pitch=59, start=2.0, end=2.1875),  # F (repeat)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm (F, Gb, Ab, A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=54, start=1.6875, end=1.875), # Gb
    pretty_midi.Note(velocity=80, pitch=56, start=1.875, end=2.0),   # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=2.0, end=2.1875),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (Ab7 on 2, D7 on 4)
piano_notes = [
    # Ab7 on beat 2 (1.875s)
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.0),  # Ab
    pretty_midi.Note(velocity=85, pitch=67, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=75, pitch=69, start=1.875, end=2.0),  # D
    # D7 on beat 4 (2.1875s)
    pretty_midi.Note(velocity=90, pitch=62, start=2.1875, end=2.375),  # D
    pretty_midi.Note(velocity=85, pitch=66, start=2.1875, end=2.375),  # F#
    pretty_midi.Note(velocity=80, pitch=64, start=2.1875, end=2.375),  # A
    pretty_midi.Note(velocity=75, pitch=68, start=2.1875, end=2.375),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax: Continue the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=3.1875, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=100, pitch=59, start=3.5625, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=3.9375),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.9375, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=59, start=4.125, end=4.3125), # F
    pretty_midi.Note(velocity=100, pitch=61, start=4.3125, end=4.5),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=80, pitch=59, start=3.1875, end=3.375), # B
    pretty_midi.Note(velocity=80, pitch=56, start=3.375, end=3.5625), # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=3.5625, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=3.9375),  # F
    pretty_midi.Note(velocity=80, pitch=54, start=3.9375, end=4.125), # Gb
    pretty_midi.Note(velocity=80, pitch=56, start=4.125, end=4.3125), # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=4.3125, end=4.5),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (Bb7 on 2, E7 on 4)
piano_notes = [
    # Bb7 on beat 2 (3.875s)
    pretty_midi.Note(velocity=90, pitch=61, start=3.875, end=4.0),  # Bb
    pretty_midi.Note(velocity=85, pitch=65, start=3.875, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=3.875, end=4.0),  # C
    pretty_midi.Note(velocity=75, pitch=67, start=3.875, end=4.0),  # F
    # E7 on beat 4 (4.1875s)
    pretty_midi.Note(velocity=90, pitch=60, start=4.1875, end=4.375),  # E
    pretty_midi.Note(velocity=85, pitch=64, start=4.1875, end=4.375),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=4.1875, end=4.375),  # A
    pretty_midi.Note(velocity=75, pitch=66, start=4.1875, end=4.375),  # B
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bars 3-4 already handled

# Bar 4: Full quartet (4.5 - 6.0s)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.6875, end=4.875), # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=100, pitch=61, start=5.0625, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.4375),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.4375, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=5.8125), # F
    pretty_midi.Note(velocity=100, pitch=61, start=5.8125, end=6.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=58, start=4.5, end=4.6875),  # Bb
    pretty_midi.Note(velocity=80, pitch=59, start=4.6875, end=4.875), # B
    pretty_midi.Note(velocity=80, pitch=56, start=4.875, end=5.0625), # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=5.0625, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.4375),  # F
    pretty_midi.Note(velocity=80, pitch=54, start=5.4375, end=5.625), # Gb
    pretty_midi.Note(velocity=80, pitch=56, start=5.625, end=5.8125), # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=5.8125, end=6.0),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (G7 on 2, C7 on 4)
piano_notes = [
    # G7 on beat 2 (5.375s)
    pretty_midi.Note(velocity=90, pitch=67, start=5.375, end=5.5625),  # G
    pretty_midi.Note(velocity=85, pitch=71, start=5.375, end=5.5625),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=5.375, end=5.5625),  # Bb
    pretty_midi.Note(velocity=75, pitch=72, start=5.375, end=5.5625),  # D
    # C7 on beat 4 (5.6875s)
    pretty_midi.Note(velocity=90, pitch=60, start=5.6875, end=5.875),  # C
    pretty_midi.Note(velocity=85, pitch=64, start=5.6875, end=5.875),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=5.6875, end=5.875),  # G
    pretty_midi.Note(velocity=75, pitch=67, start=5.6875, end=5.875),  # B
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bars 4
start = 4.5
# Kick on 1 and 3
pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
# Hihat on every eighth
for i in range(8):
    pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_introduction.mid')
