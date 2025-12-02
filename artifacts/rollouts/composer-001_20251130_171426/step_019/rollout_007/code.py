
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=i * 0.375, end=i * 0.375 + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm
# Dm = D, F, A, C
# Walking line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D (chromatic approach)

bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625), # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.0), # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125), # A
    pretty_midi.Note(velocity=100, pitch=68, start=2.125, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.375), # B
    pretty_midi.Note(velocity=100, pitch=70, start=2.375, end=2.5), # C
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Dm7 = D, F, A, C
# Comp on 2 and 4

# Bar 2: 2nd beat (0.75s into bar)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.375))

# Bar 2: 4th beat (1.5s into bar)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.125))

# Sax: Motif in Dm
# D, F, G, Bb -> short motif, leave it hanging

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.0),
]

sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Dm
# D -> Eb -> F -> G -> A -> Bb -> B -> C -> D (chromatic approach)

bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125), # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.125, end=3.25), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.5), # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.625), # A
    pretty_midi.Note(velocity=100, pitch=68, start=3.625, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=3.875), # B
    pretty_midi.Note(velocity=100, pitch=70, start=3.875, end=4.0), # C
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Dm7 = D, F, A, C
# Comp on 2 and 4

# Bar 3: 2nd beat (0.75s into bar)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=3.875))

# Bar 3: 4th beat (1.5s into bar)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.625))

# Sax: Motif in Dm
# D, F, G, Bb -> short motif, leave it hanging

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=64, start=3.125, end=3.25),
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.375),
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.5),
]

sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in Dm
# D -> Eb -> F -> G -> A -> Bb -> B -> C -> D (chromatic approach)

bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625), # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.625, end=4.75), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.0), # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.125), # A
    pretty_midi.Note(velocity=100, pitch=68, start=5.125, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.375), # B
    pretty_midi.Note(velocity=100, pitch=70, start=5.375, end=5.5), # C
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Dm7 = D, F, A, C
# Comp on 2 and 4

# Bar 4: 2nd beat (0.75s into bar)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.375))

# Bar 4: 4th beat (1.5s into bar)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=6.0, end=6.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=6.0, end=6.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=6.0, end=6.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=6.0, end=6.125))

# Sax: Motif in Dm
# D, F, G, Bb -> short motif, leave it hanging

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=64, start=4.625, end=4.75),
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875),
    pretty_midi.Note(velocity=110, pitch=68, start=4.875, end=5.0),
]

sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 2: 1.5 - 3.0s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=1.875))
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5 + i * 0.375, end=1.5 + i * 0.375 + 0.125))

# Bar 3: 3.0 - 4.5s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.25, end=3.375))
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0 + i * 0.375, end=3.0 + i * 0.375 + 0.125))

# Bar 4: 4.5 - 6.0s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=4.875))
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5 + i * 0.375, end=4.5 + i * 0.375 + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
