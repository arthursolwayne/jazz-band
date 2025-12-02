
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
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4 (1.5 - 6.0s)
# Sax: motif starting on D, then F#, then B, then D (D F# B D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # F#
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=43, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=70, pitch=44, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=70, pitch=45, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=70, pitch=47, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=70, pitch=48, start=2.5, end=2.75),  # G#
    pretty_midi.Note(velocity=70, pitch=49, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=70, pitch=50, start=3.0, end=3.25),  # A#
    pretty_midi.Note(velocity=70, pitch=52, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=70, pitch=53, start=3.5, end=3.75),  # C#
    pretty_midi.Note(velocity=70, pitch=55, start=3.75, end=4.0),  # D#
    pretty_midi.Note(velocity=70, pitch=56, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=70, pitch=57, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=70, pitch=59, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=70, pitch=60, start=4.75, end=5.0),  # G#
    pretty_midi.Note(velocity=70, pitch=62, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=70, pitch=63, start=5.25, end=5.5),  # A#
    pretty_midi.Note(velocity=70, pitch=64, start=5.5, end=5.75),  # B
    pretty_midi.Note(velocity=70, pitch=66, start=5.75, end=6.0),  # C#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # F#7 (F# A# C# E)
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # F#7 again
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # F#7 again
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
