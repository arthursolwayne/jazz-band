
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.625), # C (fifth)
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0),  # Bb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # F (root)
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75), # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125), # C (fifth)
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5),  # Bb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.625), # C (fifth)
    pretty_midi.Note(velocity=80, pitch=44, start=5.625, end=6.0),  # Bb (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.25),  # E
]
# Bar 3: Bbmaj7 (Bb D F A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=3.0),  # A
])
# Bar 4: Dm7 (D F A C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.75),  # C
])
# Resolving chord: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=6.0),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=6.0),  # F
])

for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.25),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.999), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.75),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.25),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
]

for note in drum_notes:
    drums.notes.append(note)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - A - F - D (F6 - A6 - F6 - D6)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F6
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A6
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.999), # F6 (return)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D6
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F6 (finish)
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # A6
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F6
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D6
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
