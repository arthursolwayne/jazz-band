
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full ensemble (1.5 - 3.0s)
# Bass: D2 (MIDI 38), F#2 (MIDI 41), G2 (MIDI 43), A2 (MIDI 45)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # F#2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 on 3
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),  # A2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chords each bar
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # C4
]
# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F4
])
# Bar 4: A7 (A C# E G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),  # C#4
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),  # E4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # G4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging. Make it sing.
# D4 (62) -> F#4 (67) -> A4 (69) -> D5 (72), then resolve back to D4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Bass (A2 on beat 1)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),  # A2 on 1
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),  # F#2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),  # G2 on 3
    pretty_midi.Note(velocity=100, pitch=45, start=4.125, end=4.5),  # A2 on 4
]
bass.notes.extend(bass_notes)

# Bar 4: Piano (resolve A7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # C#4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G4
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
