
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1 (0.0 to 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),   # Snare on 4
    # Hi-hats on every eighth note
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking bass in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # F
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),  # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s): Fmaj7
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=3.0),  # E
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # A
    # Bar 3 (3.0 - 4.5s): Gm7
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # F
    # Bar 4 (4.5 - 6.0s): C7
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=6.0),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),   # A
    # Bar 3 (3.0 - 4.5s) - Rest
    # Bar 4 (4.5 - 6.0s) - Repeat the motif
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),   # A
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
