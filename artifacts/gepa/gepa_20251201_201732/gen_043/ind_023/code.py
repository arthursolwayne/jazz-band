
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

# Drums
drum_notes = [
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Melody - short motif, start and leave hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F#5
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # A5
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # F#5
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D5
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # C5
]
sax.notes.extend(sax_notes)

# Bass: Walking line (D2-G2), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=80, pitch=51, start=1.75, end=2.0),  # Eb2 (approach)
    pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.25),  # E2
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.5),  # G2
    pretty_midi.Note(velocity=80, pitch=57, start=2.5, end=2.75),  # A2
    pretty_midi.Note(velocity=80, pitch=55, start=2.75, end=3.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on last chord
piano_notes = [
    # Bar 2: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=55, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=57, start=1.5, end=1.75),
    
    # Bar 3: Bm7 (B, D, F#, A)
    pretty_midi.Note(velocity=80, pitch=57, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=60, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.25),
    
    # Bar 4: G7 (G, B, D, F#)
    pretty_midi.Note(velocity=80, pitch=55, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=58, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=60, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.75),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif, complete it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F#5
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # A5
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # F#5
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # D5
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # C5
]
sax.notes.extend(sax_notes)

# Bass: Walking line (D2-G2), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),  # D2
    pretty_midi.Note(velocity=80, pitch=51, start=3.25, end=3.5),  # Eb2 (approach)
    pretty_midi.Note(velocity=80, pitch=52, start=3.5, end=3.75),  # E2
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.0),  # G2
    pretty_midi.Note(velocity=80, pitch=57, start=4.0, end=4.25),  # A2
    pretty_midi.Note(velocity=80, pitch=55, start=4.25, end=4.5),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on last chord
piano_notes = [
    # Bar 3: Bm7 (B, D, F#, A)
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.25),
    
    # Bar 4: G7 (G, B, D, F#)
    pretty_midi.Note(velocity=80, pitch=55, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=58, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=60, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),
    
    # Bar 4: G7 (same chord on beat 2 and 4)
    pretty_midi.Note(velocity=80, pitch=55, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=58, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=60, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.25),
]
piano.notes.extend(piano_notes)

# Bar 4: Drums (4.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
