
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (MIDI 53) to Bb2 (MIDI 57), walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75),  # F2
    pretty_midi.Note(velocity=80, pitch=55, start=1.75, end=2.0),  # G2
    pretty_midi.Note(velocity=80, pitch=57, start=2.0, end=2.25),  # Bb2
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.5),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chords each bar (Bar 2: Fm7)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0),  # Bb4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.0),  # D5
]
piano.notes.extend(piano_notes)

# Sax: Motif (F4, Ab4, Bb4, D5) - one short phrase
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # D5
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, Fm7 -> Bbm7
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.25),  # Bb2
    pretty_midi.Note(velocity=80, pitch=59, start=3.25, end=3.5),  # C2
    pretty_midi.Note(velocity=80, pitch=53, start=3.5, end=3.75),  # F2
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Bbm7 open voicing
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.5),  # F4
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.5),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: Motif variation (Ab4, Bb4, F4, G4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),  # G4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, Bbm7 -> F7
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.75),  # G2
    pretty_midi.Note(velocity=80, pitch=57, start=4.75, end=5.0),  # Bb2
    pretty_midi.Note(velocity=80, pitch=59, start=5.0, end=5.25),  # C2
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),  # E2
]
bass.notes.extend(bass_notes)

# Piano: F7 open voicing
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.0),  # F4
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.0),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.0),  # D5
]
piano.notes.extend(piano_notes)

# Sax: Motif resolution (F4, G4, Ab4, Bb4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # Bb4
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
