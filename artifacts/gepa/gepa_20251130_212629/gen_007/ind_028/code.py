
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in (1.5 - 3.0s)
# Bass line: Walking in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on beat 1
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # D
    # Bar 2: Cm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Bb
    # Bar 3: F7 on beat 1
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # D
    # Bar 3: Eb7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),   # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7: D, F, Bb, C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # G
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3 and 4: Drums continue with same pattern
for i in range(3):
    offset = 1.5 + 1.5 * i
    for note in drum_notes:
        new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + offset, note.end + offset)
        drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
