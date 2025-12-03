
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
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, roots and fifths, chromatic approaches
bass_notes = [
    # Bar 2: Fm (F, C, D#, F)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # C2
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # D#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # F2
    # Bar 3: Gm7 (G, D, F, G)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # D2
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # F2
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),  # G2
    # Bar 4: Cm7 (C, G, Bb, C)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # C2
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # G2
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # C2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=1.875),  # D4
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F4
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: motif, one short phrase, make it sing
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.65),  # F4
    pretty_midi.Note(velocity=110, pitch=73, start=1.65, end=1.8),  # G4
    pretty_midi.Note(velocity=110, pitch=71, start=1.8, end=1.95),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=1.95, end=2.1),  # E4
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=73, start=3.0, end=3.15),  # G4
    pretty_midi.Note(velocity=110, pitch=71, start=3.15, end=3.3),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=3.3, end=3.45),  # E4
    pretty_midi.Note(velocity=110, pitch=67, start=3.45, end=3.6),  # D4
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.65),  # F4
    pretty_midi.Note(velocity=110, pitch=73, start=4.65, end=4.8),  # G4
    pretty_midi.Note(velocity=110, pitch=71, start=4.8, end=4.95),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=4.95, end=5.1),  # E4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
# midi.write disabled
