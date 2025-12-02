
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line with chromatic approaches
bass_notes = [
    # Bar 2: F -> Gb -> G -> Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=73, start=2.625, end=3.0),  # Ab

    # Bar 3: Bb -> B -> C -> C#
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=80, start=4.125, end=4.5),  # C#

    # Bar 4: D -> Eb -> E -> F
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=81, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=83, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=84, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=77, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=84, start=2.0, end=2.25),  # F

    # Bar 3: G7 on 2
    pretty_midi.Note(velocity=100, pitch=77, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=82, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=83, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=87, start=3.5, end=3.75),  # D

    # Bar 4: C7 on 2
    pretty_midi.Note(velocity=100, pitch=79, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=84, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=82, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=89, start=5.0, end=5.25),  # B
]
piano.notes.extend(piano_notes)

# Sax: Dante - Melody: F -> Bb -> C -> E (with a slight delay on E)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=77, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=79, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=110, pitch=83, start=3.0, end=3.25),  # E
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
