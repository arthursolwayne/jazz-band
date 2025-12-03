
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short, haunting motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D5
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # E5
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D5
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # C5
]
sax.notes.extend(sax_notes)

# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.75),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=44, start=1.75, end=2.0),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=46, start=2.0, end=2.25),  # F2 (fifth)
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.5),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=2.75),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=44, start=2.75, end=3.0),  # Eb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar
# Bar 2: G7sus4 (D, G, B, D)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75),
]
piano.notes.extend(piano_notes)

# Bar 3: Bm7 (B, D, F#, A)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=79, start=3.0, end=3.25),
]
piano.notes.extend(piano_notes)

# Bar 4: C7 (C, E, G, B)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continuation of the motif, but incomplete
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # F#5 (shifting)
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # E5
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # F#5
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # G5
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # F#5
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # E5
]
sax.notes.extend(sax_notes)

# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.25),  # B2 (root)
    pretty_midi.Note(velocity=90, pitch=51, start=3.25, end=3.5),  # C2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=3.5, end=3.75),  # D2 (fifth)
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.0),  # C#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=4.0, end=4.25),  # B2 (root)
    pretty_midi.Note(velocity=90, pitch=51, start=4.25, end=4.5),  # C2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: finish the motif, resolve on D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # E5 (half-step up)
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D5
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # C5
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D5
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # C5
]
sax.notes.extend(sax_notes)

# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.75),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=44, start=4.75, end=5.0),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=46, start=5.0, end=5.25),  # F2 (fifth)
    pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.5),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.5, end=5.75),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=44, start=5.75, end=6.0),  # Eb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, resolve on the last chord (C7)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=60, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=64, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=71, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=60, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=64, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=67, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=71, start=5.5, end=5.75),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
