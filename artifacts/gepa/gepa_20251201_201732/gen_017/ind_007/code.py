
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
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # E5
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # D5
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # C5
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # E5
]
sax.notes.extend(sax_notes)

# Bass: Walking line (F - A - C - D)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),  # A2
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=2.625),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),  # A2
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),  # D3
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125),  # C3
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),  # E3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 2: F7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # E5
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # F5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # A5
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # C6
]
piano.notes.extend(piano_notes)

# Bar 3: G7 (G B D F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # F5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # G5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # B5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),  # D6
]
piano.notes.extend(piano_notes)

# Bar 4: C7 (C E G B)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # C6
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75),  # E6
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),  # G6
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.75),  # B6
]
piano.notes.extend(piano_notes)

# Drums: Continue (3.0 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Sax: Finish the motif on the last bar
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # E5
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # E5
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # E5
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # D5
]
sax.notes.extend(sax_notes)

# Bass: Walking line (C - E - G - A)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75),  # E3
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125),  # D3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),  # E3
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # G3
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25),  # A3
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625),  # G3
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # C4
]
bass.notes.extend(bass_notes)

midi.instruments.extend([sax, bass, piano, drums])
