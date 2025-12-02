
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

# Marcus - Walking bass line in F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=49, start=2.625, end=3.0),  # F#
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),  # G#
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875),  # F#
    pretty_midi.Note(velocity=100, pitch=51, start=4.875, end=5.25), # G#
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=48, start=5.625, end=6.0),  # F
]
for note in bass_notes:
    bass.notes.append(note)

# Diane - 7th chords on 2 and 4, F7, Bb7, F7, Bb7
piano_notes = [
    # Bar 2 (1.5-2.25s)
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25), # D
    # Bar 3 (2.25-3.0s)
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=3.0), # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=3.0), # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=3.0), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0), # G
    # Bar 4 (3.0-3.75s)
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75), # D
    # Bar 4 (3.75-4.5s)
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.5), # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=4.5), # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.5), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.5), # G
]
for note in piano_notes:
    piano.notes.append(note)

# Dante - Melody: F, Bb, A, G (bars 2-4)
sax_notes = [
    # Bar 2 (1.5-2.25s)
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # Bb
    # Bar 3 (2.25-3.0s)
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # G
    # Bar 4 (3.0-3.75s)
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # Bb
    # Bar 4 (3.75-4.5s)
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # G
    # Bar 4 (4.5-5.25s)
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # Bb
    # Bar 4 (5.25-6.0s)
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # G
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
