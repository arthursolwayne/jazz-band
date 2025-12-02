
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.75, end=2.0), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5), # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.75), # E
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0), # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25), # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5), # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.5, end=3.75), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0), # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.25), # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5), # E
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75), # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0), # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.5), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.75), # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0), # D
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.0), # D7 - D
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=2.0), # D7 - G
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=2.0), # D7 - B
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=2.0), # D7 - D

    # Bar 3 (2.0 - 2.5s) - rest
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.5), # D7 - D
    pretty_midi.Note(velocity=90, pitch=74, start=2.0, end=2.5), # D7 - G
    pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.5), # D7 - B
    pretty_midi.Note(velocity=90, pitch=79, start=2.0, end=2.5), # D7 - D

    # Bar 4 (2.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=3.0), # D7 - D
    pretty_midi.Note(velocity=90, pitch=74, start=2.5, end=3.0), # D7 - G
    pretty_midi.Note(velocity=90, pitch=76, start=2.5, end=3.0), # D7 - B
    pretty_midi.Note(velocity=90, pitch=79, start=2.5, end=3.0), # D7 - D

    # Bar 5 (3.0 - 3.5s) - rest
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.5), # D7 - D
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.5), # D7 - G
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.5), # D7 - B
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.5), # D7 - D

    # Bar 6 (3.5 - 4.0s)
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=4.0), # D7 - D
    pretty_midi.Note(velocity=90, pitch=74, start=3.5, end=4.0), # D7 - G
    pretty_midi.Note(velocity=90, pitch=76, start=3.5, end=4.0), # D7 - B
    pretty_midi.Note(velocity=90, pitch=79, start=3.5, end=4.0), # D7 - D

    # Bar 7 (4.0 - 4.5s) - rest
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.5), # D7 - D
    pretty_midi.Note(velocity=90, pitch=74, start=4.0, end=4.5), # D7 - G
    pretty_midi.Note(velocity=90, pitch=76, start=4.0, end=4.5), # D7 - B
    pretty_midi.Note(velocity=90, pitch=79, start=4.0, end=4.5), # D7 - D

    # Bar 8 (4.5 - 5.0s)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.0), # D7 - D
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=5.0), # D7 - G
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=5.0), # D7 - B
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=5.0), # D7 - D

    # Bar 9 (5.0 - 5.5s) - rest
    pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.5), # D7 - D
    pretty_midi.Note(velocity=90, pitch=74, start=5.0, end=5.5), # D7 - G
    pretty_midi.Note(velocity=90, pitch=76, start=5.0, end=5.5), # D7 - B
    pretty_midi.Note(velocity=90, pitch=79, start=5.0, end=5.5), # D7 - D

    # Bar 10 (5.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=6.0), # D7 - D
    pretty_midi.Note(velocity=90, pitch=74, start=5.5, end=6.0), # D7 - G
    pretty_midi.Note(velocity=90, pitch=76, start=5.5, end=6.0), # D7 - B
    pretty_midi.Note(velocity=90, pitch=79, start=5.5, end=6.0), # D7 - D
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0), # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5), # D

    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75), # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0), # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25), # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5), # D

    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0), # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25), # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5), # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75), # D

    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5), # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75), # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0), # D
]

for note in sax_notes:
    sax.notes.append(note)

# Drum fill in bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=5.0, end=5.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.75, end=6.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=5.375, end=5.75),
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=6.125),
    pretty_midi.Note(velocity=90, pitch=42, start=6.125, end=6.5),
    pretty_midi.Note(velocity=100, pitch=36, start=5.75, end=6.125),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
