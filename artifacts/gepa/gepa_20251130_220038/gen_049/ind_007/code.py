
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2–4: Full quartet (1.5 - 6.0s)
# bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # D7: G
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # D7: B
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # D7: A
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D7: D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # D7: G
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # D7: B
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # D7: A
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D7: D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # D7: G
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # D7: B
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # D7: A
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D7: D
]

for note in piano_notes:
    piano.notes.append(note)

# sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Uses D, E, F#, G, A
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
