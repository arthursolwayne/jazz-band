
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
bar_length = 1.5
for i in range(4):
    time = i * bar_length / 4.0
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_length / 4.0))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + bar_length / 4.0, end=time + bar_length / 2.0))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.75)),  # F
    (pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=2.0)),  # Gb
    (pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.25)),  # E
    (pretty_midi.Note(velocity=100, pitch=34, start=2.25, end=2.5)),  # D
    (pretty_midi.Note(velocity=100, pitch=35, start=2.5, end=2.75)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=33, start=2.75, end=3.0)),  # D
    (pretty_midi.Note(velocity=100, pitch=32, start=3.0, end=3.25)),  # C
    (pretty_midi.Note(velocity=100, pitch=31, start=3.25, end=3.5)),  # Bb
    (pretty_midi.Note(velocity=100, pitch=30, start=3.5, end=3.75)),  # A
    (pretty_midi.Note(velocity=100, pitch=29, start=3.75, end=4.0)),  # Ab
    (pretty_midi.Note(velocity=100, pitch=27, start=4.0, end=4.25)),  # G
    (pretty_midi.Note(velocity=100, pitch=26, start=4.25, end=4.5)),  # F
    (pretty_midi.Note(velocity=100, pitch=28, start=4.5, end=4.75)),  # Gb
    (pretty_midi.Note(velocity=100, pitch=25, start=4.75, end=5.0)),  # E
    (pretty_midi.Note(velocity=100, pitch=24, start=5.0, end=5.25)),  # D
    (pretty_midi.Note(velocity=100, pitch=22, start=5.25, end=5.5)),  # C
    (pretty_midi.Note(velocity=100, pitch=21, start=5.5, end=5.75)),  # Bb
    (pretty_midi.Note(velocity=100, pitch=20, start=5.75, end=6.0)),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F7
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),   # C
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar
for i in range(4):
    time = 1.5 + i * bar_length / 4.0
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_length / 4.0))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + bar_length / 4.0, end=time + bar_length / 2.0))
    for j in range(4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time + j * bar_length / 8.0, end=time + j * bar_length / 8.0 + bar_length / 8.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
