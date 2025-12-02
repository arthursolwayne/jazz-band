
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

# Add to drums
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=3.0),  # A
    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),  # D
    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0),  # F#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=55, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=57, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # A
    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # A
    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # A
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0625), # B
    pretty_midi.Note(velocity=100, pitch=67, start=2.0625, end=2.25), # C
    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.1875, end=3.375), # Eb
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5625), # E
    pretty_midi.Note(velocity=100, pitch=74, start=3.5625, end=3.75), # F
    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.6875),  # G
    pretty_midi.Note(velocity=100, pitch=78, start=4.6875, end=4.875), # A
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.0625), # Bb
    pretty_midi.Note(velocity=100, pitch=81, start=5.0625, end=5.25), # B
    pretty_midi.Note(velocity=100, pitch=83, start=5.25, end=5.4375), # C
    pretty_midi.Note(velocity=100, pitch=85, start=5.4375, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=87, start=5.625, end=5.8125), # Eb
    pretty_midi.Note(velocity=100, pitch=88, start=5.8125, end=6.0),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
