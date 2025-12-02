
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
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    (21, 1.5), (23, 1.75), (24, 2.0), (21, 2.25),
    (23, 2.5), (24, 2.75), (21, 3.0), (23, 3.25),
    (24, 3.5), (21, 3.75), (23, 4.0), (24, 4.25),
    (21, 4.5), (23, 4.75), (24, 5.0), (21, 5.25)
]
for pitch, start in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25))

# Piano: 7th chords on 2 and 4
# Bar 2: F7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=45, start=2.0, end=2.25))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=47, start=2.0, end=2.25))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.25))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=2.0, end=2.25))  # D

# Bar 3: G7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.25))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.25))  # B
piano.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.25))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.25))  # D

# Bar 4: C7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=4.0, end=4.25))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=4.0, end=4.25))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=4.0, end=4.25))  # E
piano.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=4.0, end=4.25))  # G

# Drums: continue with kick, snare, hihat
for i in range(1, 4):
    bar_start = i * 1.5
    kick_start = bar_start + 0.0
    kick_end = kick_start + 0.375
    snare_start = bar_start + 0.75
    snare_end = snare_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end))
    for j in range(0, 4):
        hit_start = bar_start + j * 0.375
        hit_end = hit_start + 0.125
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hit_start, end=hit_end))

# Sax: short motif, start at bar 2.5 (2.25s)
# F -> G -> A -> F (hanging on A)
sax_notes = [
    (45, 2.25, 2.5),  # F
    (47, 2.5, 2.75),  # G
    (48, 2.75, 3.0),  # A
    (45, 3.0, 3.25)   # F
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

# Second round: repeat the motif at bar 3.5 (3.25s), this time resolving
sax_notes = [
    (45, 3.25, 3.5),  # F
    (47, 3.5, 3.75),  # G
    (48, 3.75, 4.0),  # A
    (45, 4.0, 4.25)   # F
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

# Third round: introduce a variation at bar 4.5 (4.25s)
# F -> G -> Bb -> F
sax_notes = [
    (45, 4.25, 4.5),  # F
    (47, 4.5, 4.75),  # G
    (49, 4.75, 5.0),  # Bb
    (45, 5.0, 5.25)   # F
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dantes_intro.mid")
