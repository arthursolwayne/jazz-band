
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line in F minor, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=2.5, end=2.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=2.75, end=3.0),  # F

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=52, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=80, pitch=49, start=4.0, end=4.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=50, start=4.25, end=4.5),  # G

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=52, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=54, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=80, pitch=51, start=5.5, end=5.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=52, start=5.75, end=6.0),  # A
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=68, start=1.75, end=2.0),  # F7 (C)
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=2.0),  # F7 (E)
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # F7 (D)
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # F7 (Bb)

    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.5),  # F7 (C)
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.5),  # F7 (E)
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # F7 (D)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # F7 (Bb)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=68, start=3.25, end=3.5),  # F7 (C)
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),  # F7 (E)
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),  # F7 (D)
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # F7 (Bb)

    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.0),  # F7 (C)
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.0),  # F7 (E)
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # F7 (D)
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # F7 (Bb)

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=68, start=4.75, end=5.0),  # F7 (C)
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=5.0),  # F7 (E)
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),  # F7 (D)
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # F7 (Bb)

    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.5),  # F7 (C)
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.5),  # F7 (E)
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),  # F7 (D)
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # F7 (Bb)

    pretty_midi.Note(velocity=90, pitch=68, start=5.75, end=6.0),  # F7 (C)
    pretty_midi.Note(velocity=90, pitch=72, start=5.75, end=6.0),  # F7 (E)
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),  # F7 (D)
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),  # F7 (Bb)
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: one short motif, start, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),  # Eb

    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),  # Eb

    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # F#
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=66, start=5.75, end=6.0),  # Eb
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("cellar_intro.mid")
