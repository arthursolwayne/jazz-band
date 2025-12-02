
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
    # Hihat on every eighth
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
# Bass: Walking line, chromatic approaches
bass_notes = [
    # D (D4) on 1
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    # C# (C#4) on & of 1
    pretty_midi.Note(velocity=85, pitch=61, start=1.875, end=2.0),
    # B (B3) on 2
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.375),
    # A (A3) on & of 2
    pretty_midi.Note(velocity=85, pitch=59, start=2.375, end=2.5),
    # G (G3) on 3
    pretty_midi.Note(velocity=90, pitch=58, start=2.5, end=2.875),
    # F# (F#3) on & of 3
    pretty_midi.Note(velocity=85, pitch=57, start=2.875, end=3.0),
    # E (E3) on 4
    pretty_midi.Note(velocity=90, pitch=56, start=3.0, end=3.375),
    # D (D3) on & of 4
    pretty_midi.Note(velocity=85, pitch=55, start=3.375, end=3.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # D7 on 1
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=1.875),  # B
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.875),  # F#
    # D7 on 2
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.375),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=2.0, end=2.375),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=2.0, end=2.375),  # B
    pretty_midi.Note(velocity=85, pitch=64, start=2.0, end=2.375),  # F#
    # D7 on 3
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.875),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=2.5, end=2.875),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=2.5, end=2.875),  # B
    pretty_midi.Note(velocity=85, pitch=64, start=2.5, end=2.875),  # F#
    # D7 on 4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=85, pitch=64, start=3.0, end=3.375),  # F#
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (D4) on 1
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    # E (E4) on & of 1
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.0),
    # F# (F#4) on 2
    pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.375),
    # G (G4) on & of 2
    pretty_midi.Note(velocity=110, pitch=67, start=2.375, end=2.5),
    # D (D4) on 3
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.875),
    # E (E4) on & of 3
    pretty_midi.Note(velocity=110, pitch=64, start=2.875, end=3.0),
    # F# (F#4) on 4
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),
    # G (G4) on & of 4
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    # D (D4) on 1
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.875),
    # C# (C#4) on & of 1
    pretty_midi.Note(velocity=85, pitch=61, start=3.875, end=4.0),
    # B (B3) on 2
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.375),
    # A (A3) on & of 2
    pretty_midi.Note(velocity=85, pitch=59, start=4.375, end=4.5),
    # G (G3) on 3
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.875),
    # F# (F#3) on & of 3
    pretty_midi.Note(velocity=85, pitch=57, start=4.875, end=5.0),
    # E (E3) on 4
    pretty_midi.Note(velocity=90, pitch=56, start=5.0, end=5.375),
    # D (D3) on & of 4
    pretty_midi.Note(velocity=85, pitch=55, start=5.375, end=5.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # D7 on 1
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.875),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=3.5, end=3.875),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=3.5, end=3.875),  # B
    pretty_midi.Note(velocity=85, pitch=64, start=3.5, end=3.875),  # F#
    # D7 on 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.375),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=4.0, end=4.375),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=4.0, end=4.375),  # B
    pretty_midi.Note(velocity=85, pitch=64, start=4.0, end=4.375),  # F#
    # D7 on 3
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=85, pitch=64, start=4.5, end=4.875),  # F#
    # D7 on 4
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.375),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=5.0, end=5.375),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=5.0, end=5.375),  # B
    pretty_midi.Note(velocity=85, pitch=64, start=5.0, end=5.375),  # F#
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, resolve it
sax_notes = [
    # D (D4) on 1
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.875),
    # E (E4) on & of 1
    pretty_midi.Note(velocity=110, pitch=64, start=3.875, end=4.0),
    # F# (F#4) on 2
    pretty_midi.Note(velocity=110, pitch=66, start=4.0, end=4.375),
    # G (G4) on & of 2
    pretty_midi.Note(velocity=110, pitch=67, start=4.375, end=4.5),
    # D (D4) on 3
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),
    # E (E4) on & of 3
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.0),
    # F# (F#4) on 4
    pretty_midi.Note(velocity=110, pitch=66, start=5.0, end=5.375),
    # G (G4) on & of 4
    pretty_midi.Note(velocity=110, pitch=67, start=5.375, end=5.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    # D (D4) on 1
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.875),
    # C# (C#4) on & of 1
    pretty_midi.Note(velocity=85, pitch=61, start=5.875, end=6.0),
    # B (B3) on 2
    pretty_midi.Note(velocity=90, pitch=60, start=6.0, end=6.375),
    # A (A3) on & of 2
    pretty_midi.Note(velocity=85, pitch=59, start=6.375, end=6.5),
    # G (G3) on 3
    pretty_midi.Note(velocity=90, pitch=58, start=6.5, end=6.875),
    # F# (F#3) on & of 3
    pretty_midi.Note(velocity=85, pitch=57, start=6.875, end=7.0),
    # E (E3) on 4
    pretty_midi.Note(velocity=90, pitch=56, start=7.0, end=7.375),
    # D (D3) on & of 4
    pretty_midi.Note(velocity=85, pitch=55, start=7.375, end=7.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # D7 on 1
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.875),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=5.5, end=5.875),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=5.5, end=5.875),  # B
    pretty_midi.Note(velocity=85, pitch=64, start=5.5, end=5.875),  # F#
    # D7 on 2
    pretty_midi.Note(velocity=90, pitch=62, start=6.0, end=6.375),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=6.0, end=6.375),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=6.0, end=6.375),  # B
    pretty_midi.Note(velocity=85, pitch=64, start=6.0, end=6.375),  # F#
    # D7 on 3
    pretty_midi.Note(velocity=90, pitch=62, start=6.5, end=6.875),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=6.5, end=6.875),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=6.5, end=6.875),  # B
    pretty_midi.Note(velocity=85, pitch=64, start=6.5, end=6.875),  # F#
    # D7 on 4
    pretty_midi.Note(velocity=90, pitch=62, start=7.0, end=7.375),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=7.0, end=7.375),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=7.0, end=7.375),  # B
    pretty_midi.Note(velocity=85, pitch=64, start=7.0, end=7.375),  # F#
]
piano.notes.extend(piano_notes)

# Sax: End on G (G4) and leave it hanging
sax_notes = [
    # D (D4) on 1
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.875),
    # E (E4) on & of 1
    pretty_midi.Note(velocity=110, pitch=64, start=5.875, end=6.0),
    # F# (F#4) on 2
    pretty_midi.Note(velocity=110, pitch=66, start=6.0, end=6.375),
    # G (G4) on & of 2
    pretty_midi.Note(velocity=110, pitch=67, start=6.375, end=6.5),
    # D (D4) on 3
    pretty_midi.Note(velocity=110, pitch=62, start=6.5, end=6.875),
    # E (E4) on & of 3
    pretty_midi.Note(velocity=110, pitch=64, start=6.875, end=7.0),
    # F# (F#4) on 4
    pretty_midi.Note(velocity=110, pitch=66, start=7.0, end=7.375),
    # G (G4) on & of 4
    pretty_midi.Note(velocity=110, pitch=67, start=7.375, end=7.5),
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.625, end=4.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.0, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0625, end=4.25),
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.4375, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=4.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.8125, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=5.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.9375, end=6.125),
    pretty_midi.Note(velocity=90, pitch=42, start=6.125, end=6.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=6.3125, end=6.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
