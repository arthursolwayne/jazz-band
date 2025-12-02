
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
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Start with saxophone

# Sax: Fm7 -> Bb -> Eb -> Ab (Fm scale, but with a syncopated feel)
bar_duration = 1.5
start_time = 1.5

# Bar 2 (1.5 - 3.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3 (3.0 - 4.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # Eb
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4 (4.5 - 6.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bass (Marcus): Walking line in Fm, chromatic approaches, no repeats
bass_notes = [
    # Bar 2: F - Gb - G - Ab
    pretty_midi.Note(velocity=90, pitch=47, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=48, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=49, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.5),
    # Bar 3: Bb - C - Db - D
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=55, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=56, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.0),
    # Bar 4: F - Gb - G - Ab
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=48, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=49, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
# Bar 2: Fm7 on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on 2 (1.75 - 2.0)
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # G
    # Bar 2: Fm7 on 4 (2.75 - 3.0)
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # G
    # Bar 3: Fm7 on 2 (3.75 - 4.0)
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # G
    # Bar 3: Fm7 on 4 (4.75 - 5.0)
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # G
    # Bar 4: Fm7 on 2 (5.75 - 6.0)
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0
kick_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
]
snare_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
]
hihat_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
]

for note in kick_notes:
    drums.notes.append(note)
for note in snare_notes:
    drums.notes.append(note)
for note in hihat_notes:
    drums.notes.append(note)

# Bar 3: 3.0 - 4.5
kick_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
]
snare_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
]
hihat_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in kick_notes:
    drums.notes.append(note)
for note in snare_notes:
    drums.notes.append(note)
for note in hihat_notes:
    drums.notes.append(note)

# Bar 4: 4.5 - 6.0
kick_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
]
snare_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
]
hihat_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5),
]

for note in kick_notes:
    drums.notes.append(note)
for note in snare_notes:
    drums.notes.append(note)
for note in hihat_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fminor_intro.mid")
