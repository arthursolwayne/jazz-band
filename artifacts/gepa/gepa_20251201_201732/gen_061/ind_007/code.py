
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),   # F2

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75),  # Ab2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Bb2
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),   # F2

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625),  # G2
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),   # F2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # D4

    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F4

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # Bb4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm: F, Ab, C, D. Use these notes to create a motif.

# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # Ab4
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625),  # C4
    pretty_midi.Note(velocity=110, pitch=70, start=2.625, end=3.0),   # D4

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # Ab4

    # Bar 4: Come back and finish
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=110, pitch=70, start=4.875, end=5.25),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Add drum fill in bar 3 (1.5s into bar 3 = 3.0s)
# Extra hihat fill
for i in range(4):
    pretty_midi.Note(velocity=80, pitch=42, start=3.0 + i*0.375, end=3.0 + i*0.375 + 0.125)
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0 + i*0.375, end=3.0 + i*0.375 + 0.125))

# Add a snare hit on beat 3 of bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
