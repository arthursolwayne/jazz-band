
import pretty_midi

# Initialize the MIDI file with 160 BPM (4/4 time)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define MIDI note values
# Drums: kick=36, snare=38, hihat=42
# Sax: Dm7 = D, F, A, C (MIDI 62, 65, 69, 67)
# Bass: D2-G2, roots and fifths with chromatic approaches
# Piano: Open voicings, different chord each bar, resolve on the last
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bass: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # Eb2
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # A2
]
bass.notes.extend(bass_notes)

# Piano: Dm7 -> Gm7 -> Am7 -> D7
# Open voicings, one chord per bar, resolved on last
# Bar 2: Dm7 (D, F, A, C) in open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C
]
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
]
# Bar 4: Am7 (A, C, E, G)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G
]
piano.notes.extend(piano_notes)

# Sax: Your motif — start it, leave it hanging
# Dm7: D, F, A, C — motif: D -> A -> F -> D (with space)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=2.875),  # D (return)
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.125),  # A (finish)
]
sax.notes.extend(sax_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
