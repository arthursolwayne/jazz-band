
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

# Bar 2 (1.5 - 3.0s): Full quartet enters

# Bass: Walking line in Fm (F, Gb, Ab, A, Bb, B, C, Db)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # A
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),
    # Bar 3: Bb7 (Bb, Db, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.75),
    # Bar 4: Fm7 again
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25),
]

piano.notes.extend(piano_notes)

# Sax: Motif in Fm
# Start with F (64), then Ab (61), then a chromatic approach to Bb (62)
# Leave it hanging on the Ab (61)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=61, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.875),  # Bb (approach)
    pretty_midi.Note(velocity=110, pitch=61, start=1.875, end=2.0),   # Ab (hang)
    # Come back and finish it on the next bar
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=110, pitch=61, start=3.125, end=3.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.375),  # Bb (finish)
]

sax.notes.extend(sax_notes)

# Drums continue for bars 2-4
# Bar 2 (1.5 - 3.0s)
for i in range(4):
    start = 1.5 + i * 0.375
    end = start + 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=end))  # Kick
    else:
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start, end=end))  # Snare
for i in range(8):
    start = 1.5 + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))  # Hi-hat

# Bar 3 (3.0 - 4.5s)
for i in range(4):
    start = 3.0 + i * 0.375
    end = start + 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=end))  # Kick
    else:
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start, end=end))  # Snare
for i in range(8):
    start = 3.0 + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))  # Hi-hat

# Bar 4 (4.5 - 6.0s)
for i in range(4):
    start = 4.5 + i * 0.375
    end = start + 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=end))  # Kick
    else:
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start, end=end))  # Snare
for i in range(8):
    start = 4.5 + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))  # Hi-hat

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
