
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

# Kick on beat 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1: 0.0 - 1.5s
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bar 2 (1.5 - 3.0s)
# Drums
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
])

# Bass (Marcus) - D2 (MIDI 38) to F#2 (MIDI 42) with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Eb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # F#2
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2
]

# Piano (Diane) - Open voicings, different chord each bar
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C4
]

# Sax (Dante) - One short motif, haunting and incomplete
# Start on F#4 (MIDI 71), rest on beat 2, then A4 (MIDI 73) on beat 3
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=73, start=2.625, end=2.875),
]

# Bar 3 (3.0 - 4.5s)
# Drums
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
])

# Bass (Marcus) - D2 (MIDI 38) to B2 (MIDI 45) with chromatic approach
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),  # Eb2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # F#2
    pretty_midi.Note(velocity=90, pitch=44, start=4.125, end=4.5),  # G#2
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.875),  # B2
])

# Piano (Diane) - D7 (D, F#, A, C#)
piano_notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # C#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # F#4
])

# Sax (Dante) - Continue the motif, resolve on beat 4
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.625),  # Bb4
    pretty_midi.Note(velocity=110, pitch=73, start=4.125, end=4.375),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.75),  # G4
])

# Bar 4 (4.5 - 6.0s)
# Drums
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
])

# Bass (Marcus) - D2 (MIDI 38) to F#2 (MIDI 42) with chromatic approach
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),  # Eb2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # F#2
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # D2
])

# Piano (Diane) - Dm7 (D, F, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # C4
])

# Sax (Dante) - End with a rest, leave it hanging
# No note on last beat, let the silence speak

# Add notes to instruments
drums.notes.extend(drum_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
