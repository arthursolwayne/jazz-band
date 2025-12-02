
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.625, end=3.0),   # D#
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),   # E
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.875),   # G#
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.625),  # A#
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),   # B
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 (C E G B) on beat 2
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25),
    # Bar 3: F7 (F A C E) on beat 2
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=76, start=3.375, end=3.75),
    # Bar 4: G7 (G B D F) on beat 2
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=77, start=4.875, end=5.25),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif (C, D#, E)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),
    # Bar 3: Leave it hanging (rest)
    # Bar 4: Come back and finish it (C, D#, E, B)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=63, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dantes_intro.mid")
