
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax: motif (C, E, F#, G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Bass: walking line (C, B, D, E)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=47, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4 (C7, E7)
piano_notes = [
    # Bar 2: 2nd beat (E7)
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),
    # Bar 3: 2nd beat (E7)
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),
    # Bar 4: 2nd beat (E7)
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax: repeat motif (C, E, F#, G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Bass: walking line (C, B, D, E)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4 (C7, E7)
piano_notes = [
    # Bar 3: 2nd beat (E7)
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),
    # Bar 4: 2nd beat (E7)
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Sax: repeat motif (C, E, F#, G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Bass: walking line (C, B, D, E)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4 (C7, E7)
piano_notes = [
    # Bar 4: 2nd beat (E7)
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),  # Snare
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),  # Snare
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('jazz_intro.mid')
