
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    time = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time + 1.125, end=time + 1.125 + 0.375)
    drums.notes.append(kick)
    # Snare on 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 1.5, end=time + 1.5 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, chromatic approaches, no repeated notes
# C7 chord: C E G B
# Start with C -> Eb -> D -> C
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),   # C
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),  # Db
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),   # E
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
# C7: C E G Bb
# Start on 2nd beat of bar 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # Bb
]
piano.notes.extend(piano_notes)

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    time = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time + 1.125, end=time + 1.125 + 0.375)
    drums.notes.append(kick)
    # Snare on 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 1.5, end=time + 1.5 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# C E C E Bb D
# Start on beat 2 of bar 2, leave it hanging, return on beat 2 of bar 3

# First pass: C E C E
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # E
]

# Second pass: Bb D
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),   # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.25),  # D
])

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
