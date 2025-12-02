
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2 - Bb2, MIDI 53 - 57), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625),  # Bb2
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),   # F2 (root)

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125),  # F2
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),   # Bb2

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625),  # Bb2
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),   # F2
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Fm7 | Bb7 | Eb7 | Ab7
# Bar 2: Fm7 (F, Ab, C, Eb) -> open voicing
# Bar 3: Bb7 (Bb, D, F, Ab) -> open voicing
# Bar 4: Eb7 (Eb, G, Bb, D) -> open voicing
# Bar 5: Ab7 (Ab, C, Eb, G) -> open voicing

piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # Eb5

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # Ab5

    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # D5

    # Bar 5: Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=90, pitch=60, start=6.0, end=6.375),  # Ab4
    pretty_midi.Note(velocity=90, pitch=67, start=6.0, end=6.375),  # C5
    pretty_midi.Note(velocity=90, pitch=62, start=6.0, end=6.375),  # Eb5
    pretty_midi.Note(velocity=90, pitch=64, start=6.0, end=6.375),  # G5
]

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, D (Fm7 arpeggio, short and suspended)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625),  # F4
    pretty_midi.Note(velocity=110, pitch=60, start=1.625, end=1.75),  # Ab4
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.875),  # Bb4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0),   # D5

    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.125),  # D5 (return and finish)
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
