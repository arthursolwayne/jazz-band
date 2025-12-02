
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
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),  # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),  # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2 to C), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.625),  # E2
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0),  # F2

    # Bar 3 (3.0s)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75),  # G2
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125),  # E2
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),  # F2

    # Bar 4 (4.5s)
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25),  # G2
    pretty_midi.Note(velocity=100, pitch=52, start=5.25, end=5.625),  # E2
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),  # F2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Fm7 -> Bb7 -> Eb7 -> Am7
piano_notes = [
    # Bar 2 (1.5s) - Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=1.875),  # D4

    # Bar 3 (3.0s) - Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Ab4

    # Bar 4 (4.5s) - Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # D4

    # Bar 4 (4.5s) - Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # C4
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625),  # E4
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625),  # G4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4, Ab4, C4, Bb4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),   # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),   # C4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),   # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),   # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5),   # C4
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.75),   # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),   # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),   # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=4.25, end=4.5),   # C4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),   # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),   # F4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2, 3, 4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1 (bar_start)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2 (bar_start + 0.75)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375))
    # Kick on 3 (bar_start + 1.125)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5))
    # Snare on 4 (bar_start + 1.875)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
