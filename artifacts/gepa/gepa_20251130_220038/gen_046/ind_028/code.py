
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
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4 (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
# F7 chord: F, A, C, E
# Chromatic approach to F
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # G#
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# F7 = F, A, C, E
# Bb7 = Bb, D, F, Ab
# Bars 2-4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # E
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # Ab
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F, G, Bb, F (on 1, 3, 7, 9)
# F - G - Bb - F (on 1, 3, 7, 9)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: continue to fill the bar
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
