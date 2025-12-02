
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # D7
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # D7
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # D7
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Add the drum fill for bar 4
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.875, end=6.0),    # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=5.875, end=6.0),
]

for note in drum_notes_bar4:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
