
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line with roots and fifths, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25),  # F#2
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),  # A2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7sus4 (D, G, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=3.0),  # C#4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Short motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # B4
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # C#5
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line with roots and fifths, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.75),  # B2
    pretty_midi.Note(velocity=90, pitch=56, start=3.75, end=4.125),  # A#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=59, start=4.125, end=4.5),  # D3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bm7 (B, D, F#, A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=4.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # A4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # C#5
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # B4
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),  # E5
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line with roots and fifths, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.875),  # D3
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # F#3
    pretty_midi.Note(velocity=90, pitch=61, start=5.25, end=5.625),  # E3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # G3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: G7 (G, B, D, F#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # F#5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish the motif and resolve
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # G5
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.25),  # G5
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625),  # G5
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0),  # G5
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    # Hihat on every eighth
    for i in range(4):
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + (i + 1) * 0.375))
    # Kick on 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
