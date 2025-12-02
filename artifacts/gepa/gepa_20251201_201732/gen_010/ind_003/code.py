
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

# Bar 2: Everyone in (1.5 - 3.0s)
# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875), # D (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # Bb (chromatic)
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625), # G (fifth)
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),  # F (chromatic)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: open voicings, resolve on the last bar
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # E

    pretty_midi.Note(velocity=100, pitch=59, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # D
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25), # C

    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # F#
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # C

    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0), # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0), # G
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0), # C
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0), # F#
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=2.75, end=3.0),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Everyone in (3.0 - 4.5s)
# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375), # F (root)
    pretty_midi.Note(velocity=100, pitch=58, start=3.375, end=3.75), # D (chromatic)
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125), # C (fifth)
    pretty_midi.Note(velocity=100, pitch=63, start=4.125, end=4.5),  # Bb (chromatic)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: open voicings, resolve on the last bar
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # E
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # Bb

    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # G

    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # G

    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),  # G
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Sax: motif continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Everyone in (4.5 - 6.0s)
# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D (root)
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # F (chromatic)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # G (chromatic)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: open voicings, resolve on the last bar
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # E

    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # E

    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # E

    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Sax: motif finish
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # C
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
