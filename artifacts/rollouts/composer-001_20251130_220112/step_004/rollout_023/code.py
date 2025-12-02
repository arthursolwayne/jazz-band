
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=3.0),  # G#
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75), # A#
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=56, start=4.875, end=5.25), # C#
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=58, start=5.625, end=6.0),  # D#
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875),  # F7: F, A, C, E
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.875),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.375),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One motif, make it sing
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),  # Bb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5),  # Bb
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25)
    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.875, end=start + 2.25)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 2.25, end=start + 2.625)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 2.625, end=start + 3.0)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
