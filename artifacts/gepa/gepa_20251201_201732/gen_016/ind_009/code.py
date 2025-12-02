
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # A2 (fifth of Dm)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # D2
    # Bar 3 (3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # D2
    # Bar 4 (4.5s)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),  # A2
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, C, D) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # D4
    # Bar 3: Gm7 (Bb, D, F, G) - open voicing
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G4
    # Bar 4: Cm7 (Eb, G, Bb, C) - open voicing
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=5.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # C5
]
piano_notes.extend([
    # Comp on 2 and 4 (Bar 2: 2.0s, Bar 3: 3.5s, Bar 4: 5.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.125),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.125),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.125),  # C5
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.125),  # D4
    pretty_midi.Note(velocity=90, pitch=57, start=3.5, end=3.625),  # Bb4
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.625),  # D4
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.625),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.625),  # G4
    pretty_midi.Note(velocity=90, pitch=61, start=5.0, end=5.125),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.125),  # G4
    pretty_midi.Note(velocity=90, pitch=65, start=5.0, end=5.125),  # Bb4
    pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.125),  # C5
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm pentatonic - D, F, G, A, C - but not scales, just a phrase
# First motive (1.5s)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875),  # A4
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.0),  # D4 (resolve)
]
# Second motive (4.5s)
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.6875, end=4.875),  # A4
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.0),  # D4 (resolve)
])
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
