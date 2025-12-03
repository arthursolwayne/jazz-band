
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root), G (fifth), E (chromatic approach), F (root)
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=73, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=80, pitch=70, start=2.25, end=2.625), # E2
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),  # F2

    # Bar 3: C (root), D (fifth), B (chromatic approach), C (root)
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # C2
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75), # D2
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.125), # B2
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),  # C2

    # Bar 4: F (root), G (fifth), E (chromatic approach), F (root)
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=73, start=4.875, end=5.25), # G2
    pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.625), # E2
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Diane on piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # A2
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.875),  # Bb2
    pretty_midi.Note(velocity=90, pitch=78, start=1.5, end=1.875),  # C3
    pretty_midi.Note(velocity=90, pitch=83, start=1.5, end=1.875),  # E3

    # Bar 3: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # C2
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # E2
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375),  # C3

    # Bar 4: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # A2
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),  # Bb2
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=90, pitch=80, start=4.5, end=4.875),  # Eb3
]
piano.notes.extend(piano_notes)

# Dante on sax: one short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Motif start
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # G4

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # G4

    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # G4
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
