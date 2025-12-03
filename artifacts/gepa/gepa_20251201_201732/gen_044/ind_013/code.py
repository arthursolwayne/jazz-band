
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

# Bass line: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root) and C (fifth)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F3
    pretty_midi.Note(velocity=100, pitch=77, start=1.875, end=2.25),  # C4
    # Bar 3: E (chromatic approach) and B (fifth of C)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # E3
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),   # B3
    # Bar 4: F (root) and C (fifth)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F3
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75),  # C4
    # Bar 5: E (chromatic approach) and B (fifth of C)
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # E3
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),   # B3
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # F3
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=2.25),  # A3
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=2.25),  # C4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),  # E3
    # Bar 3: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=75, start=2.25, end=3.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=3.0),  # Bb4
    # Bar 4: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),  # F3
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.75),  # A3
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.75),  # C4
    pretty_midi.Note(velocity=100, pitch=75, start=3.0, end=3.75),  # Eb4
]
piano.notes.extend(piano_notes)

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif starts (F, G, E, D)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F3
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # G3
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # E3
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # D3
    # Bar 3: Let the motif hang, nothing from sax
    # Bar 4: Repeat the motif, finished this time
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F3
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # G3
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # E3
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # D3
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
