
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full band starts
# Bass: Walking line in F (F2, A2, C3, D3)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=77, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=80, start=1.875, end=2.25),  # A2
    pretty_midi.Note(velocity=80, pitch=84, start=2.25, end=2.625),  # C3
    pretty_midi.Note(velocity=80, pitch=85, start=2.625, end=3.0),   # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicing, Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=80, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.875),  # E
]
piano.notes.extend(piano_notes)

# Sax: Melody, one short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=72, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=105, pitch=76, start=1.875, end=2.25),  # Bb4
    pretty_midi.Note(velocity=105, pitch=77, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=105, pitch=76, start=2.625, end=3.0),   # Bb4
]
sax.notes.extend(sax_notes)

# Bar 3: Continue with full band
# Bass: Walking line in F (F2, A2, C3, D3)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=77, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=80, start=3.375, end=3.75),  # A2
    pretty_midi.Note(velocity=80, pitch=84, start=3.75, end=4.125),  # C3
    pretty_midi.Note(velocity=80, pitch=85, start=4.125, end=4.5),   # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicing, Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=80, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.375),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: Melody, continue the motif
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=72, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=105, pitch=76, start=3.375, end=3.75),  # Bb4
    pretty_midi.Note(velocity=105, pitch=77, start=3.75, end=4.125),  # B4
    pretty_midi.Note(velocity=105, pitch=76, start=4.125, end=4.5),   # Bb4
]
sax.notes.extend(sax_notes)

# Bar 4: Continue with full band
# Bass: Walking line in F (F2, A2, C3, D3)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=77, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=80, start=4.875, end=5.25),  # A2
    pretty_midi.Note(velocity=80, pitch=84, start=5.25, end=5.625),  # C3
    pretty_midi.Note(velocity=80, pitch=85, start=5.625, end=6.0),   # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicing, Em7 (E, G, B, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=89, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=91, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Sax: Melody, finish the motif
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=72, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=105, pitch=76, start=4.875, end=5.25),  # Bb4
    pretty_midi.Note(velocity=105, pitch=77, start=5.25, end=5.625),  # B4
    pretty_midi.Note(velocity=105, pitch=76, start=5.625, end=6.0),   # Bb4
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
