
import pretty_midi

# Create a new MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Initialize instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum mappings
# Kick: 36, Snare: 38, Hihat: 42

# Bar 1: 0.0 - 1.5 sec — Drums only, Little Ray sets the mood
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),# Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # Hihat on 4
]
drums.notes.extend(drums_notes)

# Bar 2: 1.5 - 3.0 sec — Full quartet
# Marcus: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),   # C#3
    pretty_midi.Note(velocity=90, pitch=66, start=2.0, end=2.25),   # D#3
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),   # E3
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),   # F#3
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),   # E3
]
bass.notes.extend(bass_notes)

# Diane: 7th chords comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=72, start=1.5, end=1.75),   # C4 (D7 if D is the root)
    pretty_midi.Note(velocity=95, pitch=76, start=1.5, end=1.75),   # E4
    pretty_midi.Note(velocity=95, pitch=79, start=1.5, end=1.75),   # G4
    pretty_midi.Note(velocity=95, pitch=81, start=1.5, end=1.75),   # Bb4
    pretty_midi.Note(velocity=95, pitch=72, start=2.25, end=2.5),   # C4
    pretty_midi.Note(velocity=95, pitch=76, start=2.25, end=2.5),   # E4
    pretty_midi.Note(velocity=95, pitch=79, start=2.25, end=2.5),   # G4
    pretty_midi.Note(velocity=95, pitch=81, start=2.25, end=2.5),   # Bb4
]
piano.notes.extend(piano_notes)

# You: Start the motif — short, singable, with space
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),   # D4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),   # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),   # E4
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),   # D4
]
sax.notes.extend(sax_notes)

# Bar 3: 3.0 - 4.5 sec — Continue the motif, leave it hanging
# Marcus: Walking line (continuation)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.25),   # D3
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),   # C#3
    pretty_midi.Note(velocity=90, pitch=66, start=3.5, end=3.75),   # D#3
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),   # E3
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),   # F#3
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),   # E3
]
bass.notes.extend(bass_notes)

# Diane: 7th chords again
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=3.25),   # C4
    pretty_midi.Note(velocity=95, pitch=76, start=3.0, end=3.25),   # E4
    pretty_midi.Note(velocity=95, pitch=79, start=3.0, end=3.25),   # G4
    pretty_midi.Note(velocity=95, pitch=81, start=3.0, end=3.25),   # Bb4
    pretty_midi.Note(velocity=95, pitch=72, start=3.75, end=4.0),   # C4
    pretty_midi.Note(velocity=95, pitch=76, start=3.75, end=4.0),   # E4
    pretty_midi.Note(velocity=95, pitch=79, start=3.75, end=4.0),   # G4
    pretty_midi.Note(velocity=95, pitch=81, start=3.75, end=4.0),   # Bb4
]
piano.notes.extend(piano_notes)

# You: Continue the motif, leave it unresolved
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),   # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),   # E4
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.75),   # D4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),   # C#4
]
sax.notes.extend(sax_notes)

# Bar 4: 4.5 - 6.0 sec — End with a question, not a statement
# Marcus: Walking line (final notes)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.75),   # D3
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),   # C#3
    pretty_midi.Note(velocity=90, pitch=66, start=5.0, end=5.25),   # D#3
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),   # E3
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75),   # F#3
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),   # E3
]
bass.notes.extend(bass_notes)

# Diane: 7th chords again
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=4.75),   # C4
    pretty_midi.Note(velocity=95, pitch=76, start=4.5, end=4.75),   # E4
    pretty_midi.Note(velocity=95, pitch=79, start=4.5, end=4.75),   # G4
    pretty_midi.Note(velocity=95, pitch=81, start=4.5, end=4.75),   # Bb4
    pretty_midi.Note(velocity=95, pitch=72, start=5.25, end=5.5),   # C4
    pretty_midi.Note(velocity=95, pitch=76, start=5.25, end=5.5),   # E4
    pretty_midi.Note(velocity=95, pitch=79, start=5.25, end=5.5),   # G4
    pretty_midi.Note(velocity=95, pitch=81, start=5.25, end=5.5),   # Bb4
]
piano.notes.extend(piano_notes)

# You: End the motif, leave it open
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),   # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),   # E4
    pretty_midi.Note(velocity=100, pitch=66, start=5.0, end=5.25),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),   # E4
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),   # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),   # E4
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.save('dante_intro.mid')
