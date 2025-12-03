
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (MIDI 53) - C2 (MIDI 48), chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),   # F2 on 1
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.25),  # E2 on 2
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.625),  # C2 on 3
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),   # D2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, shifting chords
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # E4
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # Ab4
])
# Bar 4: Gm7 (G, Bb, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # F4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, haunting and incomplete
# Motif: F4 (71) on beat 1, F#4 (72) on beat 2, E4 (74) on beat 3, rest on beat 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F4 on 1
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.25), # F#4 on 2
    pretty_midi.Note(velocity=110, pitch=74, start=2.25, end=2.625), # E4 on 3
]
sax.notes.extend(sax_notes)

# Bar 3: Drums continue
# Bar 3: 1.5 - 3.0s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Drums continue
# Bar 4: 3.0 - 4.5s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Bass line (C2, Eb2, F2, G2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),  # C2 on 1
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75),  # Eb2 on 2
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125),  # F2 on 3
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),   # G2 on 4
]
bass.notes.extend(bass_notes)

# Bar 4: Piano resolves on Gm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G4 on 1
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb4 on 1
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # D4 on 1
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # F4 on 1
]
piano.notes.extend(piano_notes)

# Bar 4: Sax leaves it hanging, does not complete the motif
# (No notes on last bar)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
