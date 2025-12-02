
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),  # G#
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=54, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.75),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D7 - F#
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # D7 - A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # D7 - C
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.25),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.25),  # F7 - C
    # Bar 4 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # A7 - A
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # A7 - C
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # A7 - E
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # A7 - G
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 - Start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=1.6875, end=1.875),  # D
    # Bar 3 - Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # A
    # Bar 4 - Come back and finish it
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.6875, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0625),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=5.0625, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.4375),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=5.4375, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.8125),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.8125, end=6.0),  # G
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.1875, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.5625, end=bar_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.9375, end=bar_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.3125, end=bar_start + 1.5)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write out the MIDI file
midi.write("dante_intro.mid")
