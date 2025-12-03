
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Eb2 on 2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2 on 3
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on bar 2
piano_notes = [
    # Bar 2 (1.5-2.25)
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.25),  # Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),
    # Bar 3 (2.25-3.0)
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=3.0),  # Gm7 (G, Bb, D, E)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # E4 (Dm7)
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # G4 (Dm7)
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # E4 (Dm7)
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.75),  # F4 (Dm7)
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),  # E4 (Dm7)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: D2 (MIDI 38) walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2 on 1
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),  # Eb2 on 2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # G2 on 3
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # D2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on bar 3
piano_notes = [
    # Bar 3 (3.0-3.75)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.75),  # Fm7
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75),
    # Bar 4 (3.75-4.5)
    pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.5),  # Gm7
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25),  # F4 (Dm7)
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # E4 (Dm7)
    pretty_midi.Note(velocity=110, pitch=60, start=3.5, end=3.75),  # D4 (Dm7)
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # E4 (Dm7)
    pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.25),  # F4 (Dm7)
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),  # E4 (Dm7)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums: Kick on 1, snare on 2, kick on 3, snare on 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
]
drums.notes.extend(drum_notes)

# Bass: D2 (MIDI 38) walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2 on 1
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625),  # Eb2 on 2
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # G2 on 3
    pretty_midi.Note(velocity=90, pitch=38, start=6.0, end=6.375),  # D2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on bar 4
piano_notes = [
    # Bar 4 (4.5-5.25)
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=5.25),  # Fm7
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.25),
    # Bar 4 (5.25-6.0)
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=6.0),  # Gm7
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: End with a strong note, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=5.0),  # E4 (Dm7)
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.5),  # F4 (Dm7)
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=6.0),  # E4 (Dm7)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
