
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=90, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4, comp on beat 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # F
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # F
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone - one short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # Dm (melody start)
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),   # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),   # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),   # D (return)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),   # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),   # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),   # C
    pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=4.0, end=4.25),   # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=4.25, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.75),   # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=4.75, end=5.0),   # G
    pretty_midi.Note(velocity=100, pitch=53, start=5.0, end=5.25),   # F
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.5),   # G
    pretty_midi.Note(velocity=100, pitch=53, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=100, pitch=51, start=5.75, end=6.0),   # Eb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: fill the bar with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1 and 3 (beat 0 and 2)
    pretty_midi.Note(velocity=90, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=90, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4 (beat 1 and 3)
    pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.375, end=bar_start + (i + 1) * 0.375)

drums.notes.extend([note for note in drum_notes if note not in drums.notes])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
