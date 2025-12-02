
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

# Kick on 1 and 3
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
]

for note in drums_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # C

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),  # Gb

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # Gb
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, D, F, Ab
# Cm7 = C, Eb, G, Bb
# Eb7 = Eb, G, Bb, Db

# Bar 2 (1.5 - 3.0s)
piano_notes = [
    # Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=87, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=84, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=90, pitch=81, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=90, pitch=80, start=2.25, end=2.625), # Eb

    # Bb7 on beat 4
    pretty_midi.Note(velocity=90, pitch=83, start=2.625, end=3.0), # Bb
    pretty_midi.Note(velocity=90, pitch=80, start=2.625, end=3.0), # D
    pretty_midi.Note(velocity=90, pitch=87, start=2.625, end=3.0), # F
    pretty_midi.Note(velocity=90, pitch=84, start=2.625, end=3.0), # Ab

    # Bar 3 (3.0 - 4.5s)
    # Cm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125), # Bb

    # Eb7 on beat 4
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5), # G
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5), # Bb
    pretty_midi.Note(velocity=90, pitch=63, start=4.125, end=4.5), # Db

    # Bar 4 (4.5 - 6.0s)
    # Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=87, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=84, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=90, pitch=81, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=90, pitch=80, start=5.25, end=5.625), # Eb

    # Bb7 on beat 4
    pretty_midi.Note(velocity=90, pitch=83, start=5.625, end=6.0), # Bb
    pretty_midi.Note(velocity=90, pitch=80, start=5.625, end=6.0), # D
    pretty_midi.Note(velocity=90, pitch=87, start=5.625, end=6.0), # F
    pretty_midi.Note(velocity=90, pitch=84, start=5.625, end=6.0), # Ab
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, C, Db, D

# Bar 2 (1.5 - 3.0s)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=87, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=110, pitch=84, start=1.75, end=2.0), # Gb
    pretty_midi.Note(velocity=110, pitch=80, start=2.0, end=2.25), # Eb
    pretty_midi.Note(velocity=110, pitch=82, start=2.25, end=2.5), # A
    pretty_midi.Note(velocity=110, pitch=80, start=2.5, end=2.75), # Eb
    pretty_midi.Note(velocity=110, pitch=81, start=2.75, end=3.0), # C
]

# Bar 3 and 4: leave it hanging, come back and finish it
# Rest of the bars are left to the solo, but this is the intro

for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.75),    # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=3.0),
]

# Bar 3 (3.0 - 4.5s)
drums_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.5),
])

# Bar 4 (4.5 - 6.0s)
drums_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4 (but ends at 6.0)
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=6.0),
])

for note in drums_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro_wayne.mid")
