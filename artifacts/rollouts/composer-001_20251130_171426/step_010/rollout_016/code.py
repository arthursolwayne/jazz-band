
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
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
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # C
    # Bar 3: Dm7 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
    # Bar 4: Dm7 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F
    # Bar 3: Dm7 (comp on 2)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F
    # Bar 4: Dm7 (comp on 4)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # F
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif — start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),  # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write('wayne_intro.mid')
