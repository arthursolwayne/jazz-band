
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Fm motif (F, Ab, Bb, D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=2.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),   # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),   # F
    pretty_midi.Note(velocity=100, pitch=61, start=2.75, end=3.0),   # Ab
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.75, end=2.0),   # Eb
    pretty_midi.Note(velocity=80, pitch=46, start=2.0, end=2.25),   # D
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.5),   # G
    pretty_midi.Note(velocity=80, pitch=48, start=2.5, end=2.75),   # F
    pretty_midi.Note(velocity=80, pitch=47, start=2.75, end=3.0),   # Eb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),   # D
    # Bar 2: Fm7 on 4
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),   # F
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),   # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Motif variation (Ab, Bb, D, F)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.25),   # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),   # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),   # F
    pretty_midi.Note(velocity=100, pitch=61, start=4.0, end=4.25),   # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),   # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),   # G
    pretty_midi.Note(velocity=80, pitch=48, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=80, pitch=47, start=3.5, end=3.75),   # Eb
    pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=80, pitch=50, start=4.0, end=4.25),   # G
    pretty_midi.Note(velocity=80, pitch=48, start=4.25, end=4.5),   # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Fm7 on 2
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),   # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),   # D
    # Bar 3: Fm7 on 4
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),   # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Motif conclusion (F, Ab, Bb, D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=100, pitch=61, start=4.75, end=5.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),   # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=100, pitch=61, start=5.75, end=6.0),   # Ab
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=80, pitch=50, start=4.75, end=5.0),   # G
    pretty_midi.Note(velocity=80, pitch=48, start=5.0, end=5.25),   # F
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.5),   # Eb
    pretty_midi.Note(velocity=80, pitch=46, start=5.5, end=5.75),   # D
    pretty_midi.Note(velocity=80, pitch=50, start=5.75, end=6.0),   # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: Fm7 on 2
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),   # F
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),   # D
    # Bar 4: Fm7 on 4
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),   # F
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),   # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# Add more hihat in bar 4
drum_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("wayne_intro.mid")
