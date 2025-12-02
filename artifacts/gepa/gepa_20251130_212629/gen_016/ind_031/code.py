
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes: kick=36, snare=38, hihat=42
# Time in seconds
# Bar 1 (0.0 - 1.5s): Drums only
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),     # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),  # Hihat on 1&
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),    # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),  # Hihat on 2&
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),     # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),    # Hihat on 3&
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),     # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),  # Hihat on 4&
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2 (1.5 - 3.0s): Full band enters
# Bass: walking line (chromatic approach to D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.6875),     # C# (chromatic approach to D)
    pretty_midi.Note(velocity=80, pitch=64, start=1.6875, end=1.875),   # D
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.0625),   # D#
    pretty_midi.Note(velocity=80, pitch=67, start=2.0625, end=2.25),    # E
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.4375),    # F#
    pretty_midi.Note(velocity=80, pitch=71, start=2.4375, end=2.625),   # G#
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=2.8125),   # G
    pretty_midi.Note(velocity=80, pitch=74, start=2.8125, end=3.0),     # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.6875, end=2.0),     # D7 chord (D, F#, A, C)
    pretty_midi.Note(velocity=95, pitch=67, start=1.6875, end=2.0),
    pretty_midi.Note(velocity=95, pitch=72, start=1.6875, end=2.0),
    pretty_midi.Note(velocity=95, pitch=74, start=1.6875, end=2.0),
    pretty_midi.Note(velocity=95, pitch=62, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=95, pitch=67, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=95, pitch=72, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=95, pitch=74, start=2.8125, end=3.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif starts on bar 2 (1.5s), leaves it hanging
# Motif: D (62) - F# (67) - Bb (66) - rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=100, pitch=67, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=67, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=100, pitch=67, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=5.8125),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3 (3.0 - 4.5s): Continue with variations
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.1875),     # G
    pretty_midi.Note(velocity=80, pitch=74, start=3.1875, end=3.375),   # A
    pretty_midi.Note(velocity=80, pitch=76, start=3.375, end=3.5625),   # Bb
    pretty_midi.Note(velocity=80, pitch=77, start=3.5625, end=3.75),    # B
    pretty_midi.Note(velocity=80, pitch=79, start=3.75, end=3.9375),    # C#
    pretty_midi.Note(velocity=80, pitch=81, start=3.9375, end=4.125),   # D#
    pretty_midi.Note(velocity=80, pitch=82, start=4.125, end=4.3125),   # D
    pretty_midi.Note(velocity=80, pitch=84, start=4.3125, end=4.5),     # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=72, start=3.1875, end=3.5),     # G7 chord (G, B, D, F)
    pretty_midi.Note(velocity=95, pitch=77, start=3.1875, end=3.5),
    pretty_midi.Note(velocity=95, pitch=82, start=3.1875, end=3.5),
    pretty_midi.Note(velocity=95, pitch=84, start=3.1875, end=3.5),
    pretty_midi.Note(velocity=95, pitch=72, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=95, pitch=77, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=95, pitch=82, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=95, pitch=84, start=4.3125, end=4.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue motif with variations
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=67, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=100, pitch=67, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=5.8125),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4 (4.5 - 6.0s): Continue and end with a question
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=84, start=4.5, end=4.6875),     # E
    pretty_midi.Note(velocity=80, pitch=86, start=4.6875, end=4.875),   # F#
    pretty_midi.Note(velocity=80, pitch=88, start=4.875, end=5.0625),   # G
    pretty_midi.Note(velocity=80, pitch=89, start=5.0625, end=5.25),    # G#
    pretty_midi.Note(velocity=80, pitch=91, start=5.25, end=5.4375),    # A#
    pretty_midi.Note(velocity=80, pitch=93, start=5.4375, end=5.625),   # B
    pretty_midi.Note(velocity=80, pitch=94, start=5.625, end=5.8125),   # B
    pretty_midi.Note(velocity=80, pitch=96, start=5.8125, end=6.0),     # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=84, start=4.6875, end=5.0),     # E7 chord (E, G#, B, D)
    pretty_midi.Note(velocity=95, pitch=89, start=4.6875, end=5.0),
    pretty_midi.Note(velocity=95, pitch=94, start=4.6875, end=5.0),
    pretty_midi.Note(velocity=95, pitch=96, start=4.6875, end=5.0),
    pretty_midi.Note(velocity=95, pitch=84, start=5.8125, end=6.0),
    pretty_midi.Note(velocity=95, pitch=89, start=5.8125, end=6.0),
    pretty_midi.Note(velocity=95, pitch=94, start=5.8125, end=6.0),
    pretty_midi.Note(velocity=95, pitch=96, start=5.8125, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: End with a question
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=100, pitch=67, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=100, pitch=62, start=6.0, end=6.1875),
    pretty_midi.Note(velocity=100, pitch=67, start=6.1875, end=6.375),
    pretty_midi.Note(velocity=100, pitch=66, start=6.375, end=6.5625),
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Continue in bar 3 and 4
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),      # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),   # Hihat on 1&
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125),     # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),   # Hihat on 2&
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.5),      # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),     # Hihat on 3&
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),     # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),    # Hihat on 4&
    pretty_midi.Note(velocity=90, pitch=36, start=5.25, end=5.625),     # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),   # Hihat on 1&
    pretty_midi.Note(velocity=90, pitch=38, start=6.0, end=6.375),      # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=6.1875, end=6.375),   # Hihat on 2&
]

for note in drum_notes:
    drums.notes.append(note)

# Add the instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
