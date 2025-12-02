
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
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=i*0.375, end=i*0.375 + 0.1875))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches
# F7 chord: F A C E (F7 is F A C E♭)
# Bass line (F - E - D - C - B - A - G - F)

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=80, pitch=68, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=80, pitch=69, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=80, pitch=66, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=71, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=5.75, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
# F7 = F A C E♭
# B♭7 = B♭ D F A
# E♭7 = E♭ G B♭ D
# A7 = A C E G

# Bar 2 - F7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=2.0))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=2.0))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=73, start=1.75, end=2.0))  # E♭

# Bar 3 - B♭7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0))  # B♭
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=2.75, end=3.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.75, end=3.0))  # A

# Bar 4 - E♭7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0))  # E♭
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.0))  # B♭
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0))  # D

# Bar 4 - A7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=4.75, end=5.0))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=80, start=4.75, end=5.0))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=82, start=4.75, end=5.0))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=84, start=4.75, end=5.0))  # G

# Dante on sax: short motif, make it sing
# F - A - C - B♭
# Start it, leave it hanging, come back and finish it

# First phrase: F - A - C - B♭
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=1.75, end=2.0))  # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=76, start=2.0, end=2.25))  # C
sax.notes.append(pretty_midi.Note(velocity=110, pitch=73, start=2.25, end=2.5))  # B♭

# Second phrase: repeat the motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=3.5, end=3.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=3.75, end=4.0))  # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=76, start=4.0, end=4.25))  # C
sax.notes.append(pretty_midi.Note(velocity=110, pitch=73, start=4.25, end=4.5))  # B♭

# Third phrase: repeat the motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=5.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=5.75, end=6.0))  # A

# Drums for bars 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.625, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.5, end=5.875))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.0, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125))

# Hihat on every eighth
for i in range(6):
    start = 1.5 + i * 0.375
    end = start + 0.1875
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

for i in range(6):
    start = 3.5 + i * 0.375
    end = start + 0.1875
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

for i in range(4):
    start = 5.5 + i * 0.375
    end = start + 0.1875
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
