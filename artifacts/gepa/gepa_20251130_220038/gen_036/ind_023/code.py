
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
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
for note in drums_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),   # G#
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=80, pitch=54, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=57, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=80, pitch=58, start=4.5, end=4.875),   # C#
    pretty_midi.Note(velocity=80, pitch=59, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),   # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),   # F7
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),   # F7
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Whisper at first, then a cry
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),   # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),   # D
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),   # E
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),   # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75),   # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.0),   # G
    pretty_midi.Note(velocity=100, pitch=76, start=4.0, end=4.25),   # A
    pretty_midi.Note(velocity=100, pitch=78, start=4.25, end=4.5),   # B
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=100, pitch=82, start=4.75, end=5.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=84, start=5.0, end=5.25),   # F
    pretty_midi.Note(velocity=100, pitch=87, start=5.25, end=5.5),   # A
    pretty_midi.Note(velocity=100, pitch=89, start=5.5, end=5.75),   # B
    pretty_midi.Note(velocity=100, pitch=91, start=5.75, end=6.0),   # D
]
for note in sax_notes:
    sax.notes.append(note)

# Drums in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_pattern = [
    (36, 0.0), (38, 0.375), (42, 0.0),
    (36, 0.75), (38, 1.125), (42, 0.75),
    (36, 1.5), (38, 1.875), (42, 1.5),
    (36, 2.25), (38, 2.625), (42, 2.25),
    (36, 3.0), (38, 3.375), (42, 3.0),
    (36, 3.75), (38, 4.125), (42, 3.75),
    (36, 4.5), (38, 4.875), (42, 4.5),
    (36, 5.25), (38, 5.625), (42, 5.25),
]

for i in range(len(drum_pattern)):
    pitch, start = drum_pattern[i]
    end = start + 0.375
    if i % 2 == 0:
        end = start + 0.75
    if pitch == 42:
        end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start + 1.5, end=end + 1.5))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
