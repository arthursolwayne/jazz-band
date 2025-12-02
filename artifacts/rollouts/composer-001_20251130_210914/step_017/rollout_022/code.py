
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS (Marcus): Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625), # D#
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G#
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=63, start=5.25, end=5.625), # D#
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # F#
]

for note in bass_notes:
    bass.notes.append(note)

# PIANO (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),   # G
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=2.25),   # B
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),   # D
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),   # C
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.75),   # A
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.75),   # B
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.25),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),   # G
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=5.25),   # B
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.25),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# SAX (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # B
    # Bar 3 (3.0 - 4.5s) - leave it hanging
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # B
    # Bar 4 (4.5 - 6.0s) - come back and finish it
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # G#
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # F#
]

for note in sax_notes:
    sax.notes.append(note)

# Drums in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 (start)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2 (start + 0.75)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Kick on 3 (start + 1.125)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 4 (start + 1.875)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25))
    # Hihat on every eighth
    for i in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
