
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
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Fm root on beat 1, Fm5 (C) on beat 2, Fm7b5 (Ab) on beat 3, Fm on beat 4

# Bass: F (38), C (43), Ab (50), F (38)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0))

# Piano: Fm7b5 on beat 2, Cm7 on beat 3, Fm7 on beat 4, resolve on beat 4

# Bar 2: Fm7b5 (F, Ab, C, D)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.0))

# Bar 3: Cm7 (C, Eb, G, Bb)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=73, start=2.25, end=2.5))

# Bar 4: Fm7 (F, Ab, C, Eb)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=2.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=2.625, end=2.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=2.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=2.625, end=2.875))

# Sax: Short motif starting on beat 1 of bar 2, ending on beat 3 of bar 4
# Motif: F (53), Ab (61), C (65), D (66)

# First note: F on beat 1
sax.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.6875))

# Second note: Ab on beat 2
sax.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.0625))

# Third note: C on beat 3 of bar 3
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.4375))

# Fourth note: D on beat 4 of bar 4 (sustained)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0))

# Drums: Bar 2-4
# Kick on 1 and 3 of each bar
for bar in range(2, 4):
    start = bar * 1.5
    kick_start = start
    kick_end = kick_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=kick_start, end=kick_end))
    kick_start = start + 1.125
    kick_end = kick_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=kick_start, end=kick_end))

# Snare on 2 and 4 of each bar
for bar in range(2, 4):
    start = bar * 1.5
    snare_start = start + 0.75
    snare_end = snare_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    snare_start = start + 1.875
    snare_end = snare_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))

# Hi-hat on every eighth of each bar
for bar in range(2, 4):
    start = bar * 1.5
    for i in range(0, 4):
        hihat_start = start + i * 0.375
        hihat_end = hihat_start + 0.375
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
