
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

# Add drum notes
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax: Fm7 -> Bb -> Fm7 (start on beat 1, leave it hanging)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # Ab (3rd)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # F (root)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # Ab (3rd)
]

# Bass: Walking line in Fm (F, Gb, Ab, A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=80, pitch=68, start=2.625, end=3.0),  # A
]

# Piano: F7 on beat 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # Eb

    # Bar 2, beat 4: F7
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # Eb
]

# Add notes to instruments
for note in sax_notes:
    sax.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax: Fm7 -> Gb -> Fm7 (return to motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # Ab
]

# Bass: Walking line in Fm (Bb, B, C, D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),  # D
]

# Piano: F7 on beat 2 and 4
piano_notes = [
    # Bar 3, beat 2: F7
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # Eb

    # Bar 3, beat 4: F7
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),   # Eb
]

# Add notes to instruments
for note in sax_notes:
    sax.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Sax: Fm7 -> Bb -> Fm7 (resolve the motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # Ab
]

# Bass: Walking line in Fm (Eb, F, Gb, Ab)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.625), # Gb
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),  # Ab
]

# Piano: F7 on beat 2 and 4
piano_notes = [
    # Bar 4, beat 2: F7
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # Eb

    # Bar 4, beat 4: F7
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),   # C
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),   # Eb
]

# Add notes to instruments
for note in sax_notes:
    sax.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

# Add drum notes for bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_shorter_intro.mid')
