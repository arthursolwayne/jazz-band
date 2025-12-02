
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_end = 1.5
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.0, end=bar1_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.5, end=bar1_start + 1.875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.0, end=bar1_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.375, end=bar1_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.75, end=bar1_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 1.125, end=bar1_start + 1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
# Chromatic walking line starting on F (65)
bar2_start = 1.5
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=65, start=bar2_start + 0.0, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=90, pitch=66, start=bar2_start + 0.375, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=90, pitch=67, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=68, start=bar2_start + 1.125, end=bar2_start + 1.5),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=69, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=90, pitch=70, start=bar2_start + 1.875, end=bar2_start + 2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=bar2_start + 2.25, end=bar2_start + 2.625),
    pretty_midi.Note(velocity=90, pitch=72, start=bar2_start + 2.625, end=bar2_start + 3.0),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=73, start=bar2_start + 3.0, end=bar2_start + 3.375),
    pretty_midi.Note(velocity=90, pitch=74, start=bar2_start + 3.375, end=bar2_start + 3.75),
    pretty_midi.Note(velocity=90, pitch=75, start=bar2_start + 3.75, end=bar2_start + 4.125),
    pretty_midi.Note(velocity=90, pitch=76, start=bar2_start + 4.125, end=bar2_start + 4.5),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords on 2 and 4
# Bar 2: F7 (F, A, C, E flat)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: E7 (E, G#, B, D)
piano_notes = [
    # Bar 2: F7 on 2 and 4
    pretty_midi.Note(velocity=80, pitch=65, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=68, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=71, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=64, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=65, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=80, pitch=68, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=80, pitch=71, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=80, pitch=64, start=bar2_start + 1.5, end=bar2_start + 1.875),
    # Bar 3: Bb7 on 2 and 4
    pretty_midi.Note(velocity=80, pitch=62, start=bar2_start + 2.25, end=bar2_start + 2.625),
    pretty_midi.Note(velocity=80, pitch=65, start=bar2_start + 2.25, end=bar2_start + 2.625),
    pretty_midi.Note(velocity=80, pitch=69, start=bar2_start + 2.25, end=bar2_start + 2.625),
    pretty_midi.Note(velocity=80, pitch=60, start=bar2_start + 2.25, end=bar2_start + 2.625),
    pretty_midi.Note(velocity=80, pitch=62, start=bar2_start + 3.0, end=bar2_start + 3.375),
    pretty_midi.Note(velocity=80, pitch=65, start=bar2_start + 3.0, end=bar2_start + 3.375),
    pretty_midi.Note(velocity=80, pitch=69, start=bar2_start + 3.0, end=bar2_start + 3.375),
    pretty_midi.Note(velocity=80, pitch=60, start=bar2_start + 3.0, end=bar2_start + 3.375),
    # Bar 4: E7 on 2 and 4
    pretty_midi.Note(velocity=80, pitch=64, start=bar2_start + 3.75, end=bar2_start + 4.125),
    pretty_midi.Note(velocity=80, pitch=67, start=bar2_start + 3.75, end=bar2_start + 4.125),
    pretty_midi.Note(velocity=80, pitch=71, start=bar2_start + 3.75, end=bar2_start + 4.125),
    pretty_midi.Note(velocity=80, pitch=69, start=bar2_start + 3.75, end=bar2_start + 4.125),
    pretty_midi.Note(velocity=80, pitch=64, start=bar2_start + 4.5, end=bar2_start + 4.875),
    pretty_midi.Note(velocity=80, pitch=67, start=bar2_start + 4.5, end=bar2_start + 4.875),
    pretty_midi.Note(velocity=80, pitch=71, start=bar2_start + 4.5, end=bar2_start + 4.875),
    pretty_midi.Note(velocity=80, pitch=69, start=bar2_start + 4.5, end=bar2_start + 4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante) - Melody in F (bars 2-4)
# Bar 2: F (65) -> G# (67) -> F (65) -> Bb (62)
# Bar 3: Bb (62) -> C (67) -> D (69) -> F (65)
# Bar 4: F (65) -> G# (67) -> A (69) -> Bb (62)
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 0.0, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 0.375, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 1.125, end=bar2_start + 1.5),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 1.875, end=bar2_start + 2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=bar2_start + 2.25, end=bar2_start + 2.625),
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 2.625, end=bar2_start + 3.0),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 3.0, end=bar2_start + 3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 3.375, end=bar2_start + 3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=bar2_start + 3.75, end=bar2_start + 4.125),
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 4.125, end=bar2_start + 4.5),
]
for note in sax_notes:
    sax.notes.append(note)

# Drums continue in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar2_end = 3.0
bar3_end = 4.5
bar4_end = 6.0

def add_drums(start, end):
    for i in range(4):
        kick_start = start + i * 1.5
        kick_end = kick_start + 0.375
        snare_start = start + i * 1.5 + 0.75
        snare_end = snare_start + 0.375
        hihat_start = start + i * 1.5
        hihat_end = hihat_start + 0.375
        hihat2_start = hihat_start + 0.375
        hihat2_end = hihat2_start + 0.375
        hihat3_start = hihat2_start + 0.375
        hihat3_end = hihat3_start + 0.375
        hihat4_start = hihat3_start + 0.375
        hihat4_end = hihat4_start + 0.375

        # Kick
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
        # Snare
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
        # Hihat
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat2_start, end=hihat2_end))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat3_start, end=hihat3_end))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat4_start, end=hihat4_end))

add_drums(bar2_start, bar2_end)
add_drums(bar2_end, bar3_end)
add_drums(bar3_end, bar4_end)

# Finalize
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
