
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Start with sax melody

# sax motif: Fm7 -> Ab7 -> Bb7 -> Cm7
# Fm7: F, Ab, Db, Eb
# Ab7: Ab, C, Eb, Gb
# Bb7: Bb, D, F, Ab
# Cm7: C, Eb, G, Bb

# Bar 2 (1.5 - 3.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0),  # Ab (E4)
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # Db (C4)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # Eb (Bb4)
    pretty_midi.Note(velocity=100, pitch=68, start=2.5, end=2.75),  # Ab (E4)
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # C (C4)
]

# Bar 3 (3.0 - 4.5s)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # Eb (Bb4)
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # Db (C4)
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.0),  # Ab (E4)
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),  # C (C4)
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # Eb (Bb4)
])

# Bar 4 (4.5 - 6.0s)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # Db (C4)
    pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=5.0),  # Ab (E4)
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # C (C4)
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # Eb (Bb4)
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # G (C4)
])

for note in sax_notes:
    sax.notes.append(note)

# Marcus: Walking line in Fm (F, Gb, Ab, A, Bb, B, C, Db)
# Bars 2-4 (1.5 - 6.0s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),  # F (C4)
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),  # Gb (Bb4)
    pretty_midi.Note(velocity=80, pitch=68, start=2.0, end=2.25),  # Ab (E4)
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),  # A (F4)
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.75),  # Bb (Eb4)
    pretty_midi.Note(velocity=80, pitch=68, start=2.75, end=3.0),  # B (F4)
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.25),  # C (C4)
    pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.5),  # Db (C4)
    pretty_midi.Note(velocity=80, pitch=65, start=3.5, end=3.75),  # F (C4)
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0),  # Gb (Bb4)
    pretty_midi.Note(velocity=80, pitch=68, start=4.0, end=4.25),  # Ab (E4)
    pretty_midi.Note(velocity=80, pitch=69, start=4.25, end=4.5),  # A (F4)
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),  # Bb (Eb4)
    pretty_midi.Note(velocity=80, pitch=68, start=4.75, end=5.0),  # B (F4)
    pretty_midi.Note(velocity=80, pitch=60, start=5.0, end=5.25),  # C (C4)
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.5),  # Db (C4)
    pretty_midi.Note(velocity=80, pitch=65, start=5.5, end=5.75),  # F (C4)
    pretty_midi.Note(velocity=80, pitch=64, start=5.75, end=6.0),  # Gb (Bb4)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
# Bar 2 (1.5 - 3.0s): Fm7 on 2, Ab7 on 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # Eb (Bb4)
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=68, start=1.75, end=2.0),  # Ab (E4)
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # Db (C4)
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.5),  # Ab (E4)
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),  # C (C4)
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # Eb (Bb4)
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=68, start=2.75, end=3.0),  # Ab (E4)
    pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=3.0),  # C (C4)
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # Eb (Bb4)
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0),  # F (C4)
]

# Bar 3 (3.0 - 4.5s): Bb7 on 2, Cm7 on 4
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # Bb (F4)
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),  # D (C4)
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # F (Bb4)
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.0),  # Ab (E4)
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.5),  # C (C4)
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),  # Eb (Bb4)
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),  # G (F4)
    pretty_midi.Note(velocity=90, pitch=68, start=4.25, end=4.5),  # Ab (E4)
])

# Bar 4 (4.5 - 6.0s): Fm7 on 2, Ab7 on 4
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),  # Eb (Bb4)
    pretty_midi.Note(velocity=90, pitch=65, start=5.75, end=6.0),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=68, start=5.75, end=6.0),  # Ab (E4)
    pretty_midi.Note(velocity=90, pitch=60, start=5.75, end=6.0),  # Db (C4)
])

for note in piano_notes:
    piano.notes.append(note)

# Add remaining drum patterns for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    for i in range(4):
        time = start + i * 0.375
        if i == 0 or i == 2:  # Kick on 1 and 3
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))
        if i == 1 or i == 3:  # Snare on 2 and 4
            drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.375))
        # Hi-hat on every eighth
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("4_bar_intro.mid")
