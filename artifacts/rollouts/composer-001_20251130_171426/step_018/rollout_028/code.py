
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=39, start=2.625, end=3.0), # D
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.375), # E
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75), # Gb
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=90, pitch=39, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=90, pitch=39, start=5.625, end=6.0), # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875), # F7
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875),
    # Bar 3 (2.25s)
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625), # F7
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625),
    # Bar 4 (3.0s)
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375), # F7
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.375),
    # Bar 2, 2nd half (1.875s)
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # F7
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=57, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=59, start=1.875, end=2.25),
    # Bar 3, 2nd half (2.625s)
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0), # F7
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=59, start=2.625, end=3.0),
    # Bar 4, 2nd half (3.375s)
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75), # F7
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=59, start=3.375, end=3.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=1.6875), # G
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=63, start=2.4375, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.8125), # A
    pretty_midi.Note(velocity=100, pitch=63, start=3.28125, end=3.46875), # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.46875, end=3.65625), # A
    pretty_midi.Note(velocity=100, pitch=63, start=4.125, end=4.3125), # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.3125, end=4.5), # A
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.0625, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=63, start=5.71875, end=5.90625), # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.90625, end=6.0), # A
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start, end=bar_start + 1.5)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
