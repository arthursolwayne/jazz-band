
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# SAX: Tenor motif (start at 1.5s)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7, E♭, F, G, A♭
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # B♭
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # B♭
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # B♭
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # B♭
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # B♭
]
for note in sax_notes:
    sax.notes.append(note)

# BASS: Walking line, chromatic approaches, never the same note twice. He's the anchor.
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=49, start=1.75, end=2.0),  # C#
    pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.5),  # D#
    pretty_midi.Note(velocity=90, pitch=52, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=90, pitch=51, start=2.75, end=3.0),  # D#
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=3.25, end=3.5),  # C#
    pretty_midi.Note(velocity=90, pitch=48, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.0),  # B
    pretty_midi.Note(velocity=90, pitch=48, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=90, pitch=49, start=4.25, end=4.5),  # C#
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=51, start=4.75, end=5.0),  # D#
    pretty_midi.Note(velocity=90, pitch=52, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.5),  # D#
    pretty_midi.Note(velocity=90, pitch=50, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=5.75, end=6.0),  # C#
]
for note in bass_notes:
    bass.notes.append(note)

# PIANO: 7th chords, comp on 2 and 4. Stay out of your way but keep it moving.
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # A
    # Bar 3: Gm7 (G, B♭, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.5),  # B♭
    # Bar 4: Cm7 (C, E♭, G, B♭)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # A
    # Bar 2: Dm7 (D, F, A, C) - again
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # A
    # Bar 3: Gm7 (G, B♭, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # B♭
    # Bar 4: Cm7 (C, E♭, G, B♭)
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),  # A
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2, 6):
    # Kick on 1 and 3
    kick_start = i * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start + 0.75, end=kick_start + 1.125)
    # Snare on 2 and 4
    snare_start = kick_start + 0.375
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_start + 0.125)
    snare_start = kick_start + 1.125
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_start + 0.125)
    # Hi-hat on every eighth
    for j in range(4):
        hihat_start = kick_start + j * 0.375
        pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.375)

drums.notes.extend([pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375) for kick_start in [1.5, 2.25, 3.0, 3.75, 4.5, 5.25]])
drums.notes.extend([pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_start + 0.125) for snare_start in [1.875, 2.625, 3.375, 4.125, 4.875, 5.625]])
drums.notes.extend([pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.375) for hihat_start in [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
