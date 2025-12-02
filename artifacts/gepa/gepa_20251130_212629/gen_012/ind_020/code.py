
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4 (1.5 - 6.0s)

# Marcus: Walking bass line in F minor, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),   # Ab
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),   # C#
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0),   # F
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4, F7, Bb7, E7, A7
# Comp on 2 and 4, F minor
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=57, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),  # G
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax, short motif, haunting and melodic
# Start with F (57), Bb (60), Ab (58), F (57)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),   # F
    # Leave it hanging for a beat
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=59, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # E
]
for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("dante_intro.mid")
