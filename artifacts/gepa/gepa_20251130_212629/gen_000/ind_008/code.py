
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth
for i in range(0, 4):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i*0.375, end=i*0.375 + 0.1875))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D
# D F# A C D F# A C
bass_notes = [2, 4, 7, 10, 2, 4, 7, 10]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note + 24, start=start, end=end))

# Diane: 7th chords on 2 and 4
# Bar 2: D7 (D F# A C)
# Bar 3: G7 (G B D F)
# Bar 4: C7 (C E G B)
for bar in range(2, 5):
    if bar == 2:
        chords = [(2, 4, 7, 10)]
    elif bar == 3:
        chords = [(7, 10, 2, 5)]
    else:
        chords = [(0, 4, 7, 11)]
    for i, chord in enumerate(chords):
        start = 1.5 + (bar - 2) * 1.5 + 0.75
        for note in chord:
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=note + 24, start=start, end=start + 0.1875))

# Dante: Melody
# Motif: D (2) -> F# (4) -> A (7) -> D (2) (half note)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=2 + 24, start=1.5, end=2.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=4 + 24, start=2.25, end=3.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=7 + 24, start=3.0, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=2 + 24, start=3.75, end=4.5))

# Repeat motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=2 + 24, start=4.5, end=5.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=4 + 24, start=5.25, end=6.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=7 + 24, start=6.0, end=6.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=2 + 24, start=6.75, end=7.5))

# Little Ray: same pattern as bar 1
for i in range(4, 8):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=i*0.375, end=i*0.375 + 0.1875))
for i in range(4, 8):
    if i % 2 == 1:
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=i*0.375, end=i*0.375 + 0.125))
for i in range(4, 8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i*0.375, end=i*0.375 + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
