
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root), E (chromatic approach), C (fifth), D (chromatic)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0),  # D

    # Bar 3: A (chromatic), G (root), E (fifth), F (chromatic)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # F

    # Bar 4: C (chromatic), B (root), G (fifth), A (chromatic)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0), # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0), # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0), # E

    # Bar 3: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=4.5), # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5), # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5), # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5), # C

    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0), # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0), # B
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0), # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0), # F
]

for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante): Short motif, make it sing
# Phrase: F - G - Bb - F (hanging on F)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # F

    # Rest on F for the last two bars
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=6.0),    # F
]

for note in sax_notes:
    sax.notes.append(note)

# Drums in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bars2_4 = []

# Bar 2
drum_notes_bars2_4.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),    # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick
])

# Bar 3
drum_notes_bars2_4.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.5),    # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick
])

# Bar 4
drum_notes_bars2_4.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0),    # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick
])

for note in drum_notes_bars2_4:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
