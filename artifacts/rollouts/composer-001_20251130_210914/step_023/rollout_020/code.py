
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=90, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # Dm7 root
    pretty_midi.Note(velocity=90, pitch=63, start=1.75, end=2.0),  # Eb chromatic
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.75),  # F chromatic
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=3.25, end=3.5),  # Eb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.0),  # Bb chromatic
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),  # D
    # Bar 4 (continued)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # D
    # Final note
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.75, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Diane - Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.75),  # D7 - D
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.75),  # D7 - F#
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=1.75),  # D7 - A
    pretty_midi.Note(velocity=90, pitch=87, start=1.5, end=1.75),  # D7 - C
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.5),  # D7 - D
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.5),  # D7 - F#
    pretty_midi.Note(velocity=90, pitch=82, start=2.25, end=2.5),  # D7 - A
    pretty_midi.Note(velocity=90, pitch=87, start=2.25, end=2.5),  # D7 - C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.0),  # D7 - D
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=4.0),  # D7 - F#
    pretty_midi.Note(velocity=90, pitch=82, start=3.75, end=4.0),  # D7 - A
    pretty_midi.Note(velocity=90, pitch=87, start=3.75, end=4.0),  # D7 - C
]
piano.notes.extend(piano_notes)

# Dante - Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # E
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # F
    # Bar 4 (continued)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # E
    # Final note
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2
for i in range(0, 6):
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i*0.375, end=1.5 + i*0.375 + 0.375)
for i in range(0, 6):
    pretty_midi.Note(velocity=110, pitch=38, start=1.5 + i*0.375, end=1.5 + i*0.375 + 0.375)
for i in range(0, 12):
    pretty_midi.Note(velocity=90, pitch=42, start=1.5 + i*0.125, end=1.5 + i*0.125 + 0.125)

# Bar 3
for i in range(0, 6):
    pretty_midi.Note(velocity=100, pitch=36, start=3.0 + i*0.375, end=3.0 + i*0.375 + 0.375)
for i in range(0, 6):
    pretty_midi.Note(velocity=110, pitch=38, start=3.0 + i*0.375, end=3.0 + i*0.375 + 0.375)
for i in range(0, 12):
    pretty_midi.Note(velocity=90, pitch=42, start=3.0 + i*0.125, end=3.0 + i*0.125 + 0.125)

# Bar 4
for i in range(0, 6):
    pretty_midi.Note(velocity=100, pitch=36, start=4.5 + i*0.375, end=4.5 + i*0.375 + 0.375)
for i in range(0, 6):
    pretty_midi.Note(velocity=110, pitch=38, start=4.5 + i*0.375, end=4.5 + i*0.375 + 0.375)
for i in range(0, 12):
    pretty_midi.Note(velocity=90, pitch=42, start=4.5 + i*0.125, end=4.5 + i*0.125 + 0.125)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
