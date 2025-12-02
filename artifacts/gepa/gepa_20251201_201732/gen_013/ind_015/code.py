
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
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

# Marcus (Bass): Walking line in F, roots and fifths, chromatic approaches
# F2 (D2 in MIDI: 38), G2 (43), C3 (48), D3 (50), F3 (53), etc.
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0),   # C3 (next root)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # D3 (root)
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75),  # E3 (chromatic)
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125),  # F3 (fifth)
    pretty_midi.Note(velocity=90, pitch=58, start=4.125, end=4.5),   # A3 (next root)

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.875),  # A3 (root)
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # Bb3 (chromatic)
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.625),  # B3 (fifth)
    pretty_midi.Note(velocity=90, pitch=68, start=5.625, end=6.0),   # D4 (next root)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane (Piano): Open voicings, one chord per bar, resolve on last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F (bar 2)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # E

    # Bar 3: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),  # F#
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # C

    # Bar 4: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Dante (Sax): One short motif, sing it, leave it hanging, come back and finish
# Motif: F, Bb, G, G
# Start at 1.5s, end at 2.25s (first bar of the melody)
# Then repeat at 4.5s, end at 5.25s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),   # G

    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),   # G
]

for note in sax_notes:
    sax.notes.append(note)

# Final setup
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
