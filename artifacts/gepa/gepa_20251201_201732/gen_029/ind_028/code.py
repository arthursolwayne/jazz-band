
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F - Gb - G - A (root, b9, 5, b7)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # A
    # Bar 3: Bb - B - C - D (b7, 7, 9, 11)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=78, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=80, start=4.125, end=4.5),  # D
    # Bar 4: F - G - A - Bb (root, 3, 5, b7)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano comping: open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # Eb
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # Ab
    # Bar 4: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # Eb
]
piano.notes.extend(piano_notes)

# Sax melody: short motif, starts on bar 2, leave it hanging, come back and finish it in bar 4
# Motif: F - A - Bb - F (F, A, Bb, F, then back to F)
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),  # F
    # Bar 3: Rest
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),  # F (back to F)
    pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=76, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),  # F
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),  # Hi-hat
]
for i in range(2):
    for note in drum_notes:
        note.start += 2.0 * i
        note.end += 2.0 * i
    drums.notes.extend([note.copy() for note in drum_notes])

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.5),  # Hi-hat
]
for i in range(2):
    for note in drum_notes:
        note.start += 2.0 * i
        note.end += 2.0 * i
    drums.notes.extend([note.copy() for note in drum_notes])

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0),  # Hi-hat
]
for i in range(2):
    for note in drum_notes:
        note.start += 2.0 * i
        note.end += 2.0 * i
    drums.notes.extend([note.copy() for note in drum_notes])

midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled
