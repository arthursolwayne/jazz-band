
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

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
# Dm7 chord: D F A C
# Walking bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=90, pitch=68, start=2.125, end=2.25), # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375), # B
    pretty_midi.Note(velocity=90, pitch=70, start=2.375, end=2.5),  # C
]

bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Bar 2: comp on 2 and 4

# 2nd beat (0.75s into bar)
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.375))  # D
piano.notes.append(pretty_midi.Note(velocity=95, pitch=65, start=2.25, end=2.375))  # F
piano.notes.append(pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.375))  # A
piano.notes.append(pretty_midi.Note(velocity=95, pitch=70, start=2.25, end=2.375))  # C

# 4th beat (1.5s into bar)
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=2.625, end=2.75))  # D
piano.notes.append(pretty_midi.Note(velocity=95, pitch=65, start=2.625, end=2.75))  # F
piano.notes.append(pretty_midi.Note(velocity=95, pitch=69, start=2.625, end=2.75))  # A
piano.notes.append(pretty_midi.Note(velocity=95, pitch=70, start=2.625, end=2.75))  # C

# Dante: Melody - a whisper at first, then a cry
# Start with a short motif: D -> Bb -> C -> D

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.575), # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.575, end=1.65), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.65, end=1.725), # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.725, end=1.8),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.8, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=1.95), # C
    pretty_midi.Note(velocity=100, pitch=65, start=1.95, end=2.025), # D#
    pretty_midi.Note(velocity=100, pitch=62, start=2.025, end=2.1),  # D
]

sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking line, chromatic approaches, no repeated notes
# Dm7 chord: D F A C
# Walking bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.125, end=3.25), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.375), # F
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.625),  # A
    pretty_midi.Note(velocity=90, pitch=68, start=3.625, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.875), # B
    pretty_midi.Note(velocity=90, pitch=70, start=3.875, end=4.0),  # C
]

bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Bar 3: comp on 2 and 4

# 2nd beat (0.75s into bar)
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=3.75, end=3.875))  # D
piano.notes.append(pretty_midi.Note(velocity=95, pitch=65, start=3.75, end=3.875))  # F
piano.notes.append(pretty_midi.Note(velocity=95, pitch=69, start=3.75, end=3.875))  # A
piano.notes.append(pretty_midi.Note(velocity=95, pitch=70, start=3.75, end=3.875))  # C

# 4th beat (1.5s into bar)
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=4.125, end=4.25))  # D
piano.notes.append(pretty_midi.Note(velocity=95, pitch=65, start=4.125, end=4.25))  # F
piano.notes.append(pretty_midi.Note(velocity=95, pitch=69, start=4.125, end=4.25))  # A
piano.notes.append(pretty_midi.Note(velocity=95, pitch=70, start=4.125, end=4.25))  # C

# Dante: Melody - continue the motif, build intensity
# D -> Bb -> C -> D -> E -> C -> D# -> D

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.075), # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.075, end=3.15), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.15, end=3.225), # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.225, end=3.3),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.3, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.45), # C
    pretty_midi.Note(velocity=100, pitch=65, start=3.45, end=3.525), # D#
    pretty_midi.Note(velocity=100, pitch=62, start=3.525, end=3.6),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.6, end=3.675),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.675, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.825), # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.825, end=3.9),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.9, end=3.975),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=3.975, end=4.05), # G
    pretty_midi.Note(velocity=100, pitch=70, start=4.05, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.2),  # D
]

sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
# Dm7 chord: D F A C
# Walking bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.625, end=4.75), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=4.875), # F
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.125),  # A
    pretty_midi.Note(velocity=90, pitch=68, start=5.125, end=5.25), # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.375), # B
    pretty_midi.Note(velocity=90, pitch=70, start=5.375, end=5.5),  # C
]

bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Bar 4: comp on 2 and 4

# 2nd beat (0.75s into bar)
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=5.25, end=5.375))  # D
piano.notes.append(pretty_midi.Note(velocity=95, pitch=65, start=5.25, end=5.375))  # F
piano.notes.append(pretty_midi.Note(velocity=95, pitch=69, start=5.25, end=5.375))  # A
piano.notes.append(pretty_midi.Note(velocity=95, pitch=70, start=5.25, end=5.375))  # C

# 4th beat (1.5s into bar)
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=5.625, end=5.75))  # D
piano.notes.append(pretty_midi.Note(velocity=95, pitch=65, start=5.625, end=5.75))  # F
piano.notes.append(pretty_midi.Note(velocity=95, pitch=69, start=5.625, end=5.75))  # A
piano.notes.append(pretty_midi.Note(velocity=95, pitch=70, start=5.625, end=5.75))  # C

# Dante: Melody - finish with a cry, resolve on D
# D -> Bb -> C -> D -> E -> C -> D# -> D -> E -> G -> C -> B -> G -> C -> D

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.575), # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.575, end=4.65), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.65, end=4.725), # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.725, end=4.8),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.8, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=4.95), # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.95, end=5.025), # D#
    pretty_midi.Note(velocity=100, pitch=62, start=5.025, end=5.1),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.1, end=5.175),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=5.175, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.325), # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.325, end=5.4),  # B
    pretty_midi.Note(velocity=100, pitch=66, start=5.4, end=5.475),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.475, end=5.55), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.55, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.7),   # D
]

sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125))

# Hi-hat on every eighth
for i in range(0, 4):
    start = 4.5 + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
