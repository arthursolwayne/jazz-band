
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
# Fm = F, Ab, Cm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=80, pitch=47, start=1.875, end=2.25), # Ab (E2)
    pretty_midi.Note(velocity=80, pitch=46, start=2.25, end=2.625),  # G (D#2)
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0),   # F (D2)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last bar
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F (A3)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # Ab (G3)
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # C (B3)
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),  # Eb (A#3)
    
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625),  # Bb (C4)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D (E4)
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),  # F (A3)
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # Ab (G3)
    
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),   # Eb (A#3)
    pretty_midi.Note(velocity=100, pitch=56, start=2.625, end=3.0),   # G (B3)
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),   # Bb (C4)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D (E4)
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing
# Fm - Ab - Bb - C - F
# F (G4), Ab (Bb4), Bb (B4), C (C5), F (G4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.625),  # F (G4)
    pretty_midi.Note(velocity=110, pitch=70, start=1.625, end=1.75),  # Ab (Bb4)
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=1.875),  # Bb (B4)
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.0),   # C (C5)
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.75),  # F (G4)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
