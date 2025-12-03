
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm (F, Ab, D, Eb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # Eb2
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4 with open voicings
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # D
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # Ab
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),   # D
]
piano.notes.extend(piano_notes)

# Sax: motif in Fm
# Start with F, Bb, D, Eb (Fm7) - phrase, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.0),   # Eb
    # Re-enter on the third beat with a shift in rhythm
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=2.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=2.875, end=3.0),   # D
]
sax.notes.extend(sax_notes)

# Bar 3: Drums continue, same pattern
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 3: Bass continues
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),  # Ab2
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),   # Eb2
]
bass.notes.extend(bass_notes)

# Bar 3: Piano continues with open voicings
piano_notes = [
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # Ab
]
piano.notes.extend(piano_notes)

# Bar 4: Drums on 1 and 3, snare on 2 and 4, hihat on every eighth
# Already added above

# Bar 4: Bass continues
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),   # Eb2
]
bass.notes.extend(bass_notes)

# Bar 4: Piano continues with open voicings
piano_notes = [
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),   # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),   # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),   # D
]
piano.notes.extend(piano_notes)

# Bar 4: Sax completes the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.0),   # Eb
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
# midi.write disabled
