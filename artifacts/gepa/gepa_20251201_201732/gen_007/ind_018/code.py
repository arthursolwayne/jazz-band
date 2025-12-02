
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    # D2 (Dm root)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    # F2 (Dm 3rd) with chromatic approach from E2
    pretty_midi.Note(velocity=80, pitch=37, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=39, start=2.0, end=2.375),
    # A2 (Dm 5th) with chromatic approach from G#2
    pretty_midi.Note(velocity=80, pitch=38, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=40, start=2.5, end=2.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875),  # A3
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875),  # F3
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D3
    # Bar 3: Gm7 (G Bb D F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # Bb3
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625),  # G3
    # Bar 4: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),  # C4
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Sax: Bar 2-4 (1.5 - 6.0s)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm7 -> Gm7 -> Cm7
sax_notes = [
    # Bar 2: D (D3), Bb (Bb3), D (D4), Bb (Bb4)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=57, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0625, end=2.25),
    # Bar 3: G (G3), D (D4), G (G4), D (D5) – leave it hanging at the end
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=100, pitch=62, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=72, start=2.8125, end=3.0),
    # Bar 4: C (C4), Bb (Bb4), C (C5), Bb (Bb5)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=67, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=77, start=3.5625, end=3.75),
    # Bar 4: End with a long Bb5 (Bb5) to make it sing
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.5),
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
