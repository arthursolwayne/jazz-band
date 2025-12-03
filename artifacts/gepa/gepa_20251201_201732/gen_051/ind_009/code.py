
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in F minor with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),   # F2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625),  # F#2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),   # A2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, comp on 2 and 4
# Bar 2: F7sus4 (F, A, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=2.25),  # D
]
piano.notes.extend(piano_notes)

# Sax: motif starts now
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # D5
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25),  # F5
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # Eb5
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),   # F5
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in F minor with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),   # A2
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=100, pitch=37, start=3.75, end=4.125),  # E2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),   # G2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, comp on 2 and 4
# Bar 3: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.75),  # D
]
piano.notes.extend(piano_notes)

# Sax: motif variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # Eb5
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # C5
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.5),   # D5
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in F minor with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875),   # G2
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=100, pitch=37, start=5.25, end=5.625),  # E2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),   # A2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, comp on 2 and 4
# Bar 4: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=82, start=4.5, end=5.25),  # E
]
piano.notes.extend(piano_notes)

# Sax: motif resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # F5
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # Eb5
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625),  # D5
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),   # F5
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),   # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
