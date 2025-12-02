
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
    # Hihat on every eighth
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

# Bass: Walking line (F2 - A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F - G - E - F
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=55, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),  # F2
    # Bar 3: Bb - A - G - Bb
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=80, pitch=55, start=3.375, end=3.75),  # A2
    pretty_midi.Note(velocity=80, pitch=54, start=3.75, end=4.125),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=57, start=4.125, end=4.5),  # Bb2
    # Bar 4: F - E - D - F
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=51, start=4.875, end=5.25),  # E2
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.625),  # D2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0),  # F2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Eb4
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F4 (same pitch as D4)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Ab4
    # Bar 4: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Eb4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Ab - C - Bb (Fm7 with a chromatic approach to Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # Ab4
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=3.0),  # C4
    pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # F4 (returning)
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # Ab4
    pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.625),  # C4
    pretty_midi.Note(velocity=110, pitch=70, start=5.625, end=6.0),  # Bb4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2 kicks
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Bar 3 kicks
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Bar 4 kicks
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Bar 2 snare
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Bar 3 snare
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    # Bar 4 snare
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    # Hihat for bar 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    # Hihat for bar 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    # Hihat for bar 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
