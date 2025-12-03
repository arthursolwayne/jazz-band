
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): Walking line, roots and fifths with chromatic approaches
# Key: F major (F, Gm, Am, Bb, C, Dm, Em, F)
# Bar 2: F (root), F# (chromatic approach), G (fifth), G (root)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),  # G

    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),  # C

    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.25), # D#
    pretty_midi.Note(velocity=80, pitch=46, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=80, pitch=46, start=5.625, end=6.0),  # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # E
]

# Bar 3: Gm7 (G, Bb, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F
])

# Bar 4: Am7 (A, C, E, G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # G
])

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, A, Bb, C (F - A - Bb - C), then repeat with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Bar 2
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
])

# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
])

# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
])

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
