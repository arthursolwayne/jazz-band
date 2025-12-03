
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F#5
]
sax.notes.extend(sax_notes)

# Bass (walking line: D2-G2, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=80, pitch=44, start=1.75, end=2.0),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),  # G2
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),  # Ab2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # C6 (Dmaj7)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # E6
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # G6
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=2.0),  # A6 (added color),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # B5
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F#5
]
sax.notes.extend(sax_notes)

# Bass (walking line: D2-G2, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),  # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=52, start=3.25, end=3.5),  # B2
    pretty_midi.Note(velocity=80, pitch=43, start=3.5, end=3.75),  # D2
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.0),  # Eb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # E6 (Dmaj7 in different voicing)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # G6
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.5),  # Bb6 (added color)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.5),  # C7 (top)
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D5 (returning to motif)
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F#5
]
sax.notes.extend(sax_notes)

# Bass (walking line: D2-G2, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=52, start=4.5, end=4.75),  # B2
    pretty_midi.Note(velocity=80, pitch=50, start=4.75, end=5.0),  # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=5.0, end=5.25),  # D2
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.5),  # Eb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),  # C6 (Dmaj7)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # E6
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # G6
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=5.0),  # A6
]
piano.notes.extend(piano_notes)

# Drums: Bar 3-4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
