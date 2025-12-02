
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass line (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # D#
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),   # E
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=81, start=5.625, end=6.0),   # B
]
for note in bass_notes:
    bass.notes.append(note)

# Diane - Piano (7th chords, comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.25),   # D
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=2.25),   # F#
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.25),   # A
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=2.25),   # C
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=82, start=2.25, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=84, start=2.25, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=87, start=2.25, end=3.0),   # F#
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.75),   # D
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.75),   # F#
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.75),   # A
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.75),   # C
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.5),   # A
    pretty_midi.Note(velocity=100, pitch=82, start=3.75, end=4.5),   # C
    pretty_midi.Note(velocity=100, pitch=84, start=3.75, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=87, start=3.75, end=4.5),   # F#
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.25),   # D
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=5.25),   # F#
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=5.25),   # A
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=5.25),   # C
]
for note in piano_notes:
    piano.notes.append(note)

# Dante - Tenor sax (motif, starts bar 2, leaves it hanging, returns in bar 4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),   # A
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2 and 3 (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in [2, 3]:
    start = (bar - 1) * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 1.5)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 2.25)

# Bar 4: End with a snare and hihat
start = 4.5
pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 1.5)
pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 2.25)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
