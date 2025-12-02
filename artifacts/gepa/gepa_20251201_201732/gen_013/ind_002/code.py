
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Dm7: D F A C
# Bar 2: D (38) -> Eb (39) -> F (41) -> G (43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),
    # Bar 3: G (43) -> A (45) -> Bb (46) -> C (48)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=48, start=4.125, end=4.5),
    # Bar 4: C (48) -> D (50) -> Eb (51) -> F (53)
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # C

    # Bar 3: Gm7 (G Bb D F)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F

    # Bar 4: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# You: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 - start with a D, then move to F, then back to D (but with a space)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D (D4)
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),   # F (F4)
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # D (D4)
    pretty_midi.Note(velocity=110, pitch=65, start=2.75, end=3.0),   # F (F4)
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # D (D4)
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0),   # F (F4)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D (D4)
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),   # G (G4)
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # D (D4)
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),   # F (F4)
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # D (D4)
    pretty_midi.Note(velocity=110, pitch=65, start=5.75, end=6.0),   # F (F4)
]

for note in sax_notes:
    sax.notes.append(note)

# Add hihat in bar 2
hihat_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.5 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.625, end=1.625 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.75, end=1.75 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=1.875 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.0 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.125, end=2.125 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.25 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.375, end=2.375 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=2.5 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.625 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.75, end=2.75 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.875, end=2.875 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.0 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=3.125, end=3.125 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=3.25, end=3.25 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.375 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=3.5, end=3.5 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=3.625, end=3.625 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.75 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=3.875, end=3.875 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.0 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.125 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.25, end=4.25 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.375, end=4.375 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.5 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.625, end=4.625 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.75, end=4.75 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=4.875 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.0, end=5.0 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.125, end=5.125 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.25 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.375, end=5.375 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.5, end=5.5 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.625 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.75, end=5.75 + 0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.875, end=5.875 + 0.125)
]

for note in hihat_notes:
    drums.notes.append(note)

# Add snare on 2 and 4
snare_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.5)
]

for note in snare_notes:
    drums.notes.append(note)

# Add kick on 1 and 3
kick_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.90625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.90625)
]

for note in kick_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
