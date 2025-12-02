
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
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=80, pitch=77, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=79, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=81, start=5.625, end=6.0),   # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=82, start=2.25, end=2.625),  # F
    # Bar 3: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=82, start=3.75, end=4.125),  # F
    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=82, start=5.25, end=5.625),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (74) -> Eb (76) -> F (77) -> D (74) on bar 2, then continue with the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=76, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=77, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.0),   # D
    pretty_midi.Note(velocity=110, pitch=76, start=2.0, end=2.125),   # Eb
    pretty_midi.Note(velocity=110, pitch=77, start=2.125, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=79, start=2.25, end=2.5),    # G
    pretty_midi.Note(velocity=110, pitch=74, start=2.5, end=2.75),    # D
    pretty_midi.Note(velocity=110, pitch=81, start=2.75, end=3.0),    # B
    pretty_midi.Note(velocity=110, pitch=79, start=3.0, end=3.25),    # G
    pretty_midi.Note(velocity=110, pitch=74, start=3.25, end=3.5),    # D
    pretty_midi.Note(velocity=110, pitch=76, start=3.5, end=3.75),    # Eb
    pretty_midi.Note(velocity=110, pitch=77, start=3.75, end=4.0),    # F
    pretty_midi.Note(velocity=110, pitch=74, start=4.0, end=4.25),    # D
    pretty_midi.Note(velocity=110, pitch=76, start=4.25, end=4.5),    # Eb
    pretty_midi.Note(velocity=110, pitch=77, start=4.5, end=4.75),    # F
    pretty_midi.Note(velocity=110, pitch=79, start=4.75, end=5.0),    # G
    pretty_midi.Note(velocity=110, pitch=74, start=5.0, end=5.25),    # D
    pretty_midi.Note(velocity=110, pitch=81, start=5.25, end=5.5),    # B
    pretty_midi.Note(velocity=110, pitch=79, start=5.5, end=5.75),    # G
    pretty_midi.Note(velocity=110, pitch=74, start=5.75, end=6.0),    # D
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4, kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 1.5)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
