
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
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: All instruments come in
# Bass: D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25),  # Eb2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),  # E2
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),   # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # C4
]
piano.notes.extend(piano_notes)

# Sax: Motif - start it, leave it hanging, come back
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),  # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.5),  # C4
]
piano.notes.extend(piano_notes)

# Bass: D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=2.0, end=2.375),  # D2
    pretty_midi.Note(velocity=80, pitch=39, start=2.375, end=2.75),  # Eb2
    pretty_midi.Note(velocity=80, pitch=40, start=2.75, end=3.125),  # E2
    pretty_midi.Note(velocity=80, pitch=43, start=3.125, end=3.5),   # G2
]
bass.notes.extend(bass_notes)

# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # B4 (continuation)
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.5),  # F4
]
sax.notes.extend(sax_notes)

# Bar 4: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0),  # C4
]
piano.notes.extend(piano_notes)

# Bass: D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=2.5, end=2.875),  # D2
    pretty_midi.Note(velocity=80, pitch=39, start=2.875, end=3.25),  # Eb2
    pretty_midi.Note(velocity=80, pitch=40, start=3.25, end=3.625),  # E2
    pretty_midi.Note(velocity=80, pitch=43, start=3.625, end=4.0),   # G2
]
bass.notes.extend(bass_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # D4 (finish the motif)
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.125, end=3.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.75, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=3.875, end=4.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.3125, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
