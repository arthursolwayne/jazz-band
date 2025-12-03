
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches, roots and fifths
bass_notes = [
    # Bar 2 (Fm7 - F, C, Ab, D)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),  # C (fifth)
    pretty_midi.Note(velocity=100, pitch=37, start=2.25, end=2.625),  # Eb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # C (fifth)
    
    # Bar 3 (Ab7 - Ab, Eb, D, G)
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375),  # Ab (root)
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75),  # Eb (fifth)
    pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.125),  # D (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=45, start=4.125, end=4.5),  # Eb (fifth)
    
    # Bar 4 (Dm7 - D, A, F, C)
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # D (root)
    pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.25),  # A (fifth)
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625),  # F (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=47, start=5.625, end=6.0),  # A (fifth)
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.875),  # Ab
]

# Bar 3: Ab7 (Ab, D, Eb, G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.375),  # G
])

# Bar 4: Dm7 (D, F, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.875),  # C
])

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, D, C
# Bar 2: Play F, Ab, D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=40, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=42, start=2.25, end=2.625),  # D
]

# Bar 3: Leave it hanging
# Bar 4: Return and finish with C
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=40, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=42, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=110, pitch=43, start=5.625, end=6.0),  # C
])

sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
])

# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
])

# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
])

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
