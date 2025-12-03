
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (D2 - F#2, chromatic approach to D)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    # Bar 3 (A2 - C#2, chromatic approach to A)
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=46, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.5),
    # Bar 4 (D2 - F#2, chromatic approach to D)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=39, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (D F# A C)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F#
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),  # C
    # Bar 3: Bm7 (B D F# A)
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),  # F#
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),  # A
    # Bar 4: Gmaj7 (G B D F#)
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=6.0),  # B
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),  # F#
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # F#
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4 (full ensemble)
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
