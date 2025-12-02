
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
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i*0.375, end=i*0.375 + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches
# Dm7 chord: D F A C
# Walking bass: D F Eb G A C Bb D

bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
# Dm7 = D F A C
# G7 = G B D F
# Cm7 = C Eb G Bb
# F7 = F A C Eb

# Bar 2: Dm7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25))  # C

# Bar 3: G7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75))  # B
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75))  # F

# Bar 4: Cm7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25))  # Eb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25))  # Bb

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Dm7, start motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75))  # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0))   # D

# Bar 3: G7, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25))  # G

# Bar 4: Dm7, return and finish
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5))   # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0))  # D

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))
for i in range(4, 8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=(i * 0.375), end=(i * 0.375) + 0.125))

# Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5))
for i in range(8, 12):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=(i * 0.375), end=(i * 0.375) + 0.125))

# Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0))
for i in range(12, 16):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=(i * 0.375), end=(i * 0.375) + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
