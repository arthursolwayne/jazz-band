
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),   # F (root)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # Ab (fifth)
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),  # G (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),   # F (root)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord per bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # D
]
piano.notes.extend(piano_notes)

# Sax: short motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),  # C
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: walking line, root and fifth with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),   # Ab (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75),  # Bb (chromatic)
    pretty_midi.Note(velocity=80, pitch=41, start=3.75, end=4.125),  # Ab (fifth)
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),   # F (root)
]
bass.notes.extend(bass_notes)

# Piano: Dm7 (D, F, A, B)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # B
]
piano.notes.extend(piano_notes)

# Sax: continue the motif, resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5),  # C
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: walking line, root and fifth with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),   # F (root)
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25),  # Ab (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),  # Bb (chromatic)
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=6.0),   # Ab (fifth)
]
bass.notes.extend(bass_notes)

# Piano: Gm7 (G, Bb, D, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Eb
]
piano.notes.extend(piano_notes)

# Drum fill
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),  # Kick on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),   # Kick on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Sax: resolve motif, close it out
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=6.0),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
