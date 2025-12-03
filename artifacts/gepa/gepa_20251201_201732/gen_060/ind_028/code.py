
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # G2
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # E2
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),  # E2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C4

    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F4

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),   # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),   # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),   # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),   # Bb4

    # Resolutions on the last beat of each bar
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G4
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # C4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4, F4, G4, D4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),   # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25)
    # Hihat on every eighth
    for eighth in [bar_start, bar_start + 0.375, bar_start + 0.75, bar_start + 1.125, bar_start + 1.5, bar_start + 1.875]:
        pretty_midi.Note(velocity=100, pitch=42, start=eighth, end=bar_start + 2.25)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
