
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: All instruments in. Sax takes the melody.
# Dmaj7 -> G7 -> Cm7 -> F7
# Sax: short motif, start, leave it hanging, come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D (start motif)
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75), # F# (leave it hanging)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75), # D (come back)
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=2.875), # A (finish motif)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.75),   # D2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=1.75, end=2.0),   # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.25),   # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.5),   # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=45, start=2.5, end=2.75),   # A2 (root)
    pretty_midi.Note(velocity=80, pitch=47, start=2.75, end=3.0),   # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.25),   # C3 (fifth)
    pretty_midi.Note(velocity=80, pitch=48, start=3.25, end=3.5),   # B2 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),  # F#
]

# Bar 3: G7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=81, start=2.0, end=2.25),  # F#
])

# Bar 4: Cm7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.75),  # Eb
])

# Bar 4: F7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.25),  # E
])

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
