
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
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)     # Hihat on every eighth
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2, G2, A2, C3) with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=54, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),  # C3
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=54, start=3.375, end=3.75), # G2
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125), # A2
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),  # C3
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=54, start=4.875, end=5.25), # G2
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.625), # A2
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0)   # C3
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, comp on 2 and 4
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # E

    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F

    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # G
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.875), # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.625), # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.375, end=4.625), # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.125), # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.875), # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.875, end=6.0),  # G (resolve)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Fill the bar
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 4

    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 4

    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
