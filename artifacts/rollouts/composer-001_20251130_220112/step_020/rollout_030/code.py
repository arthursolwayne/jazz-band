
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
# Sax melody: Dm7 -> G7 -> Cm7 -> F7
# Dm7: D F A C
# G7: G B D F
# Cm7: C Eb G Bb
# F7: F A C Eb

# Sax melody (1.5 - 3.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0), # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5), # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75), # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0), # B
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: walking line in Dm
# D - Eb - F - G - A - Bb - C - D
# Bar 2: D - Eb - F - G
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=2.0), # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.25), # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5), # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano chords: Dm7 on 2, G7 on 3, Cm7 on 4
# Comp on 2 and 4
piano_notes = [
    # Dm7 on beat 2 (1.75 - 2.0)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0), # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0), # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0), # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0), # C
    # G7 on beat 4 (2.25 - 2.5)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5), # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5), # B
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5), # D
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.5), # F
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody: Cm7 -> F7
# Cm7: C Eb G Bb
# F7: F A C Eb

# Sax melody (3.0 - 4.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25), # C
    pretty_midi.Note(velocity=100, pitch=63, start=3.25, end=3.5), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25), # F
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5), # A
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: walking line in Dm
# Bar 3: A - Bb - C - D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25), # A
    pretty_midi.Note(velocity=80, pitch=66, start=3.25, end=3.5), # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=3.5, end=3.75), # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0), # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano chords: Cm7 on 2, F7 on 4
# Comp on 2 and 4
piano_notes = [
    # Cm7 on beat 2 (3.25 - 3.5)
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5), # C
    pretty_midi.Note(velocity=90, pitch=63, start=3.25, end=3.5), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5), # G
    pretty_midi.Note(velocity=90, pitch=66, start=3.25, end=3.5), # Bb
    # F7 on beat 4 (3.75 - 4.0)
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0), # F
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0), # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0), # C
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.0), # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody: Dm7 -> G7 -> Cm7 -> F7
# Dm7: D F A C
# G7: G B D F
# Cm7: C Eb G Bb
# F7: F A C Eb

# Sax melody (4.5 - 6.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75), # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0), # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5), # C
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75), # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0), # B
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: walking line in Dm
# Bar 4: D - Eb - F - G
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75), # D
    pretty_midi.Note(velocity=80, pitch=63, start=4.75, end=5.0), # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=5.0, end=5.25), # F
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5), # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano chords: Dm7 on 2, G7 on 3, Cm7 on 4
# Comp on 2 and 4
piano_notes = [
    # Dm7 on beat 2 (4.75 - 5.0)
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0), # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0), # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0), # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0), # C
    # G7 on beat 4 (5.25 - 5.5)
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5), # G
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5), # B
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5), # D
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.5), # F
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Drums (4.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
