
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.5)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.25)
    # Hi-hat
    for i in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=46, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=3.0),   # A
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),   # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=54, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=5.625, end=6.0),   # F#
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # G
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=59, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # G
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Fm7 (F, Ab, Bb, D) -> F, Ab, Bb, D -> F, Ab, Bb, D (octave up)
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.0),   # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.375, end=2.5),   # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=83, start=4.5, end=4.625),  # F (octave up)
    pretty_midi.Note(velocity=100, pitch=79, start=4.625, end=4.75),  # Ab (octave up)
    pretty_midi.Note(velocity=100, pitch=82, start=4.75, end=4.875),  # Bb (octave up)
    pretty_midi.Note(velocity=100, pitch=86, start=4.875, end=5.0),   # D (octave up)
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
