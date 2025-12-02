
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line in Fm (F, Gb, Ab, Bb, B, C, Db, Eb)
# Starting on F, walking down chromatically
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# Fm7, Bbm7, Eb7, Ab7, but only on 2 and 4
piano_notes = [
    # Fm7 on beat 2 (1.875 - 2.25)
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),  # Db
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25),  # F
    # Eb7 on beat 4 (2.625 - 3.0)
    pretty_midi.Note(velocity=90, pitch=56, start=2.625, end=3.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Motif starts on beat 2 (1.875), ends on beat 4 (3.0)
# Open F, Ab, Bb, F (melodic line)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),   # F (hanging)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Continue walking line (C, Db, Eb, F)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=59, start=3.375, end=3.75), # Db
    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# Ab7 on beat 2 (3.375 - 3.75)
# Db7 on beat 4 (4.125 - 4.5)
piano_notes = [
    # Ab7 on beat 2
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),   # Ab
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.75),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),   # Bb
    pretty_midi.Note(velocity=90, pitch=58, start=3.375, end=3.75),   # Eb
    # Db7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),    # Db
    pretty_midi.Note(velocity=90, pitch=66, start=4.125, end=4.5),    # F
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),    # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),    # Ab
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Motif variation (Ab, Bb, C, Ab)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),   # Ab (hanging)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Continue walking
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # Gb
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# Fm7 on beat 2 (4.875 - 5.25)
# Bbm7 on beat 4 (5.625 - 6.0)
piano_notes = [
    # Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),  # Db
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.25),  # F
    # Bbm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=51, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=46, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=90, pitch=49, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=6.0),   # Ab
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Final motif, resolve the hanging note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=6.0, end=6.375),   # F
]

for note in sax_notes:
    sax.notes.append(note)

# Drums continue in bar 3 and 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.75),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
