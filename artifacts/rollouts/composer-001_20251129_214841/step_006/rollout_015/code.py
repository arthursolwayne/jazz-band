
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.append(drum_kick)
drums.notes.append(drum_kick2)

# Snare on 2 and 4
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drums.notes.append(drum_snare)
drums.notes.append(drum_snare2)

# Hihat on every eighth
hihat_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
for note in hihat_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),   # D#
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),   # E
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),   # G#
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.625),  # A#
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),   # B
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 2 (1.5 - 3.0s) - C7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25)   # B
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3 (3.0 - 4.5s) - D7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75)   # C
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4 (4.5 - 6.0s) - E7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25)   # C
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif in C, one phrase, leave it hanging
# Bar 2 (1.5 - 3.0s) - Motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),   # E
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),   # G
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3 (3.0 - 4.5s) - Repeat motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),   # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),   # G
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4 (4.5 - 6.0s) - End on a question
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),   # E
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),   # G
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
