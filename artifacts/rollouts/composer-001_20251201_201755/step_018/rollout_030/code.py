
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in Fm (F, Ab, D, C)
# Bar 2: F (D2), Ab (Eb2), D (F2), C (Eb2)
# Bar 3: F (D2), Ab (Eb2), D (F2), C (Eb2)
# Bar 4: F (D2), Ab (Eb2), D (F2), C (Eb2)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=36, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=36, start=2.625, end=3.0),  # C
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=36, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=36, start=4.125, end=4.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=36, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=36, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Diane - Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes = [
    # Bar 2 - Fm7
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.5 + 0.375),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=61, start=1.5, end=1.5 + 0.375),  # Ab (Eb4)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.5 + 0.375),  # C (G4)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.5 + 0.375),  # D (A4)
    # Bar 3 - Bb7
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.0 + 0.375),  # Bb (F4)
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.0 + 0.375),  # D (A4)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.0 + 0.375),  # F (Bb4)
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.0 + 0.375),  # Ab (Eb4)
    # Bar 4 - Eb7
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.5 + 0.375),  # Eb (D4)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.5 + 0.375),  # G (F4)
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.5 + 0.375),  # Bb (G4)
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.5 + 0.375),  # D (A4)
]
piano.notes.extend(piano_notes)

# Dante - Tenor sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Ab - D - F (F, Ab, D, F)
# First two notes in bar 2, last two in bar 4
sax_notes = [
    # Bar 2 - First two notes
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=2.0),   # Ab (Eb4)
    # Bar 4 - Last two notes
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # D (A4)
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # F (C4)
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
# midi.write disabled
