
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

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2: Everyone enters. Sax plays motif, bass walks, piano comps, drums continue

# Sax motif: Dm7 -> F -> C -> Eb -> D (over 4 beats)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))  # D (Dm7)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0))  # Eb

# Bass: Walking line with chromatic approaches
# Dm7: D - C# - C - B - A - G - F - E - D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=61, start=1.625, end=1.75))  # C#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=1.875))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=59, start=1.875, end=2.0))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=57, start=2.0, end=2.125))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=55, start=2.125, end=2.25))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.375))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=52, start=2.375, end=2.5))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.625))  # D

# Piano: 7th chords on 2 and 4
# Dm7: D, F, A, C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.0))  # C

# Bar 3: Continue the rhythm, sax repeats motif with slight variation
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5))  # Eb

# Bass: Continue walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.125))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=61, start=3.125, end=3.25))  # C#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.375))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=59, start=3.375, end=3.5))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=57, start=3.5, end=3.625))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=55, start=3.625, end=3.75))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=3.875))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=52, start=3.875, end=4.0))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.125))  # D

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.5))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.5))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.5))  # C

# Bar 4: Sax finishes motif, everyone resolves
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0))  # Eb

# Bass: Resolve to D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.625))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=61, start=4.625, end=4.75))  # C#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=4.875))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=59, start=4.875, end=5.0))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=57, start=5.0, end=5.125))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=55, start=5.125, end=5.25))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.375))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=52, start=5.375, end=5.5))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.625))  # D

# Piano: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.0))  # C

# Drums continue with same pattern
for i in range(4, 8):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Add kick and snare for bars 2-4
for i in range(4, 8):
    if i % 2 == 0:
        start = i * 0.375
        end = start + 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=end))
    if i % 2 == 1:
        start = i * 0.375
        end = start + 0.375
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
