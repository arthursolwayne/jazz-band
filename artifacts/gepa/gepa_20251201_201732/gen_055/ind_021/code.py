
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line - D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),  # Eb2
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),   # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Motif - start it, leave it hanging
# Play a short, haunting motif on the 3rd beat of bar 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),   # C5
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line - D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125),  # Eb2
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),   # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings - Bar 3: Bbmaj7 (Bb-D-F-A)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # A5
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation - return and finish it
# Resume motif on beat 1 of bar 3, but with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # D5
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # C5
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),   # Bb4
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]

drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line - D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625),  # Eb2
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),   # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings - Bar 4: Gm7 (G-Bb-D-F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G5
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # F5
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation - leave it unresolved
# End on the last note of the motif, unresolved
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # Bb4
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
