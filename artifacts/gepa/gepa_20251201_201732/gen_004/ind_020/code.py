
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

# Drums: Bar 1
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2 starts at 1.5s

# Bass line: Walking line in F (F2 - C3)
bass_notes = [
    # Bar 2: F2 (root), E2 (chromatic approach), F2 (root), G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=73, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # E2
    pretty_midi.Note(velocity=90, pitch=73, start=2.25, end=2.625),  # F2
    pretty_midi.Note(velocity=90, pitch=75, start=2.625, end=3.0),  # G2
    # Bar 3: C3 (fifth), B2 (chromatic approach), C3 (fifth), D3 (seventh)
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=90, pitch=75, start=3.375, end=3.75),  # B2
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125),  # C3
    pretty_midi.Note(velocity=90, pitch=77, start=4.125, end=4.5),  # D3
    # Bar 4: F2 (root), E2 (chromatic approach), F2 (root), G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=73, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # E2
    pretty_midi.Note(velocity=90, pitch=73, start=5.25, end=5.625),  # F2
    pretty_midi.Note(velocity=90, pitch=75, start=5.625, end=6.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # E
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=75, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # Ab
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),  # F#
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - F - C (F, Bb, F, C) in 4th position
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=80, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=80, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=83, start=3.375, end=3.5),   # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
