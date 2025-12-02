
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
# Sax: Short motif, start on Fm7 chord
# Fm7: F, Ab, C, Eb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.75),  # F (Ab in 3rd inversion)
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # G (Fm7 tension)
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),  # Eb (leave it hanging)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm, chromatic approach to F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=2.0, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.5),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=58, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),  # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif, but with a twist
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),  # Eb
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm, chromatic approach to F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=3.5, end=3.75),  # F#
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.0),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=58, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Resolve motif, end on a strong note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.5),  # F (resolve)
    pretty_midi.Note(velocity=100, pitch=70, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=5.75, end=6.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm, chromatic approach to F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=5.0, end=5.25),  # F#
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=5.75, end=6.0),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=58, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),  # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Hihat on every 8th
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))

midi.instruments.extend([sax, bass, piano, drums])

midi.save('intro_wayne.mid')
