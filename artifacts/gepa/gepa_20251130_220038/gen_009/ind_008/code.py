
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=54, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=61, start=5.625, end=6.0),  # F#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # G
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),   # D
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: continue for bars 2-4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 2
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
