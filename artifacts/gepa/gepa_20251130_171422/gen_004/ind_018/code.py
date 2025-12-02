
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
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=54, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=55, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=100, pitch=58, start=2.5, end=2.75),  # A#
    pretty_midi.Note(velocity=100, pitch=59, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=3.25, end=3.5),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.25, end=4.5),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=5.0, end=5.25),  # A#
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=5.75, end=6.0),  # C#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Bars 2-4: F7, Bb7, E7, A7
chords = [
    # Bar 2: F7
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    # Bar 3: Bb7
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=54, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # Ab
    # Bar 4: E7
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.75),  # D
    # Bar 4: A7
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # G
]

for note in chords:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bars 2-4: 1.5 - 6.0s

for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    kick_times = [bar_start + 0.0, bar_start + 1.125]
    snare_times = [bar_start + 0.75, bar_start + 2.25]
    hihat_times = [bar_start + i * 0.375 for i in range(0, 4)]  # every eighth note

    for time in kick_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))
    for time in snare_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.375))
    for time in hihat_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.1875))

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F -> G -> Bb -> F (motif)
# Use quarter notes, with space in between

# Bar 2: F (start)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75))

# Bar 3: G (second note of motif)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=55, start=3.0, end=3.25))

# Bar 4: Bb (third note of motif)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=57, start=4.5, end=4.75))

# Bar 4: F (final note of motif)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=53, start=5.25, end=5.5))

# Add space between motif notes to make it sing

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
